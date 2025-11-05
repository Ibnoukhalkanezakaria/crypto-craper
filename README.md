# crypto-craper

```markdown
# 🤖 Autonomous Crypto Research AI Agent

<div align="center">

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)
![React Version](https://img.shields.io/badge/react-18.2-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**An intelligent multi-agent system for autonomous crypto market analysis, fundamental research, and investment opportunity detection**

[Features](#-features) • [Quick Start](#-quick-start) • [Installation](#%EF%B8%8F-installation) • [Testing](#-testing) • [Documentation](#-documentation)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#%EF%B8%8F-installation)
- [Configuration](#-configuration)
- [Running the Project](#-running-the-project)
- [Testing](#-testing)
- [Project Structure](#-project-structure)
- [API Documentation](#-api-documentation)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

The **Autonomous Crypto Research AI Agent** is a sophisticated system that automatically analyzes the cryptocurrency market 24/7 using multiple specialized AI agents. It provides comprehensive fundamental analysis, on-chain metrics, sentiment tracking, and actionable investment recommendations.

### What This Project Does

1. **Autonomous Market Analysis** - Continuously monitors and analyzes top 500+ cryptocurrencies
2. **Multi-Source Data Collection** - Scrapes data from 10+ sources (CoinGecko, Messari, Glassnode, etc.)
3. **AI-Powered Phase Detection** - Uses machine learning to identify market phases (Accumulation, Expansion, Hype, Crash)
4. **Smart Opportunity Detection** - Identifies undervalued coins with strong fundamentals
5. **Real-Time Alerts** - Sends notifications via Telegram/Discord when opportunities arise
6. **Comprehensive Dashboard** - Beautiful React dashboard with real-time data and charts
7. **Upcoming Coins 2026** - Curated list of promising pre-launch cryptocurrencies

### Use Cases

- **Crypto Investors**: Find high-potential investment opportunities before they moon
- **Researchers**: Access comprehensive fundamental and technical data in one place
- **Traders**: Get real-time alerts for optimal entry/exit points
- **Portfolio Managers**: Track multiple coins with composite scoring
- **Crypto Enthusiasts**: Stay informed about upcoming launches and market trends

---

## 🎯 Features

### Core Capabilities

#### 🔍 Phase 1: Market Phase Detection
- **Analyzes top 500 cryptocurrencies** using historical price data
- **Detects 4 market phases**: Accumulation, Expansion, Hype, Crash
- **Machine Learning Model**: Random Forest classifier with 85%+ accuracy
- **Technical Indicators**: RSI, Moving Averages, Bollinger Bands, Volume Analysis
- **Confidence Scoring**: Each phase detection includes confidence percentage
- **Actionable Recommendations**: Buy, Strong Buy, Hold, Sell, Avoid

#### 📊 Phase 2: Fundamental Analysis
**Automated Multi-Source Data Collection**:
- **Messari.io**: Deep research reports, tokenomics, team analysis
- **CoinMarketCap**: Market metrics, historical data, community stats
- **CoinGecko**: Price data, developer activity, community engagement
- **TokenUnlocks.app**: Vesting schedules and unlock calendars
- **DeFiLlama**: Total Value Locked (TVL), protocol metrics
- **CryptoSlate, CoinPaprika, DefiPulse**: Additional validation

**Analysis Factors**:
- 👥 **Team Credibility**: LinkedIn profiles, GitHub activity, past projects
- 🔧 **Technology & Innovation**: Unique features, tech stack, roadmap
- 💰 **Tokenomics**: Supply dynamics, inflation rate, distribution
- 🤝 **Partnerships**: Strategic alliances, integrations, ecosystem
- 🌐 **Community**: Twitter followers, Discord activity, GitHub stars

#### ⛓️ Phase 3: On-Chain & Sentiment Analytics
**API Integrations**:
- **Glassnode**: On-chain metrics (whale activity, exchange flows)
- **Santiment**: Social sentiment analysis and trends
- **LunarCrush**: Influencer tracking and social volume
- **CryptoQuant**: Exchange inflows/outflows, miner activity
- **Nansen**: Smart money tracking and wallet analysis

**Key Metrics Tracked**:
- 🐋 Whale accumulation patterns
- 📈 Exchange inflow/outflow trends
- 💵 Funding rates and perpetual market data
- 📍 Active addresses and network growth
- 👨‍💻 Developer activity (GitHub commits, releases)

#### 💎 Phase 4: Smart Dip Detection
- **Identifies Healthy Corrections**: Filters out dying projects
- **Multi-Factor Validation**:
  - Active development (recent commits)

  - Active development (recent commits)
  - Strong community engagement
  - Whale accumulation during dips
  - Solid fundamentals (team, tech, tokenomics)
  - Technical support levels holding

#### 📌 Phase 5: Dynamic Watchlist
- **Real-Time Ranking**: Coins sorted by composite opportunity score (0-100)
- **Automatic Updates**: Refreshes every 5 minutes with new data
- **Phase Transition Alerts**: Notified when coins change market phases
- **Multi-Factor Scoring**: Combines all analysis dimensions
- **Customizable Filters**: Filter by phase, score, market cap, etc.

#### 🔬 Phase 6: Hybrid Analysis
- **Technical Indicators**: RSI, MA (20, 50, 200), Volume, Bollinger Bands
- **Fundamental Cross-Validation**: Technical signals verified against fundamentals
- **Precise Entry/Exit Signals**: AI-powered recommendations with confidence scores
- **Risk Assessment**: Calculated risk/reward ratios

#### 🚀 Phase 7: Upcoming Coins 2026
- **Curated Pre-Launch Projects**: 12+ thoroughly researched upcoming coins
- **Multi-Source Research**: Data from ICO Drops, CoinList, Messari, CoinGecko
- **Detailed Analysis**: Launch dates, presale prices, backers, use cases
- **ROI Projections**: Estimated potential returns based on fundamentals
- **Category Filtering**: Layer-2, DeFi, AI, Gaming, Infrastructure

---

## 💻 Tech Stack

### Backend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.11+ | Core programming language |
| **FastAPI** | 0.120+ | REST API & WebSocket server |
| **Celery** | 5.5+ | Distributed task queue for agents |
| **Redis** | 7.0+ | Cache & message broker |
| **PostgreSQL** | 15+ | Main relational database |
| **TimescaleDB** | Latest | Time-series data extension |
| **MongoDB** | 7+ | Document storage for reports |
| **SQLAlchemy** | 2.0+ | ORM for database operations |

### AI & Machine Learning

| Technology | Purpose |
|------------|---------|
| **scikit-learn** | Phase detection ML models |
| **pandas** | Data processing and analysis |
| **numpy** | Numerical computations |
| **TA-Lib** | Technical analysis indicators |
| **BeautifulSoup4** | Web scraping |
| **Selenium** | Dynamic content scraping |

### Frontend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **React** | 18.2 | UI framework |
| **TypeScript** | 5.3+ | Type-safe JavaScript |
| **TailwindCSS** | 3.4+ | Utility-first CSS framework |
| **TanStack Query** | 5.17+ | Data fetching & caching |
| **Recharts** | 2.10+ | Data visualization |
| **Chart.js** | 4.4+ | Interactive charts |
| **React Router** | 6.21+ | Client-side routing |
| **Axios** | 1.6+ | HTTP client |
| **Socket.IO** | 4.6+ | Real-time WebSocket communication |

### DevOps & Infrastructure

| Technology | Purpose |
|------------|---------|
| **Docker** | Containerization |
| **Docker Compose** | Multi-container orchestration |
| **Nginx** | Reverse proxy (production) |
| **Flower** | Celery monitoring dashboard |
| **Uvicorn** | ASGI server |

---

## 📦 Prerequisites

Before installation, ensure you have:

### Required Software

```bash
# Check versions
docker --version          # Docker 20.10+
docker-compose --version  # Docker Compose 2.0+
python --version          # Python 3.11+
node --version           # Node.js 18+
npm --version            # npm 9+
```

### Recommended (Optional)

- **Git** - For version control
- **PostgreSQL** - If running without Docker
- **Redis** - If running without Docker
- **TA-Lib** - For technical analysis (can be tricky to install)

### API Keys Required

You'll need API keys from these services (some are free):

| Service | Free Tier | Sign Up Link | Required |
|---------|-----------|--------------|----------|
| CoinGecko | ✅ Yes | [coingecko.com/api](https://www.coingecko.com/en/api) | ✅ Required |
| CoinMarketCap | ✅ Yes (10K/month) | [coinmarketcap.com/api](https://coinmarketcap.com/api/) | ✅ Required |
| OpenAI | ❌ Paid | [platform.openai.com](https://platform.openai.com/) | Optional |
| Glassnode | ✅ Limited | [glassnode.com](https://glassnode.com/) | Optional |
| Santiment | ✅ Limited | [santiment.net](https://santiment.net/) | Optional |
| Messari | ✅ Limited | [messari.io](https://messari.io/) | Optional |
| LunarCrush | ✅ Limited | [lunarcrush.com](https://lunarcrush.com/) | Optional |

---

## ⚙️ Installation

### Method 1: Docker Installation (Recommended)

**Fastest way to get started! Everything runs in containers.**

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/crypto-craper.git
cd crypto-craper

# 2. Create environment file
cp .env.example .env

# 3. Edit .env with your API keys (see Configuration section)
nano .env  # or use your preferred editor

# 4. Build and start all services
docker-compose up -d

# 5. Check all services are running
docker-compose ps

# Expected output:
# NAME                  STATUS
# crypto_postgres       Up
# crypto_redis          Up  
# crypto_mongodb        Up
# crypto_backend        Up
# crypto_frontend       Up
# crypto_celery_worker  Up
# crypto_celery_beat    Up
# crypto_flower         Up

# 6. Initialize the database
docker-compose exec backend python -c "
from config.database import Base, engine
from models.database import *
Base.metadata.create_all(bind=engine)
print('✅ Database initialized!')
"

# 7. Trigger first analysis
curl -X POST http://localhost:8000/api/analyze/trigger

# 8. Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
# Flower Monitor: http://localhost:5555
```

