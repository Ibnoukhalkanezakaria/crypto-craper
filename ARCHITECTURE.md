# 🏗️ System Architecture & Design

## Overview

This document describes the complete architecture of the Autonomous Crypto Research AI Agent system.

## System Components

### 1. Data Collection Layer

**Multi-Source Data Aggregation**

```python
agents/data_collector/
├── collector.py          # Main data collection orchestrator
├── sources/
│   ├── coingecko.py     # CoinGecko API integration
│   ├── coinmarketcap.py # CoinMarketCap integration
│   ├── messari.py       # Messari research data
│   ├── defillama.py     # DeFi protocol metrics
│   └── token_unlocks.py # Token vesting schedules
```

**Features:**
- Asynchronous concurrent data fetching
- Rate limiting and backoff strategies
- Automatic retry on failure
- Data validation and sanitization
- Caching layer for frequently accessed data

**Data Sources:**
1. **CoinGecko** - Price, volume, community metrics
2. **CoinMarketCap** - Market rankings, tokenomics
3. **Messari** - Deep research reports
4. **DeFiLlama** - TVL, protocol revenue
5. **TokenUnlocks** - Vesting schedules
6. **GitHub** - Development activity
7. **Social Media** - Twitter, Reddit, Discord

### 2. Market Phase Detection

**Machine Learning Pipeline**

```python
agents/phase_detector/
├── detector.py          # Phase detection ML model
├── features.py          # Feature engineering
├── training.py          # Model training pipeline
└── models/
    ├── phase_rf.pkl     # Random Forest model
    └── scaler.pkl       # Feature scaler
```

**Phases Detected:**
1. **ACCUMULATION** 🟢
   - Low volatility
   - Decreasing volume
   - Sideways price action
   - 50-70% down from ATH
   - *Recommendation: BUY*

2. **EXPANSION** 🔵
   - Steady uptrend
   - Increasing volume
   - Price above MA50/MA200
   - Strong fundamentals
   - *Recommendation: BUY/HOLD*

3. **HYPE** 🟡
   - Parabolic price move
   - Extreme volume spikes
   - RSI > 70
   - Social media frenzy
   - *Recommendation: AVOID/SELL*

4. **CRASH** 🔴
   - Sharp decline
   - Panic selling
   - High volatility
   - Capitulation
   - *Recommendation: WAIT*

**Technical Indicators Used:**
- RSI (Relative Strength Index)
- Moving Averages (20, 50, 200)
- Bollinger Bands
- Volume Analysis
- ADX (Trend Strength)
- MACD
- Rate of Change

### 3. Fundamental Analysis Engine

**Comprehensive Project Evaluation**

```python
agents/fundamental/
├── analyzer.py          # Main analysis orchestrator
├── team_analyzer.py     # Team & credibility assessment
├── tech_analyzer.py     # Technology evaluation
├── tokenomics.py        # Economic model analysis
└── community.py         # Community strength metrics
```

**Analysis Components:**

**A. Team Analysis (25% weight)**
- LinkedIn profiles verification
- GitHub contribution history
- Previous projects and track record
- Team size and expertise
- Advisors and partnerships

**B. Technology Assessment (20% weight)**
- Innovation and uniqueness
- Blockchain platform
- Consensus mechanism
- Smart contract audits
- Whitepaper quality
- GitHub activity (commits, stars, forks)

**C. Tokenomics (25% weight)**
- Supply metrics (circulating, total, max)
- Inflation rate
- Token distribution
- Vesting schedules
- Unlock dates
- Token utility and demand drivers

**D. Community Strength (15% weight)**
- Twitter followers and engagement
- Telegram/Discord members
- Reddit subscribers
- GitHub stars and watchers
- Community sentiment

**E. Ecosystem & Partnerships (15% weight)**
- Strategic partnerships
- Integrations
- Use cases
- Adoption metrics

### 4. On-Chain Analytics

**Blockchain Data Analysis**

```python
agents/onchain/
├── analytics.py         # Main on-chain agent
├── glassnode.py        # Glassnode integration
├── santiment.py        # Santiment metrics
├── cryptoquant.py      # CryptoQuant data
└── whale_tracker.py    # Whale activity detection
```

**Metrics Tracked:**

**A. Wallet Metrics**
- Active addresses (daily, weekly)
- New addresses
- Zero-balance addresses
- Whale addresses (>1% supply)

