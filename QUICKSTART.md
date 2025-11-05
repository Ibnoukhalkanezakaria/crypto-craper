# 🚀 Quick Start Guide - Crypto Research AI Agent

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker & Docker Compose** (v20.10+)
- **Python 3.11+** (for local development)
- **Node.js 18+** (for frontend)
- **PostgreSQL 15+** with TimescaleDB (or use Docker)

## Step 1: Clone and Setup Environment

```bash
# Navigate to your project directory
cd /home/zibnoukh/crypto-craper

# Create environment file
cp .env.example .env
```

## Step 2: Configure API Keys

Edit the `.env` file and add your API keys:

```bash
# Essential API Keys (Get these first!)
COINGECKO_API_KEY=your_key_here           # https://www.coingecko.com/en/api
COINMARKETCAP_API_KEY=your_key_here       # https://coinmarketcap.com/api/
OPENAI_API_KEY=your_key_here              # https://platform.openai.com/

# Optional but recommended
GLASSNODE_API_KEY=your_key_here           # https://glassnode.com/
SANTIMENT_API_KEY=your_key_here           # https://santiment.net/
LUNARCRUSH_API_KEY=your_key_here          # https://lunarcrush.com/
MESSARI_API_KEY=your_key_here             # https://messari.io/

# Notification channels (optional)
TELEGRAM_BOT_TOKEN=your_bot_token         # Create via @BotFather
TELEGRAM_CHAT_ID=your_chat_id
DISCORD_WEBHOOK_URL=your_webhook_url      # Server Settings → Integrations
```

### How to Get API Keys:

1. **CoinGecko** (FREE):
   - Visit https://www.coingecko.com/en/api
   - Sign up for free account
   - Get API key from dashboard

2. **CoinMarketCap** (FREE tier available):
   - Visit https://coinmarketcap.com/api/
   - Create account
   - Free tier: 10,000 calls/month

3. **OpenAI** (Paid):
   - Visit https://platform.openai.com/
   - Add payment method
   - Create API key

4. **Telegram Bot**:
   - Message @BotFather on Telegram
   - Use `/newbot` command
   - Copy the token

## Step 3: Start with Docker (Recommended)

```bash
# Build and start all services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f backend
```

Services will be available at:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Flower (Celery Monitor)**: http://localhost:5555

## Step 4: Initialize Database

```bash
# Access the database container
docker-compose exec postgres psql -U crypto_user -d crypto_db

# Run initialization script
\i /docker-entrypoint-initdb.d/init.sql

# Exit
\q
```

Alternatively, use the backend to create tables:

```bash
# Run migrations
docker-compose exec backend python -c "
from config.database import Base, engine
from models.database import *
Base.metadata.create_all(bind=engine)
print('Database tables created successfully!')
"
```

## Step 5: Test the System

### Test API Connection:

```bash
curl http://localhost:8000/api/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2025-11-02T..."
}
```

### Trigger First Analysis:

```bash
curl -X POST http://localhost:8000/api/analyze/trigger
```

### Check Celery Workers:

```bash
docker-compose exec celery_worker celery -A agents.orchestrator.celery_app inspect active
```

## Step 6: Access the Dashboard

Open your browser and navigate to:
```
http://localhost:3000
```

You should see:
- **Dashboard** with market overview
- **Stats cards** showing total coins, opportunities
- **Phase distribution** chart
- **Top opportunities** table

## Manual Setup (Without Docker)

If you prefer to run without Docker:

### Backend Setup:

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install TA-Lib (required for technical analysis)
# On Ubuntu/Debian:
sudo apt-get install ta-lib
# On macOS:
brew install ta-lib

# Set up environment
export PYTHONPATH=$(pwd)

# Run database migrations
alembic upgrade head

# Start FastAPI server
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

### Start Celery Workers (in separate terminals):

