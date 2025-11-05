"""
Configuration management for the crypto research AI agent.
"""
from typing import Optional, List
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Environment
    environment: str = Field(default="development", alias="ENVIRONMENT")
    debug: bool = Field(default=True, alias="DEBUG")
    
    # API Configuration
    api_host: str = Field(default="0.0.0.0", alias="API_HOST")
    api_port: int = Field(default=8000, alias="API_PORT")
    api_secret_key: str = Field(alias="API_SECRET_KEY")
    
    # Database
    database_url: str = Field(alias="DATABASE_URL")
    db_pool_size: int = Field(default=20, alias="DB_POOL_SIZE")
    db_max_overflow: int = Field(default=10, alias="DB_MAX_OVERFLOW")
    
    # Redis
    redis_url: str = Field(alias="REDIS_URL")
    cache_ttl: int = Field(default=300, alias="CACHE_TTL")
    
    # MongoDB
    mongodb_url: str = Field(alias="MONGODB_URL")
    
    # Celery
    celery_broker_url: str = Field(alias="CELERY_BROKER_URL")
    celery_result_backend: str = Field(alias="CELERY_RESULT_BACKEND")
    
    # API Keys - Data Sources
    coingecko_api_key: Optional[str] = Field(default=None, alias="COINGECKO_API_KEY")
    coinmarketcap_api_key: Optional[str] = Field(default=None, alias="COINMARKETCAP_API_KEY")
    messari_api_key: Optional[str] = Field(default=None, alias="MESSARI_API_KEY")
    glassnode_api_key: Optional[str] = Field(default=None, alias="GLASSNODE_API_KEY")
    santiment_api_key: Optional[str] = Field(default=None, alias="SANTIMENT_API_KEY")
    lunarcrush_api_key: Optional[str] = Field(default=None, alias="LUNARCRUSH_API_KEY")
    cryptoquant_api_key: Optional[str] = Field(default=None, alias="CRYPTOQUANT_API_KEY")
    
    # AI/LLM Keys
    openai_api_key: Optional[str] = Field(default=None, alias="OPENAI_API_KEY")
    anthropic_api_key: Optional[str] = Field(default=None, alias="ANTHROPIC_API_KEY")
    
    # Notification Services
    telegram_bot_token: Optional[str] = Field(default=None, alias="TELEGRAM_BOT_TOKEN")
    telegram_chat_id: Optional[str] = Field(default=None, alias="TELEGRAM_CHAT_ID")
    discord_webhook_url: Optional[str] = Field(default=None, alias="DISCORD_WEBHOOK_URL")
    
    smtp_host: Optional[str] = Field(default=None, alias="SMTP_HOST")
    smtp_port: int = Field(default=587, alias="SMTP_PORT")
    smtp_username: Optional[str] = Field(default=None, alias="SMTP_USERNAME")
    smtp_password: Optional[str] = Field(default=None, alias="SMTP_PASSWORD")
    email_from: Optional[str] = Field(default=None, alias="EMAIL_FROM")
    email_to: Optional[str] = Field(default=None, alias="EMAIL_TO")
    
    # Agent Configuration
    data_collection_interval: int = Field(default=60, alias="DATA_COLLECTION_INTERVAL")
    top_coins_count: int = Field(default=500, alias="TOP_COINS_COUNT")
    phase_detection_interval: int = Field(default=6, alias="PHASE_DETECTION_INTERVAL")
    onchain_analysis_interval: int = Field(default=4, alias="ONCHAIN_ANALYSIS_INTERVAL")
    scoring_update_interval: int = Field(default=30, alias="SCORING_UPDATE_INTERVAL")
    
    # ML Model Settings
    model_retrain_interval: int = Field(default=7, alias="MODEL_RETRAIN_INTERVAL")
    alert_confidence_threshold: float = Field(default=0.75, alias="ALERT_CONFIDENCE_THRESHOLD")
    backtesting_period: int = Field(default=365, alias="BACKTESTING_PERIOD")
    
    # Scraping Configuration
    user_agent: str = Field(
        default="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
        alias="USER_AGENT"
    )
    scraping_delay: int = Field(default=2, alias="SCRAPING_DELAY")
    max_concurrent_requests: int = Field(default=10, alias="MAX_CONCURRENT_REQUESTS")
    selenium_headless: bool = Field(default=True, alias="SELENIUM_HEADLESS")
    
    # Security
    cors_origins: str = Field(
        default="http://localhost:3000,http://localhost:5173",
        alias="CORS_ORIGINS"
    )
    jwt_secret_key: str = Field(alias="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", alias="JWT_ALGORITHM")
    jwt_expiration_hours: int = Field(default=24, alias="JWT_EXPIRATION_HOURS")
    
    # Logging
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    log_format: str = Field(default="json", alias="LOG_FORMAT")
    
    # Feature Flags
    enable_telegram_alerts: bool = Field(default=True, alias="ENABLE_TELEGRAM_ALERTS")
    enable_discord_alerts: bool = Field(default=True, alias="ENABLE_DISCORD_ALERTS")
    enable_email_alerts: bool = Field(default=False, alias="ENABLE_EMAIL_ALERTS")
    enable_web_scraping: bool = Field(default=True, alias="ENABLE_WEB_SCRAPING")
    enable_ml_models: bool = Field(default=True, alias="ENABLE_ML_MODELS")
    enable_sentiment_analysis: bool = Field(default=True, alias="ENABLE_SENTIMENT_ANALYSIS")
    enable_onchain_analysis: bool = Field(default=True, alias="ENABLE_ONCHAIN_ANALYSIS")
    
    @property
    def cors_origins_list(self) -> List[str]:
        """Get CORS origins as a list."""
        return [origin.strip() for origin in self.cors_origins.split(",")]
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "allow"  # Allow extra fields from .env


# Global settings instance
settings = Settings()
