"""
Database models for the crypto research AI agent.
"""
from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Float, DateTime, Boolean, 
    Text, JSON, ForeignKey, Enum as SQLEnum, Index
)
from sqlalchemy.orm import relationship
from config.database import Base
import enum


class MarketPhase(str, enum.Enum):
    """Market phase enumeration."""
    HYPE = "hype"
    CRASH = "crash"
    ACCUMULATION = "accumulation"
    EXPANSION = "expansion"
    UNKNOWN = "unknown"


class Recommendation(str, enum.Enum):
    """Investment recommendation."""
    STRONG_BUY = "strong_buy"
    BUY = "buy"
    HOLD = "hold"
    SELL = "sell"
    AVOID = "avoid"


class Coin(Base):
    """Main coin/cryptocurrency model."""
    __tablename__ = "coins"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(20), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    coingecko_id = Column(String(100), index=True)
    coinmarketcap_id = Column(Integer, index=True)
    
    # Current metrics
    current_price = Column(Float)
    market_cap = Column(Float)
    volume_24h = Column(Float)
    circulating_supply = Column(Float)
    total_supply = Column(Float)
    max_supply = Column(Float)
    
    # Phase detection
    current_phase = Column(SQLEnum(MarketPhase), default=MarketPhase.UNKNOWN)
    phase_confidence = Column(Float, default=0.0)
    
    # Scoring
    opportunity_score = Column(Float, default=0.0)
    fundamental_score = Column(Float, default=0.0)
    technical_score = Column(Float, default=0.0)
    onchain_score = Column(Float, default=0.0)
    sentiment_score = Column(Float, default=0.0)
    
    # Recommendation
    recommendation = Column(SQLEnum(Recommendation), default=Recommendation.HOLD)
    
    # Metadata
    is_active = Column(Boolean, default=True)
    in_watchlist = Column(Boolean, default=False)
    rank = Column(Integer)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    price_history = relationship("PriceHistory", back_populates="coin", cascade="all, delete-orphan")
    fundamental_data = relationship("FundamentalData", back_populates="coin", uselist=False)
    onchain_metrics = relationship("OnChainMetrics", back_populates="coin", cascade="all, delete-orphan")
    sentiment_data = relationship("SentimentData", back_populates="coin", cascade="all, delete-orphan")
    alerts = relationship("Alert", back_populates="coin", cascade="all, delete-orphan")
    
    __table_args__ = (
        Index('idx_coin_score', 'opportunity_score'),
        Index('idx_coin_phase', 'current_phase'),
    )


class PriceHistory(Base):
    """Historical price data (time-series)."""
    __tablename__ = "price_history"
    __table_args__ = (
        Index('idx_price_coin_timestamp', 'coin_id', 'timestamp'),
        {'extend_existing': True}
    )
    
    id = Column(Integer, primary_key=True, index=True)
    coin_id = Column(Integer, ForeignKey("coins.id"), nullable=False)
    
    timestamp = Column(DateTime, nullable=False, index=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    
    # Technical indicators
    rsi = Column(Float)
    ma_20 = Column(Float)
    ma_50 = Column(Float)
    ma_200 = Column(Float)
    macd = Column(Float)
    macd_signal = Column(Float)
    
    coin = relationship("Coin", back_populates="price_history")


class FundamentalData(Base):
    """Fundamental analysis data for a coin."""
    __tablename__ = "fundamental_data"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, index=True)
    coin_id = Column(Integer, ForeignKey("coins.id"), unique=True, nullable=False)
    
    # Team & Project
    team_score = Column(Float, default=0.0)
    team_linkedin_count = Column(Integer)
    github_repo_url = Column(String(500))
    github_stars = Column(Integer)
    github_forks = Column(Integer)
    github_commits_30d = Column(Integer)
    github_contributors = Column(Integer)
    
    # Technology
    technology_score = Column(Float, default=0.0)
    blockchain_platform = Column(String(100))
    consensus_mechanism = Column(String(100))
    whitepaper_url = Column(String(500))
    
    # Tokenomics
    tokenomics_score = Column(Float, default=0.0)
    token_type = Column(String(50))
    inflation_rate = Column(Float)
    staking_apy = Column(Float)
    unlock_schedule = Column(JSON)  # From TokenUnlocks
    next_unlock_date = Column(DateTime)
    next_unlock_amount = Column(Float)
    
    # Partnerships & Ecosystem
    partnership_score = Column(Float, default=0.0)
    partnerships = Column(JSON)  # List of partnerships
    ecosystem_projects = Column(Integer)
    
    # DeFi Metrics (from DeFiLlama)
    tvl = Column(Float)
    tvl_change_24h = Column(Float)
    protocol_revenue = Column(Float)
    
    # Community
    community_score = Column(Float, default=0.0)
    twitter_followers = Column(Integer)
    telegram_members = Column(Integer)
    discord_members = Column(Integer)
    reddit_subscribers = Column(Integer)
    
    # Messari Data
    messari_report_url = Column(String(500))
    messari_risk_rating = Column(String(20))
    
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    coin = relationship("Coin", back_populates="fundamental_data")