```bash
# Terminal 2: Celery Worker
celery -A agents.orchestrator.celery_app worker --loglevel=info

# Terminal 3: Celery Beat (scheduler)
celery -A agents.orchestrator.celery_app beat --loglevel=info

# Terminal 4: Flower (monitoring)
celery -A agents.orchestrator.celery_app flower --port=5555
```

### Frontend Setup:

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## Troubleshooting

### Issue: "Cannot connect to database"

```bash
# Check PostgreSQL is running
docker-compose ps postgres

# Check logs
docker-compose logs postgres

# Restart database
docker-compose restart postgres
```

### Issue: "Redis connection failed"

```bash
# Check Redis is running
docker-compose ps redis

# Test Redis
docker-compose exec redis redis-cli ping
# Should return: PONG
```

### Issue: "Celery tasks not running"

```bash
# Check Celery worker status
docker-compose logs celery_worker

# Restart workers
docker-compose restart celery_worker celery_beat
```

### Issue: "No data showing in dashboard"

```bash
# Manually trigger data collection
curl -X POST http://localhost:8000/api/analyze/trigger

# Check task status in Flower
# Open: http://localhost:5555
```

## Testing Individual Components

### Test Data Collector:

```bash
docker-compose exec backend python -c "
import asyncio
from agents.data_collector.collector import DataCollectorAgent

async def test():
    async with DataCollectorAgent() as agent:
        data = await agent.collect_all_sources('bitcoin', 'BTC')
        print('Successfully collected data!')
        print(f'Sources: {list(data[\"sources\"].keys())}')

asyncio.run(test())
"
```

### Test Phase Detector:

```bash
docker-compose exec backend python agents/phase_detector/detector.py
```

### Test Scoring Engine:

```bash
docker-compose exec backend python scoring/engine.py
```

## Next Steps

1. **Configure Alerts**: Set up Telegram/Discord webhooks in `.env`
2. **Customize Weights**: Edit `scoring/engine.py` to adjust scoring weights
3. **Add More Coins**: Increase `TOP_COINS_COUNT` in `.env`
4. **Schedule Analysis**: Adjust frequencies in `agents/orchestrator/celery_app.py`

## Production Deployment

For production deployment:

1. **Update Environment**:
   ```bash
   ENVIRONMENT=production
   DEBUG=False
   ```

2. **Use Strong Secrets**:
   ```bash
   # Generate secure keys
   API_SECRET_KEY=$(openssl rand -hex 32)
   JWT_SECRET_KEY=$(openssl rand -hex 32)
   ```

3. **Set up HTTPS**: Use Nginx reverse proxy with SSL
4. **Enable Monitoring**: Configure Sentry, Prometheus, Grafana
5. **Backup Database**: Set up automated PostgreSQL backups

## Support & Resources

- **API Documentation**: http://localhost:8000/docs
- **GitHub Issues**: Report bugs and request features
- **Discord Community**: Join for support

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend (React)                      │
│              http://localhost:3000                       │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                  FastAPI Backend                         │
│              http://localhost:8000                       │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│         Celery Workers + Beat Scheduler                  │
│         (Autonomous Agent Orchestration)                 │
└──┬──────────┬──────────┬──────────┬──────────┬─────────┘
   │          │          │          │          │
   ▼          ▼          ▼          ▼          ▼
┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────────┐
│Data  │  │Phase │  │Fundam│  │OnCh. │  │Sentiment │
│Coll. │  │Detec │  │Analys│  │Analys│  │Analysis  │
└──────┘  └──────┘  └──────┘  └──────┘  └──────────┘
   │          │          │          │          │
   └──────────┴──────────┴──────────┴──────────┘
                      │
┌─────────────────────▼─────────────────────────────────┐
│      PostgreSQL + TimescaleDB + Redis + MongoDB        │
└───────────────────────────────────────────────────────┘
```

## Enjoy! 🎉

Your autonomous crypto research AI agent is now running!
Monitor the Flower dashboard to see the agents working automatically.
