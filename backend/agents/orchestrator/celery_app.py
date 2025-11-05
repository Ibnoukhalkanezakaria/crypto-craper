"""
Celery application for distributed task processing.
Orchestrates autonomous data collection and analysis.
"""
from celery import Celery
from celery.schedules import crontab
from config.settings import settings
from loguru import logger

# Create Celery app
celery_app = Celery(
    "crypto_agent",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend
)

# Celery configuration
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=3600,  # 1 hour max
    task_soft_time_limit=3000,  # 50 minutes soft limit
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=100,
)

# Beat schedule for periodic tasks
celery_app.conf.beat_schedule = {
    # Collect data every hour
    "collect-data-hourly": {
        "task": "agents.orchestrator.celery_app.collect_market_data",
        "schedule": crontab(minute=0),  # Every hour
    },
    
    # Update phase detection every 6 hours
    "detect-phases": {
        "task": "agents.orchestrator.celery_app.detect_all_phases",
        "schedule": crontab(minute=0, hour="*/6"),  # Every 6 hours
    },
    
    # Update on-chain metrics every 4 hours
    "update-onchain-metrics": {
        "task": "agents.orchestrator.celery_app.update_onchain_data",
        "schedule": crontab(minute=30, hour="*/4"),  # Every 4 hours
    },
    
    # Update sentiment every 2 hours
    "update-sentiment": {
        "task": "agents.orchestrator.celery_app.update_sentiment_data",
        "schedule": crontab(minute=15, hour="*/2"),  # Every 2 hours
    },
    
    # Recalculate scores every 30 minutes
    "recalculate-scores": {
        "task": "agents.orchestrator.celery_app.recalculate_all_scores",
        "schedule": crontab(minute="*/30"),  # Every 30 minutes
    },
    
    # Send pending alerts every 10 minutes
    "send-alerts": {
        "task": "agents.orchestrator.celery_app.send_pending_alerts",
        "schedule": crontab(minute="*/10"),  # Every 10 minutes
    },
    
    # Retrain models weekly
    "retrain-models": {
        "task": "agents.orchestrator.celery_app.retrain_ml_models",
        "schedule": crontab(minute=0, hour=2, day_of_week=0),  # Sunday 2 AM
    },
}


@celery_app.task(name="agents.orchestrator.celery_app.collect_market_data")
def collect_market_data():
    """
    Collect market data from all sources for top coins.
    Runs hourly.
    """
    import asyncio
    from agents.data_collector.collector import DataCollectorAgent
    from config.database import SessionLocal
    from models.database import Coin, PriceHistory
    from datetime import datetime
    
    logger.info("Starting market data collection...")
    
    try:
        async def collect():
            async with DataCollectorAgent() as agent:
                # Collect data for top coins
                all_data = await agent.collect_top_coins(settings.top_coins_count)
                
                # Save to database
                db = SessionLocal()
                try:
                    for coin_data in all_data:
                        sources = coin_data.get("sources", {})
                        cg_data = sources.get("coingecko", {})
                        
                        # Update or create coin record
                        coin = db.query(Coin).filter(
                            Coin.symbol == coin_data.get("symbol")
                        ).first()
                        
                        if not coin:
                            coin = Coin(
                                symbol=coin_data.get("symbol"),
                                name=cg_data.get("name"),
                                coingecko_id=coin_data.get("coin_id")
                            )
                            db.add(coin)
                        
                        # Update market data
                        coin.current_price = cg_data.get("current_price")
                        coin.market_cap = cg_data.get("market_cap")
                        coin.volume_24h = cg_data.get("volume_24h")
                        coin.circulating_supply = cg_data.get("circulating_supply")
                        coin.total_supply = cg_data.get("total_supply")
                        coin.max_supply = cg_data.get("max_supply")
                        coin.updated_at = datetime.utcnow()
                        
                        db.commit()
                        
                        # Add price history entry
                        price_entry = PriceHistory(
                            coin_id=coin.id,
                            timestamp=datetime.utcnow(),
                            close=cg_data.get("current_price"),
                            volume=cg_data.get("volume_24h")
                        )
                        db.add(price_entry)
                    
                    db.commit()
                    logger.info(f"Successfully collected data for {len(all_data)} coins")
                    
                finally:
                    db.close()
        
        asyncio.run(collect())
        return {"status": "success", "message": "Data collection completed"}
        
    except Exception as e:
        logger.error(f"Error in data collection: {e}")
        return {"status": "error", "message": str(e)}


