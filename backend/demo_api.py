"""
Demo API server - Standalone version without PostgreSQL/Redis dependencies
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import asyncio
from contextlib import asynccontextmanager

# Import our agents
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from config.demo_settings import demo_settings

# Simple in-memory storage for demo
demo_data = {
    "coins": [],
    "watchlist": []
}

class CoinResponse(BaseModel):
    symbol: str
    name: str
    current_price: float
    market_cap: float
    volume_24h: float
    price_change_24h: float
    current_phase: str
    phase_confidence: float
    opportunity_score: float
    recommendation: str

class StatsResponse(BaseModel):
    total_coins: int
    total_opportunities: int
    accumulation_count: int
    expansion_count: int
    hype_count: int
    crash_count: int

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize demo data on startup"""
    print("🚀 Starting Crypto Research AI Agent - Demo Mode")
    print("=" * 60)
    
    # Load initial demo data
    await initialize_demo_data()
    
    yield
    
    print("👋 Shutting down...")

app = FastAPI(
    title="Crypto Research AI Agent - Demo",
    description="Autonomous cryptocurrency research and investment analysis",
    version="1.0.0-demo",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=demo_settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def initialize_demo_data():
    """Load sample data for demonstration"""
    from agents.data_collector.collector import DataCollectorAgent
    from agents.phase_detector.detector import PhaseDetectorAgent
    from scoring.engine import ScoringEngine
    import pandas as pd
    import numpy as np
    
    print("📊 Loading demo data...")
    
    # Top coins to fetch
    top_coins = ["bitcoin", "ethereum", "solana", "cardano", "polkadot"]
    
    collector = DataCollectorAgent()
    detector = PhaseDetectorAgent()
    scorer = ScoringEngine()
    
    for coin_id in top_coins:
        try:
            # Collect real data from CoinGecko
            async with collector:
                data = await collector.collect_coingecko_data(coin_id)
                
                if data:
                    # Generate sample price history for phase detection
                    dates = pd.date_range(end=datetime.now(), periods=365, freq='D')
                    base_price = data.get('current_price', 100)
                    
                    # Simulate different phases for demo
                    if coin_id == "bitcoin":
                        # Accumulation phase
                        trend = np.linspace(0, base_price * 0.1, 365)
                        noise = np.random.normal(0, base_price * 0.02, 365)
                    elif coin_id == "ethereum":
                        # Expansion phase
                        trend = np.linspace(0, base_price * 0.3, 365)
                        noise = np.random.normal(0, base_price * 0.03, 365)
                    elif coin_id == "solana":
                        # Hype phase
                        trend = np.linspace(0, base_price * 0.5, 365)
                        noise = np.random.normal(0, base_price * 0.05, 365)
                    else:
                        # Mixed/Unknown
                        trend = np.linspace(0, base_price * 0.05, 365)
                        noise = np.random.normal(0, base_price * 0.02, 365)
                    
                    prices = base_price * 0.7 + trend + noise
                    
                    price_history = pd.DataFrame({
                        'timestamp': dates,
                        'open': prices * 0.99,
                        'high': prices * 1.02,
                        'low': prices * 0.98,
                        'close': prices,
                        'volume': np.random.randint(1000000, 100000000, 365)
                    })
                    
                    # Detect phase
                    phase_result = detector.detect_phase(price_history)
                    
                    # Calculate opportunity score
                    score_result = scorer.calculate_opportunity_score(
                        fundamental_score=np.random.randint(60, 90),
                        technical_score=np.random.randint(55, 85),
                        onchain_score=np.random.randint(50, 80),
                        sentiment_score=np.random.randint(45, 75),
                        phase=phase_result['phase'],
                        phase_confidence=phase_result['confidence']
                    )
                    
                    # Store in demo data
                    coin_data = {
                        "symbol": data['symbol'].upper(),
                        "name": data['name'],
                        "current_price": data.get('current_price', 0),
                        "market_cap": data.get('market_cap', 0),
                        "volume_24h": data.get('volume_24h', 0),
                        "price_change_24h": data.get('price_change_24h', 0),
                        "current_phase": phase_result['phase'].value,
                        "phase_confidence": phase_result['confidence'],
                        "opportunity_score": score_result['opportunity_score'],
                        "recommendation": score_result['recommendation'].value,
                        "last_updated": datetime.now().isoformat()
                    }
                    
                    demo_data["coins"].append(coin_data)
                    print(f"  ✅ {coin_data['symbol']:6} - {coin_data['name']:15} | Phase: {coin_data['current_phase']:12} | Score: {coin_data['opportunity_score']:.1f}")
                    
        except Exception as e:
            print(f"  ⚠️  Error loading {coin_id}: {str(e)[:50]}")
    
    print(f"\n✅ Loaded {len(demo_data['coins'])} coins successfully!")
    print("=" * 60)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Crypto Research AI Agent - Demo Mode",
        "status": "running",
        "docs": "/docs",
        "coins_loaded": len(demo_data["coins"])
    }

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "mode": "demo",
        "timestamp": datetime.now().isoformat(),
        "coins_loaded": len(demo_data["coins"])
    }

