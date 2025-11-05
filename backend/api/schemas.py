"""
Pydantic schemas for API request/response models.
"""
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime
from models.database import MarketPhase, Recommendation


class CoinResponse(BaseModel):
    """Basic coin information response."""
    id: int
    symbol: str
    name: str
    current_price: Optional[float]
    market_cap: Optional[float]
    volume_24h: Optional[float]
    
    current_phase: MarketPhase
    phase_confidence: float
    
    opportunity_score: float
    fundamental_score: float
    technical_score: float
    onchain_score: float
    sentiment_score: float
    
    recommendation: Recommendation
    in_watchlist: bool
    rank: Optional[int]
    
    updated_at: datetime
    
    class Config:
        from_attributes = True


class FundamentalDataResponse(BaseModel):
    """Fundamental analysis data response."""
    team_score: float
    technology_score: float
    tokenomics_score: float
    community_score: float
    partnership_score: float
    
    github_stars: Optional[int]
    github_commits_30d: Optional[int]
    tvl: Optional[float]
    twitter_followers: Optional[int]
    
    class Config:
        from_attributes = True


class OnChainMetricsResponse(BaseModel):
    """On-chain metrics response."""
    timestamp: datetime
    active_addresses: Optional[int]
    exchange_netflow: Optional[float]
    whale_accumulation: Optional[bool]
    transaction_count: Optional[int]
    
    class Config:
        from_attributes = True


class SentimentDataResponse(BaseModel):
    """Sentiment data response."""
    timestamp: datetime
    sentiment_score: float
    sentiment_label: str
    social_volume: Optional[int]
    galaxy_score: Optional[float]
    
    class Config:
        from_attributes = True


class CoinDetailResponse(BaseModel):
    """Detailed coin information."""
    coin: CoinResponse
    fundamental: Optional[FundamentalDataResponse]
    onchain_history: List[OnChainMetricsResponse]
    sentiment_history: List[SentimentDataResponse]


class WatchlistResponse(BaseModel):
    """Watchlist coin response."""
    symbol: str
    name: str
    current_price: Optional[float]
    opportunity_score: float
    current_phase: MarketPhase
    recommendation: Recommendation
    
    class Config:
        from_attributes = True


class PhaseHistoryResponse(BaseModel):
    """Market phase history response."""
    symbol: str
    current_phase: MarketPhase
    current_confidence: float
    history: List[Dict]


class AlertResponse(BaseModel):
    """Alert response."""
    id: int
    coin_id: int
    alert_type: str
    severity: str
    title: str
    message: str
    is_sent: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