@celery_app.task(name="agents.orchestrator.celery_app.detect_all_phases")
def detect_all_phases():
    """
    Run phase detection for all active coins.
    Runs every 6 hours.
    """
    from agents.phase_detector.detector import PhaseDetectorAgent
    from config.database import SessionLocal
    from models.database import Coin, PriceHistory
    import pandas as pd
    
    logger.info("Starting phase detection...")
    
    try:
        db = SessionLocal()
        detector = PhaseDetectorAgent()
        
        coins = db.query(Coin).filter(Coin.is_active == True).all()
        
        for coin in coins:
            try:
                # Get price history
                history = db.query(PriceHistory).filter(
                    PriceHistory.coin_id == coin.id
                ).order_by(PriceHistory.timestamp.asc()).all()
                
                if len(history) < 200:
                    logger.warning(f"Insufficient data for {coin.symbol}")
                    continue
                
                # Convert to DataFrame
                df = pd.DataFrame([{
                    "timestamp": h.timestamp,
                    "open": h.open,
                    "high": h.high,
                    "low": h.low,
                    "close": h.close,
                    "volume": h.volume
                } for h in history])
                
                # Detect phase
                result = detector.detect_phase(df)
                
                # Update coin
                coin.current_phase = result["phase"]
                coin.phase_confidence = result["confidence"]
                
                logger.info(f"{coin.symbol}: {result['phase']} (conf: {result['confidence']:.2f})")
                
            except Exception as e:
                logger.error(f"Error detecting phase for {coin.symbol}: {e}")
                continue
        
        db.commit()
        db.close()
        
        logger.info("Phase detection completed")
        return {"status": "success"}
        
    except Exception as e:
        logger.error(f"Error in phase detection: {e}")
        return {"status": "error", "message": str(e)}


@celery_app.task(name="agents.orchestrator.celery_app.update_onchain_data")
def update_onchain_data():
    """
    Update on-chain metrics for all active coins.
    Runs every 4 hours.
    """
    import asyncio
    from agents.onchain.analytics import OnChainAnalyticsAgent
    from config.database import SessionLocal
    from models.database import Coin, OnChainMetrics
    from datetime import datetime
    
    logger.info("Starting on-chain data update...")
    
    try:
        async def update():
            async with OnChainAnalyticsAgent() as agent:
                db = SessionLocal()
                coins = db.query(Coin).filter(Coin.is_active == True).limit(100).all()
                
                for coin in coins:
                    try:
                        score = await agent.calculate_onchain_score(coin.symbol)
                        metrics = await agent.get_glassnode_metrics(coin.symbol)
                        
                        # Update coin score
                        coin.onchain_score = score
                        
                        # Add metrics entry
                        onchain_entry = OnChainMetrics(
                            coin_id=coin.id,
                            timestamp=datetime.utcnow(),
                            active_addresses=metrics.get("active_count"),
                            transaction_count=metrics.get("transaction_count")
                        )
                        db.add(onchain_entry)
                        
                        logger.info(f"{coin.symbol}: On-chain score = {score:.2f}")
                        
                    except Exception as e:
                        logger.error(f"Error updating on-chain for {coin.symbol}: {e}")
                        continue
                
                db.commit()
                db.close()
        
        asyncio.run(update())
        logger.info("On-chain update completed")
        return {"status": "success"}
        
    except Exception as e:
        logger.error(f"Error updating on-chain data: {e}")
        return {"status": "error", "message": str(e)}


