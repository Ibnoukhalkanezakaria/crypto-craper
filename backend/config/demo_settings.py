"""
Standalone demo mode configuration - runs without Docker/PostgreSQL/Redis
"""
from typing import Optional, List
from pydantic_settings import BaseSettings
from pydantic import Field


class StandaloneSettings(BaseSettings):
    """Simplified settings for standalone demo mode."""
    
    # Environment
    environment: str = "demo"
    debug: bool = True
    
    # API Configuration
    api_host: str = "127.0.0.1"
    api_port: int = 8000
    
    # SQLite for demo (no PostgreSQL needed)
    database_url: str = "sqlite:///./crypto_demo.db"
    
    # API Keys - Data Sources (optional for demo)
    coingecko_api_key: Optional[str] = None
    
    # CORS for local frontend
    cors_origins: str = "http://localhost:3000,http://localhost:3001,http://localhost:5173,http://127.0.0.1:3000,http://127.0.0.1:3001,http://127.0.0.1:5173"
    
    # Feature Flags (simplified for demo)
    enable_web_scraping: bool = False
    enable_ml_models: bool = True
    enable_sentiment_analysis: bool = False
    enable_onchain_analysis: bool = False
    
    @property
    def cors_origins_list(self) -> List[str]:
        """Get CORS origins as a list."""
        return [origin.strip() for origin in self.cors_origins.split(",")]
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "allow"


# Global settings instance for demo
demo_settings = StandaloneSettings()