**B. Exchange Flows**
- Exchange inflow (bearish)
- Exchange outflow (bullish)
- Net flow
- Exchange balance
- Supply on exchanges %

**C. Transaction Analysis**
- Transaction count
- Transaction volume
- Average transaction size
- Large transactions (>$100k)

**D. Holder Behavior**
- Holder distribution
- Top 10 holders %
- Gini coefficient
- Long-term vs short-term holders

**E. Network Health**
- Hash rate (for PoW)
- Staking participation (for PoS)
- Validator count
- Network fees

**F. Advanced Metrics**
- MVRV Ratio (Market Value to Realized Value)
- SOPR (Spent Output Profit Ratio)
- Net Unrealized Profit/Loss
- Supply in profit %

### 5. Sentiment Analysis

**Social Media & News Monitoring**

```python
agents/sentiment/
├── analyzer.py          # Sentiment orchestrator
├── twitter_monitor.py   # Twitter analysis
├── reddit_monitor.py    # Reddit scraping
├── news_scraper.py      # News aggregation
└── nlp_model.py        # NLP sentiment model
```

**Data Sources:**
- Twitter mentions and sentiment
- Reddit discussions (r/cryptocurrency, specific coin subs)
- Discord activity
- News articles
- Influencer mentions (LunarCrush)

**Analysis Methods:**
- BERT-based sentiment classification
- Sentiment polarity (-1 to +1)
- Social volume trending
- Influencer impact analysis
- Fear & Greed index integration

### 6. Composite Scoring Engine

**Multi-Factor Opportunity Assessment**

```python
scoring/
├── engine.py            # Scoring algorithm
├── weights.py           # Configurable weights
└── recommender.py       # Investment recommendations
```

**Scoring Formula:**

```
Opportunity Score = (
    Fundamental_Score × 0.30 +
    Technical_Score   × 0.25 +
    OnChain_Score     × 0.25 +
    Sentiment_Score   × 0.20
) × Phase_Multiplier
```

**Phase Multipliers:**
- Accumulation: 1.3x (boost)
- Expansion: 1.2x (boost)
- Hype: 0.6x (penalty)
- Crash: 0.7x (penalty)
- Unknown: 1.0x (neutral)

**Score Interpretation:**
- **80-100**: Strong Buy (Top opportunities)
- **65-79**: Buy (Good opportunities)
- **40-64**: Hold (Monitor)
- **25-39**: Sell (Exit positions)
- **0-24**: Avoid (Stay away)

### 7. Orchestration & Scheduling

**Automated Task Management**

```python
agents/orchestrator/
├── celery_app.py        # Celery configuration
├── tasks.py             # Scheduled tasks
└── schedules.py         # Cron schedules
```

**Scheduled Tasks:**

| Task | Frequency | Description |
|------|-----------|-------------|
| Data Collection | Hourly | Collect market data from all sources |
| Phase Detection | Every 6 hours | Update market phase classifications |
| On-Chain Update | Every 4 hours | Fetch latest on-chain metrics |
| Sentiment Update | Every 2 hours | Analyze social sentiment |
| Score Calculation | Every 30 min | Recalculate opportunity scores |
| Alert Dispatch | Every 10 min | Send pending alerts |
| Model Retraining | Weekly | Retrain ML models with new data |

### 8. Alert & Notification System

**Multi-Channel Alerts**

```python
alerts/
├── notifier.py          # Alert dispatcher
├── telegram.py          # Telegram bot
├── discord.py           # Discord webhook
└── email.py            # Email notifications
```

**Alert Types:**

1. **Phase Transition Alerts**
   - Accumulation → Expansion (BUY signal)
   - Expansion → Hype (CAUTION)
   - Hype → Crash (SELL signal)

2. **High Opportunity Alerts**
   - Score crosses 75+ threshold
   - Accumulation phase + High score
   - Whale accumulation detected

3. **Whale Activity Alerts**
   - Large transactions (>$1M)
   - Significant exchange outflows
   - Unusual holder concentration changes

4. **Risk Alerts**
   - Upcoming large token unlocks
   - Development activity decline
   - Negative sentiment spikes

### 9. API Layer

**RESTful API Endpoints**

```python
api/
├── main.py              # FastAPI application
├── routes/
│   ├── coins.py         # Coin endpoints
│   ├── watchlist.py     # Watchlist management
│   ├── analytics.py     # Analytics endpoints
│   └── alerts.py        # Alert management
├── schemas.py           # Pydantic models
└── dependencies.py      # Shared dependencies
```

