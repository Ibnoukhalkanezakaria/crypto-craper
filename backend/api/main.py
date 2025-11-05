"""
FastAPI application - Main API endpoints.
"""
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta

from config.settings import settings
from config.database import get_db
from models.database import Coin, MarketPhase, Recommendation
from api.schemas import (
    CoinResponse, CoinDetailResponse, WatchlistResponse,
    PhaseHistoryResponse, AlertResponse
)

# Create FastAPI app
app = FastAPI(
    title="Crypto Research AI Agent API",
    description="Autonomous cryptocurrency research and analysis platform",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint - API information."""
    return {
        "name": "Crypto Research AI Agent API",
        "version": "1.0.0",
        "status": "operational",
        "endpoints": {
            "coins": "/api/coins",
            "watchlist": "/api/watchlist",
            "coin_detail": "/api/coins/{symbol}",
            "phase_history": "/api/phases/{symbol}",
            "alerts": "/api/alerts"
        }
    }


@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/api/coins", response_model=List[CoinResponse])
async def get_coins(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    phase: Optional[MarketPhase] = None,
    min_score: Optional[float] = Query(None, ge=0, le=100),
    db: Session = Depends(get_db)
):
    """
    Get list of analyzed coins.
    
    Parameters:
    - skip: Number of records to skip (pagination)
    - limit: Maximum number of records to return
    - phase: Filter by market phase
    - min_score: Minimum opportunity score
    """
    query = db.query(Coin).filter(Coin.is_active == True)
    
    if phase:
        query = query.filter(Coin.current_phase == phase)
    
    if min_score is not None:
        query = query.filter(Coin.opportunity_score >= min_score)
    
    # Order by opportunity score
    query = query.order_by(Coin.opportunity_score.desc())
    
    coins = query.offset(skip).limit(limit).all()
    
    return coins


@app.get("/api/coins/{symbol}", response_model=CoinDetailResponse)
async def get_coin_detail(
    symbol: str,
    db: Session = Depends(get_db)
):
    """
    Get detailed information about a specific coin.
    
    Parameters:
    - symbol: Cryptocurrency symbol (e.g., BTC, ETH)
    """
    coin = db.query(Coin).filter(Coin.symbol == symbol.upper()).first()
    
    if not coin:
        raise HTTPException(status_code=404, detail=f"Coin {symbol} not found")
    
    # Load relationships
    fundamental = coin.fundamental_data
    recent_onchain = db.query(coin.onchain_metrics).order_by(
        coin.onchain_metrics.c.timestamp.desc()
    ).limit(30).all() if coin.onchain_metrics else []
    
    recent_sentiment = db.query(coin.sentiment_data).order_by(
        coin.sentiment_data.c.timestamp.desc()
    ).limit(30).all() if coin.sentiment_data else []
    
    return {
        "coin": coin,
        "fundamental": fundamental,
        "onchain_history": recent_onchain,
        "sentiment_history": recent_sentiment
    }


@app.get("/api/watchlist", response_model=List[WatchlistResponse])
async def get_watchlist(
    limit: int = Query(50, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Get top coins in watchlist (highest opportunity scores).
    
    Parameters:
    - limit: Maximum number of coins to return
    """
    coins = db.query(Coin).filter(
        Coin.is_active == True,
        Coin.in_watchlist == True
    ).order_by(
        Coin.opportunity_score.desc()
    ).limit(limit).all()
    
    return coins


@app.post("/api/watchlist/{symbol}")
async def add_to_watchlist(
    symbol: str,
    db: Session = Depends(get_db)
):
    """
    Add a coin to watchlist.
    
    Parameters:
    - symbol: Cryptocurrency symbol
    """
    coin = db.query(Coin).filter(Coin.symbol == symbol.upper()).first()
    
    if not coin:
        raise HTTPException(status_code=404, detail=f"Coin {symbol} not found")
    
    coin.in_watchlist = True
    db.commit()
    
    return {"message": f"{symbol} added to watchlist"}


@app.delete("/api/watchlist/{symbol}")
async def remove_from_watchlist(
    symbol: str,
    db: Session = Depends(get_db)
):
    """
    Remove a coin from watchlist.
    
    Parameters:
    - symbol: Cryptocurrency symbol
    """
    coin = db.query(Coin).filter(Coin.symbol == symbol.upper()).first()
    
    if not coin:
        raise HTTPException(status_code=404, detail=f"Coin {symbol} not found")
    
    coin.in_watchlist = False
    db.commit()
    
    return {"message": f"{symbol} removed from watchlist"}


@app.get("/api/phases/{symbol}", response_model=PhaseHistoryResponse)
async def get_phase_history(
    symbol: str,
    days: int = Query(90, ge=1, le=365),
    db: Session = Depends(get_db)
):
    """
    Get market phase history for a coin.
    
    Parameters:
    - symbol: Cryptocurrency symbol
    - days: Number of days of history
    """
    coin = db.query(Coin).filter(Coin.symbol == symbol.upper()).first()
    
    if not coin:
        raise HTTPException(status_code=404, detail=f"Coin {symbol} not found")
    
    # Get price history with phase detection
    start_date = datetime.utcnow() - timedelta(days=days)
    
    from models.database import PriceHistory
    
    history = db.query(PriceHistory).filter(
        PriceHistory.coin_id == coin.id,
        PriceHistory.timestamp >= start_date
    ).order_by(PriceHistory.timestamp.asc()).all()
    
    return {
        "symbol": symbol,
        "current_phase": coin.current_phase,
        "current_confidence": coin.phase_confidence,
        "history": history
    }


@app.get("/api/alerts", response_model=List[AlertResponse])
async def get_alerts(
    unsent_only: bool = Query(False),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db)
):
    """
    Get recent alerts.
    
    Parameters:
    - unsent_only: Only return unsent alerts
    - limit: Maximum number of alerts
    """
    from models.database import Alert
    
    query = db.query(Alert)
    
    if unsent_only:
        query = query.filter(Alert.is_sent == False)
    
    alerts = query.order_by(
        Alert.created_at.desc()
    ).limit(limit).all()
    
    return alerts