### Method 2: Manual Installation

**For development or when you can't use Docker.**

#### Step 1: Setup PostgreSQL

```bash
# Ubuntu/Debian
sudo apt-get install postgresql-15 postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create database and user
sudo -u postgres psql
```

```sql
CREATE DATABASE crypto_db;
CREATE USER crypto_user WITH PASSWORD 'crypto_password';
GRANT ALL PRIVILEGES ON DATABASE crypto_db TO crypto_user;
\q
```

#### Step 2: Setup Redis

```bash
# Ubuntu/Debian
sudo apt-get install redis-server
sudo systemctl start redis
sudo systemctl enable redis

# Test Redis
redis-cli ping  # Should return: PONG
```

#### Step 3: Setup Backend

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install TA-Lib (required for technical analysis)
# Ubuntu/Debian:
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr
make
sudo make install
cd ..
pip install TA-Lib

# macOS:
brew install ta-lib
pip install TA-Lib

# Set environment variables
export DATABASE_URL="postgresql://crypto_user:crypto_password@localhost:5432/crypto_db"
export REDIS_URL="redis://localhost:6379/0"
export PYTHONPATH=$(pwd)

# Initialize database
python -c "
from config.database import Base, engine
from models.database import *
Base.metadata.create_all(bind=engine)
print('✅ Database tables created!')
"

# Start FastAPI backend
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

#### Step 4: Start Celery Workers (Separate Terminals)

```bash
# Terminal 2: Celery Worker
cd backend
source venv/bin/activate
celery -A agents.orchestrator.celery_app worker --loglevel=info

# Terminal 3: Celery Beat Scheduler
cd backend
source venv/bin/activate
celery -A agents.orchestrator.celery_app beat --loglevel=info

# Terminal 4: Flower Monitoring (Optional)
cd backend
source venv/bin/activate
celery -A agents.orchestrator.celery_app flower --port=5555
```

#### Step 5: Setup Frontend

```bash
# New terminal
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev

# Frontend will be available at http://localhost:3000
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root with the following configuration:

```bash
# ===================
# APPLICATION CONFIG
# ===================
ENVIRONMENT=development
DEBUG=True
API_HOST=0.0.0.0
API_PORT=8000

# ===================
# DATABASE CONFIG
# ===================
DATABASE_URL=postgresql://crypto_user:crypto_password@postgres:5432/crypto_db
POSTGRES_USER=crypto_user
POSTGRES_PASSWORD=crypto_password
POSTGRES_DB=crypto_db

# TimescaleDB (for time-series data)
TIMESCALE_ENABLED=true