**Key Endpoints:**

```
GET  /api/coins                    # List all analyzed coins
GET  /api/coins/{symbol}           # Detailed coin analysis
GET  /api/watchlist                # User's watchlist
POST /api/watchlist/{symbol}       # Add to watchlist
GET  /api/phases/{symbol}          # Phase history
GET  /api/stats/overview           # System statistics
GET  /api/stats/phase-distribution # Phase distribution
POST /api/analyze/trigger          # Manual analysis trigger
GET  /api/alerts                   # Recent alerts
```

### 10. Frontend Dashboard

**React-based Interactive UI**

```
frontend/src/
├── components/
│   ├── Layout.tsx                 # Main layout
│   ├── StatsCards.tsx             # Statistics cards
│   ├── PhaseDistributionChart.tsx # Phase chart
│   ├── CoinTable.tsx              # Coin listing
│   └── WatchlistManager.tsx       # Watchlist component
├── pages/
│   ├── Dashboard.tsx              # Main dashboard
│   ├── Watchlist.tsx              # Watchlist page
│   ├── CoinDetail.tsx             # Coin details
│   └── Analytics.tsx              # Analytics page
└── services/
    └── api.ts                     # API client
```

**Features:**
- Real-time data updates
- Interactive charts (Chart.js, Recharts)
- Coin filtering and sorting
- Watchlist management
- Phase visualization
- Score breakdown
- Alert notifications

### 11. Database Schema

**PostgreSQL + TimescaleDB**

```sql
-- Core tables
coins                    # Coin master data
price_history           # Time-series price data (hypertable)
onchain_metrics         # Time-series on-chain data (hypertable)
sentiment_data          # Time-series sentiment (hypertable)
fundamental_data        # Fundamental analysis
alerts                  # Alert records
ml_models               # Model versioning
system_logs            # System logging

-- Indexes
idx_coin_score         # Opportunity score
idx_coin_phase         # Market phase
idx_price_coin_ts      # Price history queries
```

## Data Flow

```
1. Data Collection (Hourly)
   ↓
2. Store Raw Data (PostgreSQL/MongoDB)
   ↓
3. Feature Engineering
   ↓
4. Phase Detection (ML Model)
   ↓
5. Fundamental Analysis
   ↓
6. On-Chain Analysis
   ↓
7. Sentiment Analysis
   ↓
8. Composite Scoring
   ↓
9. Alert Generation
   ↓
10. Notification Dispatch
    ↓
11. Frontend Update
```

## Scalability Considerations

1. **Horizontal Scaling**: Add more Celery workers
2. **Database Partitioning**: TimescaleDB automatic partitioning
3. **Caching**: Redis for frequent queries
4. **Load Balancing**: Nginx for API requests
5. **Async Processing**: All I/O operations are async
6. **Rate Limiting**: Respect API rate limits
7. **Queue Management**: Celery for distributed tasks

## Security

1. **API Key Management**: Environment variables only
2. **Database Credentials**: Encrypted and rotated
3. **CORS Protection**: Configured origins
4. **JWT Authentication**: For user endpoints (future)
5. **Input Validation**: Pydantic schemas
6. **SQL Injection Prevention**: SQLAlchemy ORM
7. **XSS Protection**: React auto-escaping

## Monitoring & Observability

1. **Flower**: Celery task monitoring
2. **Prometheus**: Metrics collection
3. **Grafana**: Visualization dashboards
4. **Sentry**: Error tracking
5. **Application Logs**: Structured JSON logging
6. **Database Metrics**: Query performance

## Future Enhancements

1. **Machine Learning Improvements**
   - Deep learning models (LSTM for price prediction)
   - Reinforcement learning for portfolio optimization
   - Ensemble methods for better accuracy

2. **Additional Data Sources**
   - On-chain DEX data
   - NFT metrics
   - Governance participation
   - Protocol-specific metrics

3. **Advanced Features**
   - Portfolio tracking
   - Automated backtesting
   - Strategy recommendations
   - Risk management tools
   - Price alerts
   - DCA calculator

4. **User Features**
   - User accounts and authentication
   - Custom watchlists
   - Personalized alerts
   - Portfolio management
   - Historical performance tracking

5. **Mobile App**
   - React Native mobile application
   - Push notifications
   - Biometric authentication

## Conclusion

This architecture provides a robust, scalable foundation for autonomous cryptocurrency research and analysis. The modular design allows for easy extension and customization while maintaining high performance and reliability.