@app.get("/api/coins", response_model=List[CoinResponse])
async def get_coins(
    phase: Optional[str] = None,
    min_score: Optional[float] = None,
    limit: int = 100
):
    """Get all coins with optional filtering"""
    coins = demo_data["coins"].copy()
    
    # Filter by phase
    if phase:
        coins = [c for c in coins if c["current_phase"].lower() == phase.lower()]
    
    # Filter by minimum score
    if min_score is not None:
        coins = [c for c in coins if c["opportunity_score"] >= min_score]
    
    # Sort by opportunity score
    coins.sort(key=lambda x: x["opportunity_score"], reverse=True)
    
    # Limit results
    coins = coins[:limit]
    
    return coins

@app.get("/api/coins/{symbol}")
async def get_coin(symbol: str):
    """Get detailed information for a specific coin"""
    symbol = symbol.upper()
    coin = next((c for c in demo_data["coins"] if c["symbol"] == symbol), None)
    
    if not coin:
        raise HTTPException(status_code=404, detail=f"Coin {symbol} not found")
    
    return coin

@app.get("/api/watchlist")
async def get_watchlist():
    """Get user's watchlist"""
    watchlist_symbols = demo_data["watchlist"]
    watchlist_coins = [c for c in demo_data["coins"] if c["symbol"] in watchlist_symbols]
    return watchlist_coins

@app.post("/api/watchlist/{symbol}")
async def add_to_watchlist(symbol: str):
    """Add coin to watchlist"""
    symbol = symbol.upper()
    
    # Check if coin exists
    coin = next((c for c in demo_data["coins"] if c["symbol"] == symbol), None)
    if not coin:
        raise HTTPException(status_code=404, detail=f"Coin {symbol} not found")
    
    # Add to watchlist if not already there
    if symbol not in demo_data["watchlist"]:
        demo_data["watchlist"].append(symbol)
    
    return {"message": f"{symbol} added to watchlist", "watchlist": demo_data["watchlist"]}

@app.delete("/api/watchlist/{symbol}")
async def remove_from_watchlist(symbol: str):
    """Remove coin from watchlist"""
    symbol = symbol.upper()
    
    if symbol in demo_data["watchlist"]:
        demo_data["watchlist"].remove(symbol)
    
    return {"message": f"{symbol} removed from watchlist", "watchlist": demo_data["watchlist"]}

@app.get("/api/stats/overview", response_model=StatsResponse)
async def get_overview_stats():
    """Get overview statistics"""
    coins = demo_data["coins"]
    
    return {
        "total_coins": len(coins),
        "total_opportunities": len([c for c in coins if c["opportunity_score"] >= 70]),
        "accumulation_count": len([c for c in coins if c["current_phase"] == "accumulation"]),
        "expansion_count": len([c for c in coins if c["current_phase"] == "expansion"]),
        "hype_count": len([c for c in coins if c["current_phase"] == "hype"]),
        "crash_count": len([c for c in coins if c["current_phase"] == "crash"])
    }

@app.get("/api/stats/phase-distribution")
async def get_phase_distribution():
    """Get phase distribution for charts"""
    coins = demo_data["coins"]
    
    phases = {}
    for coin in coins:
        phase = coin["current_phase"]
        phases[phase] = phases.get(phase, 0) + 1
    
    return phases

@app.post("/api/analyze/trigger")
async def trigger_analysis():
    """Manually trigger a new analysis cycle"""
    # Reload demo data
    await initialize_demo_data()
    return {
        "message": "Analysis triggered successfully",
        "coins_analyzed": len(demo_data["coins"]),
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    print(f"\n🌐 Starting server at http://{demo_settings.api_host}:{demo_settings.api_port}")
    print(f"📚 API Documentation: http://{demo_settings.api_host}:{demo_settings.api_port}/docs")
    print(f"🎯 Demo Mode - No database required!\n")
    
    uvicorn.run(
        app,
        host=demo_settings.api_host,
        port=demo_settings.api_port,
        log_level="info"
    )