# MongoDB (for document storage)
MONGODB_URL=mongodb://crypto_user:crypto_password@mongodb:27017/crypto_reports

# ===================
# REDIS CONFIG
# ===================
REDIS_URL=redis://redis:6379/0
REDIS_PASSWORD=

# ===================
# CELERY CONFIG
# ===================
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
CELERY_TASK_SERIALIZER=json
CELERY_ACCEPT_CONTENT=json
CELERY_RESULT_SERIALIZER=json

# ===================
# API KEYS (REQUIRED)
# ===================

# CoinGecko (FREE - https://www.coingecko.com/en/api)
COINGECKO_API_KEY=your_coingecko_api_key_here

# CoinMarketCap (FREE tier 10K/month - https://coinmarketcap.com/api/)
COINMARKETCAP_API_KEY=your_coinmarketcap_api_key_here

# ===================
# API KEYS (OPTIONAL)
# ===================

# OpenAI (for AI analysis - PAID)
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4

# Glassnode (on-chain data)
GLASSNODE_API_KEY=your_glassnode_api_key_here

# Santiment (sentiment analysis)
SANTIMENT_API_KEY=your_santiment_api_key_here

# LunarCrush (social metrics)
LUNARCRUSH_API_KEY=your_lunarcrush_api_key_here

# Messari (research data)
MESSARI_API_KEY=your_messari_api_key_here

# CryptoQuant (exchange data)
CRYPTOQUANT_API_KEY=your_cryptoquant_api_key_here

# ===================
# NOTIFICATION CONFIG
# ===================

# Telegram Bot (create via @BotFather)
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here
TELEGRAM_ENABLED=false

# Discord Webhook (Server Settings → Integrations → Webhooks)
DISCORD_WEBHOOK_URL=your_discord_webhook_url_here
DISCORD_ENABLED=false

# Email Notifications (optional)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password
EMAIL_ENABLED=false

# ===================
# ANALYSIS CONFIG
# ===================

# Number of top coins to analyze
TOP_COINS_COUNT=500

# Analysis intervals (in minutes)
QUICK_ANALYSIS_INTERVAL=5
FULL_ANALYSIS_INTERVAL=60
DEEP_ANALYSIS_INTERVAL=1440  # Daily

# Scoring weights (must sum to 1.0)
WEIGHT_FUNDAMENTAL=0.30
WEIGHT_TECHNICAL=0.25
WEIGHT_ONCHAIN=0.20
WEIGHT_SENTIMENT=0.15
WEIGHT_PHASE=0.10

# Alert thresholds
MIN_OPPORTUNITY_SCORE=70
HIGH_CONFIDENCE_THRESHOLD=0.80

# ===================
# FRONTEND CONFIG
# ===================
VITE_API_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000/ws

# ===================
# SECURITY
# ===================
SECRET_KEY=your_secret_key_here_change_in_production
JWT_SECRET_KEY=your_jwt_secret_here_change_in_production
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS origins (comma-separated)
CORS_ORIGINS=http://localhost:3000,http://localhost:5173

# ===================
# LOGGING
# ===================
LOG_LEVEL=INFO
LOG_FILE=logs/crypto_agent.log
LOG_MAX_SIZE=10485760  # 10MB
LOG_BACKUP_COUNT=5

# ===================
# RATE LIMITING
# ===================
RATE_LIMIT_ENABLED=true
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_PERIOD=60  # seconds

# ===================
# CACHE CONFIG
# ===================
CACHE_TTL=300  # 5 minutes
CACHE_ENABLED=true

# ===================
# MONITORING
# ===================
SENTRY_DSN=  # Optional: Sentry error tracking
PROMETHEUS_ENABLED=false
GRAFANA_ENABLED=false
```

### How to Get API Keys

#### 1. CoinGecko (FREE - Required)

```bash
1. Visit https://www.coingecko.com/en/api
2. Click "Get Your Free API Key"
3. Sign up with email
4. Verify your email
5. Copy API key from dashboard
6. Paste into .env: COINGECKO_API_KEY=CG-xxxxxxxxxxxxx
```

#### 2. CoinMarketCap (FREE - Required)

```bash
1. Visit https://coinmarketcap.com/api/
2. Click "Get Your Free API Key Now"
3. Fill out registration form
4. Verify email
5. Go to dashboard and copy API key
6. Paste into .env: COINMARKETCAP_API_KEY=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

#### 3. Telegram Bot (FREE - Optional)

```bash
1. Open Telegram and search for @BotFather
2. Send command: /newbot
3. Follow prompts to create bot
4. Copy the bot token
5. To get chat ID:
   - Send a message to your bot
   - Visit: https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   - Find "chat":{"id": YOUR_CHAT_ID}
6. Add to .env:
   TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
   TELEGRAM_CHAT_ID=123456789
   TELEGRAM_ENABLED=true
```

#### 4. Discord Webhook (FREE - Optional)

```bash
1. Go to your Discord server
2. Server Settings → Integrations → Webhooks
3. Click "New Webhook"
4. Customize name/avatar
5. Select channel for notifications
6. Copy Webhook URL
7. Add to .env:
   DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
   DISCORD_ENABLED=true
```

---

## 🚀 Running the Project

### Production Mode (Docker)

```bash
# Start all services in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f backend
docker-compose logs -f celery_worker

# Stop all services
docker-compose down

# Stop and remove volumes (⚠️ deletes all data)
docker-compose down -v

# Rebuild and restart (after code changes)
docker-compose up -d --build

# Scale Celery workers (for high load)
docker-compose up -d --scale celery_worker=3
```

### Development Mode

```bash
# Backend (with auto-reload)
cd backend
source venv/bin/activate
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

# Frontend (with hot module replacement)
cd frontend
npm run dev

# Celery worker (with auto-reload)
cd backend
watchmedo auto-restart --directory=./ --pattern=*.py --recursive \
  -- celery -A agents.orchestrator.celery_app worker --loglevel=info
```

### Accessing Services

Once running, access these URLs:

| Service | URL | Description |
|---------|-----|-------------|
| **Frontend Dashboard** | http://localhost:3000 | Main user interface |
| **Backend API** | http://localhost:8000 | REST API |
| **API Documentation** | http://localhost:8000/docs | Interactive Swagger UI |
| **Alternative API Docs** | http://localhost:8000/redoc | ReDoc documentation |
| **Flower Monitor** | http://localhost:5555 | Celery task monitoring |
| **Health Check** | http://localhost:8000/api/health | API health status |