@app.get("/api/stats/overview")
async def get_overview_stats(db: Session = Depends(get_db)):
    """Get overview statistics."""
    total_coins = db.query(Coin).filter(Coin.is_active == True).count()
    
    phase_counts = {}
    for phase in MarketPhase:
        count = db.query(Coin).filter(
            Coin.is_active == True,
            Coin.current_phase == phase
        ).count()
        phase_counts[phase.value] = count
    
    top_opportunities = db.query(Coin).filter(
        Coin.is_active == True,
        Coin.opportunity_score >= 70
    ).count()
    
    return {
        "total_coins": total_coins,
        "phase_distribution": phase_counts,
        "top_opportunities": top_opportunities,
        "watchlist_count": db.query(Coin).filter(
            Coin.in_watchlist == True
        ).count()
    }


@app.get("/api/stats/phase-distribution")
async def get_phase_distribution(db: Session = Depends(get_db)):
    """Get distribution of coins across market phases."""
    distribution = []
    
    for phase in MarketPhase:
        count = db.query(Coin).filter(
            Coin.is_active == True,
            Coin.current_phase == phase
        ).count()
        
        avg_score = db.query(Coin).filter(
            Coin.is_active == True,
            Coin.current_phase == phase
        ).with_entities(
            Coin.opportunity_score
        ).all()
        
        avg = sum(s[0] for s in avg_score) / len(avg_score) if avg_score else 0
        
        distribution.append({
            "phase": phase.value,
            "count": count,
            "avg_opportunity_score": round(avg, 2)
        })
    
    return distribution


@app.post("/api/analyze/trigger")
async def trigger_analysis():
    """
    Manually trigger a full analysis cycle.
    This endpoint queues analysis tasks.
    """
    from agents.orchestrator.celery_app import analyze_all_coins
    
    task = analyze_all_coins.delay()
    
    return {
        "message": "Analysis triggered",
        "task_id": task.id
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug
    )