class OnChainMetrics(Base):
    """On-chain analytics data."""
    __tablename__ = "onchain_metrics"
    __table_args__ = (
        Index('idx_onchain_coin_timestamp', 'coin_id', 'timestamp'),
        {'extend_existing': True}
    )
    
    id = Column(Integer, primary_key=True, index=True)
    coin_id = Column(Integer, ForeignKey("coins.id"), nullable=False)
    timestamp = Column(DateTime, nullable=False, index=True)
    
    # Wallet & Address Metrics
    active_addresses = Column(Integer)
    new_addresses = Column(Integer)
    whale_addresses = Column(Integer)
    
    # Exchange Flows
    exchange_inflow = Column(Float)
    exchange_outflow = Column(Float)
    exchange_netflow = Column(Float)
    exchange_balance = Column(Float)
    
    # Whale Activity
    whale_accumulation = Column(Boolean)
    large_tx_count = Column(Integer)
    whale_tx_volume = Column(Float)
    
    # Network Activity
    transaction_count = Column(Integer)
    transaction_volume = Column(Float)
    avg_transaction_value = Column(Float)
    
    # Holder Metrics
    holder_concentration = Column(Float)  # Gini coefficient
    top_10_holders_percentage = Column(Float)
    
    # Derivatives (if applicable)
    funding_rate = Column(Float)
    open_interest = Column(Float)
    
    coin = relationship("Coin", back_populates="onchain_metrics")


class SentimentData(Base):
    """Social sentiment and buzz metrics."""
    __tablename__ = "sentiment_data"
    __table_args__ = (
        Index('idx_sentiment_coin_timestamp', 'coin_id', 'timestamp'),
        {'extend_existing': True}
    )
    
    id = Column(Integer, primary_key=True, index=True)
    coin_id = Column(Integer, ForeignKey("coins.id"), nullable=False)
    timestamp = Column(DateTime, nullable=False, index=True)
    
    # Overall sentiment
    sentiment_score = Column(Float)  # -1 to 1
    sentiment_label = Column(String(20))  # positive, neutral, negative
    
    # Social volume
    twitter_mentions = Column(Integer)
    reddit_mentions = Column(Integer)
    news_mentions = Column(Integer)
    
    # Sentiment by source
    twitter_sentiment = Column(Float)
    reddit_sentiment = Column(Float)
    news_sentiment = Column(Float)
    
    # Influencer tracking (LunarCrush)
    influencer_mentions = Column(Integer)
    galaxy_score = Column(Float)  # LunarCrush proprietary score
    alt_rank = Column(Integer)
    
    # Fear & Greed
    fear_greed_index = Column(Float)
    
    coin = relationship("Coin", back_populates="sentiment_data")


class Alert(Base):
    """Alert/notification records."""
    __tablename__ = "alerts"
    __table_args__ = (
        Index('idx_alert_sent', 'is_sent', 'created_at'),
        {'extend_existing': True}
    )
    
    id = Column(Integer, primary_key=True, index=True)
    coin_id = Column(Integer, ForeignKey("coins.id"), nullable=False)
    
    alert_type = Column(String(50))  # phase_change, high_score, whale_activity, etc.
    severity = Column(String(20))  # low, medium, high, critical
    title = Column(String(200))
    message = Column(Text)
    
    alert_metadata = Column(JSON)  # Additional context
    
    is_sent = Column(Boolean, default=False)
    sent_at = Column(DateTime)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    coin = relationship("Coin", back_populates="alerts")


class MLModel(Base):
    """ML model tracking and versioning."""
    __tablename__ = "ml_models"
    __table_args__ = (
        Index('idx_model_active', 'model_type', 'is_active'),
        {'extend_existing': True}
    )
    
    id = Column(Integer, primary_key=True, index=True)
    
    model_name = Column(String(100), nullable=False)
    model_version = Column(String(50), nullable=False)
    model_type = Column(String(50))  # phase_detection, scoring, sentiment, etc.
    
    file_path = Column(String(500))
    
    # Performance metrics
    accuracy = Column(Float)
    precision = Column(Float)
    recall = Column(Float)
    f1_score = Column(Float)
    
    # Training info
    training_data_size = Column(Integer)
    training_date = Column(DateTime)
    hyperparameters = Column(JSON)
    
    is_active = Column(Boolean, default=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)


class SystemLog(Base):
    """System activity and error logs."""
    __tablename__ = "system_logs"
    __table_args__ = (
        Index('idx_log_level_timestamp', 'log_level', 'timestamp'),
        {'extend_existing': True}
    )
    
    id = Column(Integer, primary_key=True, index=True)
    
    log_level = Column(String(20))  # INFO, WARNING, ERROR, CRITICAL
    component = Column(String(100))  # data_collector, phase_detector, etc.
    message = Column(Text)
    
    log_metadata = Column(JSON)
    
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
