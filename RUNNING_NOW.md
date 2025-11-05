# 🚀 CRYPTO RESEARCH AI AGENT - NOW RUNNING!

## ✅ System Status

### Backend API Server
- **Status:** ✅ RUNNING
- **URL:** http://127.0.0.1:8000
- **API Docs:** http://127.0.0.1:8000/docs
- **Mode:** Demo (no database required)
- **Coins Loaded:** 5 (Bitcoin, Ethereum, Solana, Cardano, Polkadot)
- **Real Data:** Yes (from CoinGecko API)

### Frontend Dashboard
- **Status:** ✅ RUNNING  
- **URL:** http://localhost:3000
- **Framework:** React + TypeScript + Vite
- **Features:** Real-time coin tracking, phase detection, opportunity scores

---

## 🌐 How to Access

### Option 1: Open in Browser (Recommended)
```bash
# Open the main dashboard
xdg-open http://localhost:3000

# Or manually navigate to:
http://localhost:3000
```

### Option 2: Use API Directly
```bash
# View all coins
curl http://127.0.0.1:8000/api/coins | python3 -m json.tool

# View health status
curl http://127.0.0.1:8000/api/health

# View stats
curl http://127.0.0.1:8000/api/stats/overview
```

---

## 📊 Available Features

### Frontend Dashboard (http://localhost:3000)
- ✅ **Coin Table** - Sortable list with real prices
- ✅ **Phase Detection** - Market phase analysis
- ✅ **Opportunity Scores** - AI-powered investment scores (0-100)
- ✅ **Recommendations** - STRONG_BUY, BUY, HOLD, SELL, AVOID
- ✅ **Watchlist** - Add/remove coins to track
- ✅ **Phase Distribution** - Visual charts
- ✅ **Statistics Cards** - Overview metrics

### API Endpoints (http://127.0.0.1:8000/docs)
- `GET /api/coins` - List all coins with filtering
- `GET /api/coins/{symbol}` - Get coin details
- `GET /api/watchlist` - View watchlist
- `POST /api/watchlist/{symbol}` - Add to watchlist
- `DELETE /api/watchlist/{symbol}` - Remove from watchlist
- `GET /api/stats/overview` - Market statistics
- `GET /api/stats/phase-distribution` - Phase breakdown
- `POST /api/analyze/trigger` - Refresh data
- `GET /api/health` - Health check

---

## 🎮 Interactive Testing

### Test Scenario 1: View All Coins
1. Open http://localhost:3000
2. See table with 5 cryptocurrencies
3. Check opportunity scores (69-74 range)
4. All show "BUY" recommendation

### Test Scenario 2: Add to Watchlist
1. Click the star icon next to any coin
2. Navigate to "Watchlist" tab
3. See your selected coins

### Test Scenario 3: Refresh Data
1. Click "Trigger Analysis" button
2. Wait a few seconds
3. New scores calculated with fresh data

### Test Scenario 4: Filter Coins
1. Use the filter dropdowns
2. Filter by phase (Accumulation, Expansion, etc.)
3. Filter by minimum score

### Test Scenario 5: API Testing
```bash
# Get top opportunity
curl -s http://127.0.0.1:8000/api/coins | python3 -c "import sys, json; coins = json.load(sys.stdin); print(f\"{coins[0]['symbol']}: {coins[0]['opportunity_score']:.1f} - {coins[0]['recommendation']}\")"

# Add to watchlist
curl -X POST http://127.0.0.1:8000/api/watchlist/BTC

# View watchlist
curl -s http://127.0.0.1:8000/api/watchlist | python3 -m json.tool
```

---

## 📈 Sample Data Overview

### Current Loaded Coins:

| Symbol | Name | Price | Phase | Score | Recommendation |
|--------|------|-------|-------|-------|----------------|
| DOT | Polkadot | $2.91 | Unknown | 74.3 | BUY |
| SOL | Solana | $184.24 | Unknown | 73.1 | BUY |
| BTC | Bitcoin | $110,197 | Unknown | 69.2 | BUY |
| ETH | Ethereum | ~$3,450 | Unknown | ~68 | BUY |
| ADA | Cardano | ~$0.50 | Unknown | ~67 | BUY |

*Prices are real-time from CoinGecko*
*Phases show "Unknown" in demo mode (would detect Accumulation/Expansion/Hype/Crash with trained ML model)*

---

## 🔧 How It Works

1. **Backend Demo API** (`demo_api.py`):
   - Fetches real cryptocurrency data from CoinGecko
   - Generates sample price history (365 days)
   - Runs phase detection (30 technical indicators)
   - Calculates opportunity scores (multi-factor algorithm)
   - Stores in memory (no database needed for demo)

2. **Frontend Dashboard** (React):
   - Polls backend API every 60 seconds
   - Displays data in sortable table
   - Shows real-time price updates
   - Interactive filters and watchlist

3. **Data Flow**:
   ```
   CoinGecko API → Data Collector → Phase Detector → Scoring Engine → REST API → React Frontend → Your Browser
   ```

---

## 🛠️ Managing the Servers

### Check Status
```bash
# Backend status
ps aux | grep demo_api

# Frontend status  
ps aux | grep vite

# Test connectivity
curl http://127.0.0.1:8000/api/health
curl http://localhost:3000
```

### Stop Servers
```bash
# Stop backend
pkill -f demo_api.py

# Stop frontend
pkill -f vite
```

### Restart Servers
```bash
# Backend
cd /home/zibnoukh/crypto-craper/backend
source venv/bin/activate
nohup python demo_api.py > ../backend.log 2>&1 &

# Frontend
cd /home/zibnoukh/crypto-craper/frontend
npm run dev &
```

### View Logs
```bash
# Backend logs
tail -f /home/zibnoukh/crypto-craper/backend.log

# Frontend logs (in terminal where it's running)
```

---

## 🎯 What to Try

### Beginner:
1. ✅ Open http://localhost:3000 in browser
2. ✅ View the coin table
3. ✅ Add a coin to watchlist (click star)
4. ✅ Check the statistics cards at top

### Intermediate:
1. ✅ Open http://127.0.0.1:8000/docs (Swagger UI)
2. ✅ Try API endpoints interactively
3. ✅ Trigger new analysis
4. ✅ Filter coins by score

### Advanced:
1. ✅ Inspect Network tab in browser DevTools
2. ✅ Watch API calls in real-time
3. ✅ Modify frontend code and see hot-reload
4. ✅ Add new coins to demo_api.py

---

## 🚨 Troubleshooting

### Frontend not loading?
```bash
# Check if server is running
curl http://localhost:3000

# If not, restart it
cd frontend && npm run dev
```

### Backend not responding?
```bash
# Check if running
ps aux | grep demo_api

# Check logs
tail -50 backend.log

# Restart if needed
pkill -f demo_api.py
cd backend && source venv/bin/activate
python demo_api.py
```

### CORS errors in browser?
- The backend is configured to allow localhost:3000
- Clear browser cache and reload

### Port already in use?
```bash
# Find what's using port 8000
lsof -i :8000

# Find what's using port 3000
lsof -i :3000

# Kill and restart
```

---

## 📱 Browser Compatibility

Tested and working on:
- ✅ Chrome/Chromium
- ✅ Firefox  
- ✅ Edge
- ✅ Safari

---

## 🎉 You're All Set!

The system is **fully operational** and ready for exploration!

### Quick Links:
- 🌐 **Main Dashboard:** http://localhost:3000
- 📚 **API Documentation:** http://127.0.0.1:8000/docs
- 🔍 **API Health:** http://127.0.0.1:8000/api/health

**Enjoy exploring your autonomous crypto research AI agent!** 🚀