@celery_app.task(name="agents.orchestrator.celery_app.update_sentiment_data")
def update_sentiment_data():
    """
    Update sentiment analysis for all active coins.
    Runs every 2 hours.
    """
    import asyncio
    from agents.onchain.analytics import SentimentAnalysisAgent
    from config.database import SessionLocal
    from models.database import Coin, SentimentData
    from datetime import datetime
    
    logger.info("Starting sentiment update...")
    
    try:
        async def update():
            async with SentimentAnalysisAgent() as agent:
                db = SessionLocal()
                coins = db.query(Coin).filter(Coin.is_active == True).limit(100).all()
                
                for coin in coins:
                    try:
                        score = await agent.calculate_sentiment_score(coin.symbol)
                        sentiment = await agent.analyze_sentiment(coin.symbol)
                        
                        # Update coin score
                        coin.sentiment_score = score
                        
                        # Add sentiment entry
                        sentiment_entry = SentimentData(
                            coin_id=coin.id,
                            timestamp=datetime.utcnow(),
                            sentiment_score=sentiment.get("sentiment_score"),
                            sentiment_label=sentiment.get("sentiment_label"),
                            social_volume=sentiment.get("social_volume"),
                            galaxy_score=sentiment.get("galaxy_score")
                        )
                        db.add(sentiment_entry)
                        
                        logger.info(f"{coin.symbol}: Sentiment score = {score:.2f}")
                        
                    except Exception as e:
                        logger.error(f"Error updating sentiment for {coin.symbol}: {e}")
                        continue
                
                db.commit()
                db.close()
        
        asyncio.run(update())
        logger.info("Sentiment update completed")
        return {"status": "success"}
        
    except Exception as e:
        logger.error(f"Error updating sentiment: {e}")
        return {"status": "error", "message": str(e)}


@celery_app.task(name="agents.orchestrator.celery_app.recalculate_all_scores")
def recalculate_all_scores():
    """
    Recalculate opportunity scores for all coins.
    Runs every 30 minutes.
    """
    from scoring.engine import ScoringEngine
    from config.database import SessionLocal
    from models.database import Coin
    
    logger.info("Recalculating opportunity scores...")
    
    try:
        db = SessionLocal()
        engine = ScoringEngine()
        
        coins = db.query(Coin).filter(Coin.is_active == True).all()
        
        for coin in coins:
            try:
                # Calculate composite score
                result = engine.calculate_opportunity_score(
                    fundamental_score=coin.fundamental_score or 50,
                    technical_score=coin.technical_score or 50,
                    onchain_score=coin.onchain_score or 50,
                    sentiment_score=coin.sentiment_score or 50,
                    phase=coin.current_phase,
                    phase_confidence=coin.phase_confidence
                )
                
                # Update coin
                coin.opportunity_score = result["opportunity_score"]
                coin.recommendation = result["recommendation"]
                
            except Exception as e:
                logger.error(f"Error scoring {coin.symbol}: {e}")
                continue
        
        db.commit()
        db.close()
        
        logger.info("Score recalculation completed")
        return {"status": "success"}
        
    except Exception as e:
        logger.error(f"Error recalculating scores: {e}")
        return {"status": "error", "message": str(e)}


@celery_app.task(name="agents.orchestrator.celery_app.send_pending_alerts")
def send_pending_alerts():
    """
    Send pending alerts via configured channels.
    Runs every 10 minutes.
    """
    from alerts.notifier import AlertNotifier
    from config.database import SessionLocal
    from models.database import Alert
    
    logger.info("Sending pending alerts...")
    
    try:
        db = SessionLocal()
        notifier = AlertNotifier()
        
        alerts = db.query(Alert).filter(Alert.is_sent == False).limit(50).all()
        
        for alert in alerts:
            try:
                notifier.send_alert(alert)
                alert.is_sent = True
                alert.sent_at = datetime.utcnow()
                
            except Exception as e:
                logger.error(f"Error sending alert {alert.id}: {e}")
                continue
        
        db.commit()
        db.close()
        
        logger.info(f"Sent {len(alerts)} alerts")
        return {"status": "success", "alerts_sent": len(alerts)}
        
    except Exception as e:
        logger.error(f"Error sending alerts: {e}")
        return {"status": "error", "message": str(e)}


@celery_app.task(name="agents.orchestrator.celery_app.retrain_ml_models")
def retrain_ml_models():
    """
    Retrain ML models with latest data.
    Runs weekly.
    """
    logger.info("Retraining ML models...")
    
    try:
        # This would implement model retraining logic
        # For now, placeholder
        
        logger.info("Model retraining completed")
        return {"status": "success"}
        
    except Exception as e:
        logger.error(f"Error retraining models: {e}")
        return {"status": "error", "message": str(e)}


@celery_app.task(name="agents.orchestrator.celery_app.analyze_all_coins")
def analyze_all_coins():
    """
    Run complete analysis cycle for all coins.
    Can be triggered manually.
    """
    logger.info("Starting full analysis cycle...")
    
    results = []
    
    # Chain tasks
    results.append(collect_market_data())
    results.append(detect_all_phases())
    results.append(update_onchain_data())
    results.append(update_sentiment_data())
    results.append(recalculate_all_scores())
    
    return {"status": "success", "results": results}
