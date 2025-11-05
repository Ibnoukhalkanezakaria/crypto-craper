#!/bin/bash

# Crypto Research AI Agent - Quick Status Check

echo "======================================"
echo "🚀 CRYPTO RESEARCH AI AGENT - STATUS"
echo "======================================"
echo ""

# Check Backend
echo "🔧 Backend API Server:"
if ps aux | grep -v grep | grep demo_api.py > /dev/null; then
    echo "   ✅ RUNNING on http://127.0.0.1:8000"
    
    # Test health endpoint
    if curl -s http://127.0.0.1:8000/api/health > /dev/null 2>&1; then
        COINS=$(curl -s http://127.0.0.1:8000/api/health | python3 -c "import sys, json; data = json.load(sys.stdin); print(data['coins_loaded'])" 2>/dev/null)
        echo "   📊 Coins loaded: $COINS"
    fi
else
    echo "   ❌ NOT RUNNING"
    echo "   To start: cd backend && source venv/bin/activate && python demo_api.py"
fi

echo ""

# Check Frontend
echo "🌐 Frontend Dashboard:"
if ps aux | grep -v grep | grep vite > /dev/null; then
    echo "   ✅ RUNNING on http://localhost:3000"
else
    echo "   ❌ NOT RUNNING"
    echo "   To start: cd frontend && npm run dev"
fi

echo ""
echo "======================================"
echo "📌 QUICK ACCESS LINKS"
echo "======================================"
echo ""
echo "Main Dashboard:     http://localhost:3000"
echo "API Documentation:  http://127.0.0.1:8000/docs"  
echo "API Health Check:   http://127.0.0.1:8000/api/health"
echo ""

# Test API if running
if curl -s http://127.0.0.1:8000/api/coins > /dev/null 2>&1; then
    echo "======================================"
    echo "💎 TOP 3 OPPORTUNITIES"
    echo "======================================"
    curl -s http://127.0.0.1:8000/api/coins | python3 << 'PYEOF'
import json
import sys

coins = json.load(sys.stdin)
for i, coin in enumerate(coins[:3], 1):
    print(f"{i}. {coin['symbol']:6} - {coin['name']:15} | Score: {coin['opportunity_score']:5.1f} | {coin['recommendation'].upper():10} | ${coin['current_price']:,.2f}")
PYEOF
    echo ""
fi

echo "======================================"
echo "🎮 QUICK COMMANDS"
echo "======================================"
echo ""
echo "Refresh data:    curl -X POST http://127.0.0.1:8000/api/analyze/trigger"
echo "View all coins:  curl http://127.0.0.1:8000/api/coins | python3 -m json.tool"
echo "View stats:      curl http://127.0.0.1:8000/api/stats/overview"
echo "Add to watchlist: curl -X POST http://127.0.0.1:8000/api/watchlist/BTC"
echo ""
echo "======================================"