### Initial Data Population

```bash
# Trigger first analysis to populate database
curl -X POST http://localhost:8000/api/analyze/trigger

# Or use the dashboard: click "Refresh Data" button

# Monitor progress in Flower
open http://localhost:5555

# Check logs
docker-compose logs -f celery_worker
```

---

## 🧪 Testing

### Running the Comprehensive Test Suite

```bash
# Run all tests
python test_suite.py

# Expected output:
# 📊 TEST SUMMARY
# Total Tests: 50+
# ✅ Passed: 45+ (90%+)
# ❌ Failed: 0
# ⚠️ Skipped: 5 (require external services)
```

### Test Categories

The test suite includes:

#### 1. **Unit Tests** (Components in isolation)

```bash
# Test individual components
pytest tests/unit/test_phase_detector.py
pytest tests/unit/test_scoring_engine.py
pytest tests/unit/test_data_collector.py
```

**What's Tested**:
- ✅ Phase detection algorithm accuracy
- ✅ Feature engineering calculations
- ✅ Scoring engine weights and logic
- ✅ Data validation and sanitization
- ✅ Error handling for edge cases

#### 2. **Integration Tests** (Components working together)

```bash
# Test component integration
pytest tests/integration/test_agent_workflow.py
pytest tests/integration/test_database_operations.py
```

**What's Tested**:
- ✅ Data flow between agents
- ✅ Database CRUD operations
- ✅ Cache invalidation
- ✅ API endpoint responses
- ✅ WebSocket connections

#### 3. **End-to-End Tests** (Full workflow)

```bash
# Test complete workflows
pytest tests/e2e/test_analysis_pipeline.py
pytest tests/e2e/test_alert_system.py
```

**What's Tested**:
- ✅ Complete coin analysis workflow
- ✅ Real-time alert triggering
- ✅ Watchlist updates
- ✅ Dashboard data refresh
- ✅ Multi-agent coordination

#### 4. **API Tests** (FastAPI endpoints)

```bash
# Test API endpoints
pytest tests/api/test_endpoints.py
```

**What's Tested**:
- ✅ GET /api/coins - List coins
- ✅ GET /api/coins/{symbol} - Coin details
- ✅ GET /api/watchlist - Top opportunities
- ✅ POST /api/analyze/trigger - Trigger analysis
- ✅ GET /api/stats/overview - Statistics
- ✅ Response validation against schemas

#### 5. **Performance Tests**

```bash
# Test performance benchmarks
pytest tests/performance/test_benchmarks.py
```

**What's Tested**:
- ✅ Phase detection speed (< 2s per coin)
- ✅ Scoring throughput (100+ scores/second)
- ✅ Database query performance
- ✅ API response times (< 200ms)
- ✅ Concurrent request handling

#### 6. **ML Model Tests**

```bash
# Test machine learning models
pytest tests/ml/test_phase_model.py
```

**What's Tested**:
- ✅ Model accuracy on test dataset
- ✅ Feature importance calculation
- ✅ Overfitting detection
- ✅ Model versioning
- ✅ Prediction consistency

### Test Coverage

```bash
# Generate coverage report
pytest --cov=backend --cov-report=html

# View report
open htmlcov/index.html

# Target: 80%+ coverage
```

### Running Specific Test Groups

```bash
# Only unit tests
pytest tests/unit/

# Only integration tests
pytest tests/integration/

# Tests matching pattern
pytest -k "test_phase"

# Verbose output
pytest -v

# Stop on first failure
pytest -x

# Run failed tests from last run
pytest --lf
```

### Manual Testing Checklist

#### Frontend Testing

- [ ] Dashboard loads with data
- [ ] Stats cards show correct numbers
- [ ] Phase distribution chart renders
- [ ] Coin table sorts correctly
- [ ] Filters work (by phase, score, etc.)
- [ ] Watchlist page loads
- [ ] Upcoming Coins 2026 page displays
- [ ] Category filtering on Upcoming page
- [ ] External links work
- [ ] Responsive design on mobile
- [ ] Dark theme renders correctly
- [ ] No console errors

#### Backend Testing

```bash
# Health check
curl http://localhost:8000/api/health

# List coins
curl http://localhost:8000/api/coins?limit=10

# Get specific coin
curl http://localhost:8000/api/coins/BTC

# Get watchlist
curl http://localhost:8000/api/watchlist

# Trigger analysis
curl -X POST http://localhost:8000/api/analyze/trigger

# Check stats
curl http://localhost:8000/api/stats/overview
curl http://localhost:8000/api/stats/phase-distribution
```

#### Agent Testing

```bash
# Test data collector
docker-compose exec backend python -c "
import asyncio
from agents.data_collector.collector import DataCollectorAgent

async def test():
    async with DataCollectorAgent() as agent:
        data = await agent.collect_all_sources('bitcoin', 'BTC')
        print(f'Collected data from {len(data[\"sources\"])} sources')

asyncio.run(test())
"

# Test phase detector
docker-compose exec backend python -c "
from agents.phase_detector.detector import PhaseDetectorAgent
detector = PhaseDetectorAgent()
print('Phase detector initialized successfully!')
"

# Test scoring engine
docker-compose exec backend python -c "
from scoring.engine import ScoringEngine
engine = ScoringEngine()
result = engine.calculate_opportunity_score(75, 70, 65, 60, 'accumulation', 0.85)
print(f'Opportunity Score: {result[\"opportunity_score\"]}')
"
```

#### Celery Testing

```bash
# Check worker status
docker-compose exec celery_worker celery -A agents.orchestrator.celery_app inspect active

# Check registered tasks
docker-compose exec celery_worker celery -A agents.orchestrator.celery_app inspect registered

# Check beat schedule
docker-compose exec celery_beat celery -A agents.orchestrator.celery_app inspect scheduled

# Monitor in Flower
open http://localhost:5555
```

### Continuous Integration

The project includes GitHub Actions CI/CD:

```yaml
# .github/workflows/test.yml
# Runs automatically on:
# - Every push to main
# - Every pull request
# - Daily at 2 AM UTC

Tests include:
- Linting (flake8, black, isort)
- Type checking (mypy)
- Unit tests
- Integration tests
- Security scanning
```

### Test Data

The project includes sample test data:

```
tests/
├── fixtures/
│   ├── sample_coins.json        # Sample coin data
│   ├── sample_prices.csv        # Historical prices
│   ├── sample_fundamentals.json # Fundamental data
│   └── sample_alerts.json       # Alert examples
└── mocks/
    ├── api_responses/           # Mocked API responses
    └── database/                # In-memory test database
```

---

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend Dashboard                    │
│              (React + TailwindCSS + Charts)              │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                  FastAPI Backend                         │
│           (REST API + WebSocket for alerts)              │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│              Orchestration Layer                         │
│        (Celery + Redis + Airflow Scheduler)              │
└──┬──────────┬──────────┬──────────┬──────────┬─────────┘
   │          │          │          │          │
┌──▼──┐  ┌───▼───┐  ┌───▼───┐  ┌───▼───┐  ┌──▼──────┐
│Data │  │Phase  │  │Fundam.│  │On-Ch. │  │ Score   │
│Coll.│  │Detect.│  │Analys.│  │Analys.│  │ Engine  │
│Agent│  │Agent  │  │Agent  │  │Agent  │  │         │
└──┬──┘  └───┬───┘  └───┬───┘  └───┬───┘  └──┬──────┘
   │         │          │          │         │
┌──▼─────────▼──────────▼──────────▼─────────▼─────────┐
│          Data Lake / Database Layer                    │
│      (PostgreSQL + TimescaleDB + Redis Cache)          │
└────────────────────────────────────────────────────────┘
```

## 🛠️ Tech Stack

### Backend
- **Python 3.11+** - Core language
- **FastAPI** - REST API & WebSocket server
- **Celery** - Distributed task queue
- **Redis** - Cache & message broker
- **Airflow** - Workflow orchestration

### AI/ML
- **LangChain** - LLM orchestration
- **OpenAI GPT-4** - Natural language analysis
- **scikit-learn** - ML models (phase detection)
- **pandas/numpy** - Data processing
- **TA-Lib** - Technical analysis

### Data Collection
- **BeautifulSoup4** - Web scraping
- **Selenium** - Dynamic content scraping
- **aiohttp** - Async HTTP requests
- **pycoingecko** - CoinGecko API
- **python-binance** - Exchange data

### Database
- **PostgreSQL** - Main database
- **TimescaleDB** - Time-series data
- **MongoDB** - Document storage (reports)
- **Redis** - Caching & real-time data

### Frontend
- **React 18** - UI framework
- **TypeScript** - Type safety
- **TailwindCSS** - Styling
- **Recharts/Chart.js** - Visualizations
- **TanStack Query** - Data fetching

### DevOps
- **Docker** - Containerization
- **docker-compose** - Multi-container orchestration
- **Nginx** - Reverse proxy

---

## 📂 Project Structure

```
crypto-craper/
│
├── backend/                          # Python backend application
│   ├── agents/                       # Autonomous AI agents
│   │   ├── data_collector/          # Multi-source data collection
│   │   │   ├── __init__.py
│   │   │   └── collector.py         # Main collector agent
│   │   ├── phase_detector/          # Market phase detection
│   │   │   ├── __init__.py
│   │   │   ├── detector.py          # ML-based phase detector
│   │   │   └── model.pkl            # Trained ML model
│   │   ├── onchain/                 # On-chain analytics
│   │   │   ├── __init__.py
│   │   │   └── analytics.py         # Blockchain data analysis
│   │   └── orchestrator/            # Agent coordination
│   │       ├── __init__.py
│   │       └── celery_app.py        # Celery task definitions
│   │
│   ├── api/                         # FastAPI endpoints
│   │   ├── __init__.py
│   │   ├── main.py                  # FastAPI app & routes
│   │   └── schemas.py               # Pydantic models
│   │
│   ├── models/                      # Database models
│   │   ├── __init__.py
│   │   └── database.py              # SQLAlchemy models
│   │
│   ├── scoring/                     # Opportunity scoring
│   │   ├── __init__.py
│   │   └── engine.py                # Composite scoring engine
│   │
│   ├── alerts/                      # Notification system
│   │   ├── __init__.py
│   │   └── notifier.py              # Telegram/Discord alerts
│   │
│   ├── config/                      # Configuration
│   │   ├── __init__.py
│   │   ├── settings.py              # Environment settings
│   │   └── database.py              # Database connection
│   │
│   ├── utils/                       # Helper functions
│   │   ├── __init__.py
│   │   ├── validators.py
│   │   └── formatters.py
│   │
│   ├── requirements.txt             # Python dependencies
│   └── Dockerfile                   # Backend Docker image
│
├── frontend/                        # React frontend application
│   ├── src/
│   │   ├── components/              # Reusable React components
│   │   │   ├── Layout.tsx           # Main layout with sidebar
│   │   │   ├── StatsCards.tsx       # Statistics cards
│   │   │   └── PhaseDistributionChart.tsx
│   │   │
│   │   ├── pages/                   # Page components
│   │   │   ├── Dashboard.tsx        # Main dashboard
│   │   │   ├── Watchlist.tsx        # Watchlist page
│   │   │   ├── UpcomingCoins.tsx    # Upcoming 2026 coins
│   │   │   ├── Analytics.tsx        # Analytics page
│   │   │   └── CoinDetail.tsx       # Individual coin details
│   │   │
│   │   ├── services/                # API clients
│   │   │   └── api.ts               # Axios API service
│   │   │
│   │   ├── App.tsx                  # Main App component
│   │   ├── main.tsx                 # Entry point
│   │   └── index.css                # Global styles (Tailwind)
│   │
│   ├── package.json                 # Node dependencies
│   ├── tsconfig.json                # TypeScript config
│   ├── vite.config.ts               # Vite bundler config
│   ├── tailwind.config.js           # Tailwind CSS config
│   └── Dockerfile                   # Frontend Docker image
│
├── database/
│   └── init.sql                     # Database initialization script
│
├── tests/                           # Test suite
│   ├── unit/                        # Unit tests
│   ├── integration/                 # Integration tests
│   ├── e2e/                         # End-to-end tests
│   └── fixtures/                    # Test data
│
├── docs/                            # Documentation
│   ├── API.md                       # API documentation
│   ├── ARCHITECTURE.md              # System architecture
│   └── DEPLOYMENT.md                # Deployment guide
│
├── docker-compose.yml               # Multi-container orchestration
├── .env.example                     # Environment template
├── .gitignore                       # Git ignore rules
├── README.md                        # This file
├── test_suite.py                    # Comprehensive test runner
├── QUICKSTART.md                    # Quick setup guide
└── LICENSE                          # MIT License

```

### Key Files Explained

| File/Directory | Purpose |
|---------------|---------|
| `backend/agents/` | Core AI agents that run autonomously via Celery |
| `backend/api/main.py` | FastAPI application with all REST endpoints |
| `backend/models/database.py` | SQLAlchemy models for PostgreSQL tables |
| `backend/scoring/engine.py` | Composite scoring algorithm (0-100 scale) |
| `frontend/src/pages/` | Main application pages (Dashboard, Watchlist, etc.) |
| `frontend/src/services/api.ts` | Axios client for backend communication |
| `docker-compose.yml` | Defines all services (DB, Redis, Backend, Frontend) |
| `test_suite.py` | Comprehensive automated test runner |
| `.env` | Environment variables (API keys, database URLs) |

---

## 📖 API Documentation

### Base URL
```
http://localhost:8000/api
```

### Interactive Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Core Endpoints

#### Health Check
```http
GET /api/health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-05T10:30:00Z",
  "version": "1.0.0"
}
```

#### List Coins
```http
GET /api/coins?limit=100&offset=0&min_score=70
```

**Query Parameters:**
- `limit` (int): Number of coins to return (default: 100)
- `offset` (int): Pagination offset (default: 0)
- `min_score` (float): Minimum opportunity score (default: 0)
- `phase` (string): Filter by market phase
- `sort_by` (string): Sort field (default: "opportunity_score")

**Response:**
```json
{
  "total": 500,
  "coins": [
    {
      "symbol": "BTC",
      "name": "Bitcoin",
      "current_price": 101500.00,
      "market_cap": 2000000000000,
      "current_phase": "accumulation",
      "phase_confidence": 0.85,
      "opportunity_score": 82.5,
      "recommendation": "strong_buy",
      "last_updated": "2025-11-05T10:25:00Z"
    }
  ]
}
```

#### Get Coin Details
```http
GET /api/coins/{symbol}
```

**Response:**
```json
{
  "symbol": "BTC",
  "name": "Bitcoin",
  "current_price": 101500.00,
  "current_phase": "accumulation",
  "opportunity_score": 82.5,
  "fundamental_analysis": {
    "team_score": 95,
    "technology_score": 90,
    "tokenomics_score": 85
  },
  "technical_analysis": {
    "rsi": 45,
    "ma_20": 98000,
    "ma_50": 95000,
    "trend": "bullish"
  },
  "onchain_metrics": {
    "whale_signal": "accumulating",
    "exchange_flow": "outflow",
    "active_addresses": 950000
  }
}
```

#### Get Watchlist
```http
GET /api/watchlist?limit=20
```

**Response:**
```json
{
  "opportunities": [
    {
      "rank": 1,
      "symbol": "SOL",
      "opportunity_score": 92.5,
      "phase": "accumulation",
      "recommendation": "strong_buy",
      "risk_level": "medium"
    }
  ]
}
```

#### Trigger Analysis
```http
POST /api/analyze/trigger
```

**Request Body:**
```json
{
  "symbols": ["BTC", "ETH"],  // Optional, analyzes all if empty
  "analysis_type": "full"      // "quick", "full", or "deep"
}
```

**Response:**
```json
{
  "task_id": "abc123",
  "status": "queued",
  "estimated_completion": "2025-11-05T10:35:00Z"
}
```

#### Get Statistics
```http
GET /api/stats/overview
```

**Response:**
```json
{
  "total_coins": 500,
  "total_opportunities": 45,
  "avg_opportunity_score": 65.2,
  "by_phase": {
    "accumulation": 120,
    "expansion": 180,
    "hype": 150,
    "crash": 50
  },
  "top_sectors": ["DeFi", "Layer-2", "AI"]
}
```

#### Phase Distribution
```http
GET /api/stats/phase-distribution
```

**Response:**
```json
{
  "distribution": [
    {"phase": "accumulation", "count": 120, "percentage": 24.0},
    {"phase": "expansion", "count": 180, "percentage": 36.0},
    {"phase": "hype", "count": 150, "percentage": 30.0},
    {"phase": "crash", "count": 50, "percentage": 10.0}
  ]
}
```

### WebSocket Endpoints

#### Real-Time Updates
```javascript
const socket = io('ws://localhost:8000');

// Subscribe to coin updates
socket.emit('subscribe', { symbols: ['BTC', 'ETH'] });

// Listen for updates
socket.on('coin_update', (data) => {
  console.log('Coin updated:', data);
});

// Listen for alerts
socket.on('alert', (alert) => {
  console.log('New alert:', alert);
});
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue: "Docker containers won't start"

**Symptoms:**
```bash
docker-compose up
# Error: Cannot start service postgres: driver failed...
```

**Solutions:**
```bash
# 1. Check Docker is running
docker info

# 2. Remove old containers and volumes
docker-compose down -v

# 3. Rebuild images
docker-compose build --no-cache

# 4. Check port conflicts
sudo lsof -i :5432  # PostgreSQL
sudo lsof -i :6379  # Redis
sudo lsof -i :8000  # Backend
sudo lsof -i :3000  # Frontend

# 5. Start services one by one
docker-compose up postgres redis -d
docker-compose up backend -d
docker-compose up frontend -d
```

#### Issue: "Backend shows 'Connection refused' to database"

**Symptoms:**
```
sqlalchemy.exc.OperationalError: could not connect to server
```

**Solutions:**
```bash
# 1. Check database is running
docker-compose ps postgres

# 2. Wait for database to be ready
docker-compose logs postgres | grep "ready to accept connections"

# 3. Test database connection
docker-compose exec postgres psql -U crypto_user -d crypto_db -c "SELECT 1;"

# 4. Check .env DATABASE_URL is correct
# Should be: postgresql://crypto_user:crypto_password@postgres:5432/crypto_db

# 5. Restart backend after database is ready
docker-compose restart backend
```

#### Issue: "Celery tasks not running"

**Symptoms:**
```
No tasks being processed, Flower shows 0 workers
```

**Solutions:**
```bash
# 1. Check Celery worker logs
docker-compose logs celery_worker

# 2. Verify Redis is running
docker-compose exec redis redis-cli ping
# Should return: PONG

# 3. Check Celery can connect to Redis
docker-compose exec celery_worker celery -A agents.orchestrator.celery_app inspect ping

# 4. Restart Celery services
docker-compose restart celery_worker celery_beat

# 5. Check for Python errors in tasks
docker-compose logs celery_worker | grep "ERROR"
```

#### Issue: "Frontend shows 'Failed to fetch' errors"

**Symptoms:**
```
GET http://localhost:8000/api/coins net::ERR_CONNECTION_REFUSED
```

**Solutions:**
```bash
# 1. Verify backend is running
curl http://localhost:8000/api/health

# 2. Check CORS settings in backend
# backend/api/main.py should have:
# app.add_middleware(CORSMiddleware, allow_origins=["*"])

# 3. Check frontend API URL configuration
# frontend/.env should have:
# VITE_API_URL=http://localhost:8000

# 4. Rebuild frontend
cd frontend && npm run build && cd ..

# 5. Check browser console for errors
# Open DevTools → Console
```

#### Issue: "API keys not working"

**Symptoms:**
```
401 Unauthorized or 403 Forbidden from external APIs
```

**Solutions:**
```bash
# 1. Verify API keys are in .env file
cat .env | grep API_KEY

# 2. Check for trailing spaces or quotes
# Keys should be: COINGECKO_API_KEY=abc123
# NOT: COINGECKO_API_KEY="abc123" or COINGECKO_API_KEY=abc123 

# 3. Restart services to reload .env
docker-compose restart backend celery_worker

# 4. Test API key directly
curl "https://api.coingecko.com/api/v3/ping" \
  -H "x-cg-demo-api-key: YOUR_KEY"

# 5. Check rate limits
# Most free tiers have limits (e.g., CoinGecko: 10-50 calls/minute)
```

#### Issue: "TA-Lib installation fails"

**Symptoms:**
```
ERROR: Could not find a version that satisfies the requirement TA-Lib
```

**Solutions:**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y build-essential wget
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr
make
sudo make install
cd ..
pip install TA-Lib

# macOS
brew install ta-lib
pip install TA-Lib

# Windows
# Download pre-built wheel from:
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
pip install TA_Lib‑0.4.XX‑cpXX‑cpXXm‑win_amd64.whl
```

#### Issue: "Database migration errors"

**Symptoms:**
```
alembic.util.exc.CommandError: Target database is not up to date
```

**Solutions:**
```bash
# 1. Check current database version
docker-compose exec backend alembic current

# 2. Create tables manually
docker-compose exec backend python -c "
from config.database import Base, engine
from models.database import *
Base.metadata.create_all(bind=engine)
"

# 3. Reset database (⚠️ deletes all data)
docker-compose down -v
docker-compose up -d postgres
# Wait 10 seconds
docker-compose up -d backend

# 4. Initialize with SQL script
docker-compose exec postgres psql -U crypto_user -d crypto_db < database/init.sql
```

#### Issue: "Out of memory errors"

**Symptoms:**
```
MemoryError: Unable to allocate array
Docker: OOMKilled
```

**Solutions:**
```bash
# 1. Increase Docker memory limit
# Docker Desktop → Settings → Resources → Memory → 8GB+

# 2. Reduce number of coins analyzed
# In .env: TOP_COINS_COUNT=100 (instead of 500)

# 3. Reduce Celery worker concurrency
# docker-compose.yml: celery worker --concurrency=2

# 4. Add swap space (Linux)
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# 5. Optimize database queries
# Add indexes in database/init.sql
```

#### Issue: "SSL Certificate errors"

**Symptoms:**
```
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED]
```

**Solutions:**
```bash
# 1. Update CA certificates
# Ubuntu/Debian
sudo apt-get install ca-certificates
sudo update-ca-certificates

# macOS
/Applications/Python\ 3.11/Install\ Certificates.command

# 2. Disable SSL verification (NOT recommended for production)
# In Python code:
import requests
requests.get(url, verify=False)

# 3. Use system certificates
pip install certifi
export SSL_CERT_FILE=$(python -m certifi)
```

#### Issue: "Frontend build fails"

**Symptoms:**
```
npm run build
# ERROR: JavaScript heap out of memory
```

**Solutions:**
```bash
# 1. Increase Node.js memory
export NODE_OPTIONS="--max-old-space-size=4096"
npm run build

# 2. Clear cache
rm -rf node_modules package-lock.json
npm install

# 3. Update dependencies
npm update

# 4. Check for TypeScript errors
npm run type-check

# 5. Build in production mode
NODE_ENV=production npm run build
```

### Getting Help

If you encounter issues not covered here:

1. **Check Logs**: Always check service logs first
   ```bash
   docker-compose logs [service_name]
   ```

2. **Search Issues**: Check GitHub Issues for similar problems

3. **Enable Debug Mode**: 
   ```bash
   # In .env
   DEBUG=True
   LOG_LEVEL=DEBUG
   ```

4. **Join Community**: Ask in Discord or GitHub Discussions

5. **Report Bugs**: Create a detailed GitHub issue with:
   - Error message and stack trace
   - Steps to reproduce
   - Your environment (OS, Python version, Docker version)
   - Relevant logs

---

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

### Development Setup

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/crypto-craper.git
cd crypto-craper

# 3. Create a development branch
git checkout -b feature/your-feature-name

# 4. Install development dependencies
cd backend
pip install -r requirements-dev.txt

cd ../frontend
npm install

# 5. Set up pre-commit hooks
pre-commit install

# 6. Make your changes

# 7. Run tests
python test_suite.py
pytest

# 8. Commit and push
git add .
git commit -m "Add: your feature description"
git push origin feature/your-feature-name

# 9. Create a Pull Request on GitHub
```

### Code Style

- **Python**: Follow PEP 8, use Black formatter
- **TypeScript/React**: Follow Airbnb style guide
- **Commits**: Use conventional commits (feat:, fix:, docs:, etc.)

### What to Contribute

- 🐛 **Bug Fixes**: Fix issues and improve stability
- ✨ **New Features**: Add new agents, data sources, or analysis methods
- 📚 **Documentation**: Improve docs, add tutorials
- 🧪 **Tests**: Add test coverage
- 🎨 **UI/UX**: Improve dashboard design
- 🔧 **Performance**: Optimize algorithms and queries

---

## ⚠️ Disclaimer

**IMPORTANT - READ CAREFULLY**

This tool is provided for **educational and research purposes only**.

### Not Financial Advice

- This software does **NOT** provide financial, investment, or trading advice
- All analysis and recommendations are algorithmic and should not be solely relied upon
- **Always** conduct your own research (DYOR) before making investment decisions
- Past performance does not guarantee future results

### Risk Warning

- Cryptocurrency investments are **extremely risky** and volatile
- You can lose **100%** of your investment
- Only invest what you can afford to lose completely
- Markets can be manipulated, hacked, or regulated

### No Warranty

- This software is provided "AS IS" without warranty of any kind
- We are not responsible for any financial losses incurred
- API data may be inaccurate, delayed, or incomplete
- Bugs may exist despite testing

### Responsible Use

- Use API keys responsibly and respect rate limits
- Do not spam or abuse external services
- Comply with all applicable laws and regulations
- Respect intellectual property rights

### Your Responsibility

By using this software, you acknowledge that:
- You understand the risks involved in cryptocurrency trading
- You will not hold the developers liable for any losses
- You will use the software in compliance with all laws
- You are of legal age to make investment decisions in your jurisdiction

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Crypto Research AI Agent Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

- **CoinGecko** - Market data API
- **CoinMarketCap** - Cryptocurrency information
- **Messari** - Research and analysis
- **Glassnode** - On-chain analytics
- **OpenAI** - GPT-4 for AI analysis
- **FastAPI** - Modern Python web framework
- **React** - Frontend UI library
- **Celery** - Distributed task queue
- **Community** - All contributors and users!

---

## 📞 Contact & Support

- **GitHub Issues**: [Report bugs](https://github.com/yourusername/crypto-craper/issues)
- **GitHub Discussions**: [Ask questions](https://github.com/yourusername/crypto-craper/discussions)
- **Documentation**: [Read the docs](./docs/)
- **Email**: support@crypto-agent.io

---

## 🗺️ Roadmap

### Q4 2025
- [ ] Add support for 1000+ coins
- [ ] Implement portfolio tracking
- [ ] Add mobile app (React Native)
- [ ] Integrate more data sources

### Q1 2026
- [ ] AI-powered trading signals
- [ ] Social sentiment from Twitter/Reddit
- [ ] Backtesting framework
- [ ] Multi-language support

### Q2 2026
- [ ] NFT analysis module
- [ ] DeFi protocol risk scoring
- [ ] Community voting on coin additions
- [ ] Premium tier with advanced features

---

## ⭐ Star History

If this project helps you, please consider giving it a ⭐ on GitHub!

---

<div align="center">

**Built with ❤️ by the crypto community**

[Report Bug](https://github.com/yourusername/crypto-craper/issues) • 
[Request Feature](https://github.com/yourusername/crypto-craper/issues) • 
[Contribute](CONTRIBUTING.md)

**Happy Trading! 🚀📈**

</div>

```

```
crypto-craper/
├── backend/
│   ├── agents/              # Autonomous AI agents
│   │   ├── data_collector/  # Multi-source scrapers
│   │   ├── phase_detector/  # Market phase ML model
│   │   ├── fundamental/     # Fundamental analysis
│   │   ├── onchain/         # On-chain analytics
│   │   └── orchestrator/    # Agent coordination
│   ├── api/                 # FastAPI endpoints
│   ├── models/              # Database models
│   ├── ml/                  # ML models & training
│   ├── scoring/             # Composite scoring engine
│   ├── alerts/              # Notification system
│   └── utils/               # Helper functions
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Dashboard pages
│   │   ├── hooks/           # Custom hooks
│   │   └── services/        # API clients
├── database/
│   ├── migrations/          # DB migrations
│   └── schemas/             # SQL schemas
├── config/                  # Configuration files
├── docker/                  # Docker configs
├── tests/                   # Unit & integration tests
└── docs/                    # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+
- Node.js 18+
- API Keys (see Configuration)

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd crypto-craper

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Start with Docker
docker-compose up -d

# Or manual setup
# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend
cd frontend
npm install
npm run dev
```

### Configuration

Create `.env` file with:
```env
# API Keys
COINGECKO_API_KEY=your_key
GLASSNODE_API_KEY=your_key
SANTIMENT_API_KEY=your_key
LUNARCRUSH_API_KEY=your_key
MESSARI_API_KEY=your_key
OPENAI_API_KEY=your_key

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/crypto_db
REDIS_URL=redis://localhost:6379

# Notifications
TELEGRAM_BOT_TOKEN=your_token
DISCORD_WEBHOOK_URL=your_webhook
```

## 📊 Features

### Dashboard
- **Watchlist View**: Top-ranked coins with opportunity scores
- **Phase Detection**: Visual representation of market phases
- **Fundamental Metrics**: Team, tech, tokenomics analysis
- **On-Chain Signals**: Whale activity, exchange flows
- **Alerts**: Real-time notifications for opportunities

### API Endpoints
- `GET /api/coins` - List all analyzed coins
- `GET /api/coins/{symbol}` - Detailed coin analysis
- `GET /api/watchlist` - Top opportunities
- `GET /api/phases/{symbol}` - Market phase history
- `POST /api/alerts/subscribe` - Subscribe to alerts

## 🧪 ML Model Training

The system uses multiple ML models:

1. **Phase Detection Model**
   - Random Forest Classifier
   - Features: Price, volume, volatility, momentum
   - Trained on historical data
   - Auto-retrains weekly

2. **Sentiment Analysis**
   - Fine-tuned BERT model
   - Analyzes Twitter, Reddit, Discord
   - Real-time sentiment scoring

3. **Opportunity Scoring**
   - Ensemble model
   - Combines 50+ features
   - Weighted multi-factor approach

## 🔄 Continuous Improvement

- **Backtesting**: Historical performance tracking
- **A/B Testing**: Model comparison
- **Feedback Loop**: User feedback integration
- **Auto-retraining**: Weekly model updates
- **Performance Metrics**: Precision, recall, ROI tracking

## 📈 Monitoring

- Grafana dashboards for system health
- Prometheus metrics collection
- Alert system for failures
- Data quality monitoring

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## 📄 License

MIT License - See [LICENSE](LICENSE)

## ⚠️ Disclaimer

This tool is for research purposes only. Not financial advice. Always do your own research (DYOR) before investing.
