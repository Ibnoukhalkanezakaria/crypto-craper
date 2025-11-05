import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export interface Coin {
  id?: number
  symbol: string
  name: string
  current_price: number
  market_cap?: number
  volume_24h?: number
  price_change_24h?: number
  current_phase: string
  phase_confidence: number
  opportunity_score: number
  fundamental_score?: number
  technical_score?: number
  onchain_score?: number
  sentiment_score?: number
  recommendation: string
  in_watchlist?: boolean
  rank?: number
  updated_at?: string
}

export interface CoinDetail extends Coin {
  fundamental: any
  onchain_history: any[]
  sentiment_history: any[]
}

export interface Stats {
  total_coins: number
  phase_distribution: Record<string, number>
  top_opportunities: number
  watchlist_count: number
}

export const apiService = {
  // Coins
  getCoins: async (params?: any): Promise<Coin[]> => {
    const response = await api.get('/api/coins', { params })
    return response.data
  },

  getCoinDetail: async (symbol: string): Promise<CoinDetail> => {
    const response = await api.get(`/api/coins/${symbol}`)
    return response.data
  },

  // Watchlist
  getWatchlist: async (): Promise<Coin[]> => {
    const response = await api.get('/api/watchlist')
    return response.data
  },

  addToWatchlist: async (symbol: string): Promise<void> => {
    await api.post(`/api/watchlist/${symbol}`)
  },

  removeFromWatchlist: async (symbol: string): Promise<void> => {
    await api.delete(`/api/watchlist/${symbol}`)
  },

  // Stats
  getOverviewStats: async (): Promise<Stats> => {
    const response = await api.get('/api/stats/overview')
    return response.data
  },

  getPhaseDistribution: async (): Promise<any[]> => {
    const response = await api.get('/api/stats/phase-distribution')
    return response.data
  },

  // Alerts
  getAlerts: async (unsentOnly = false): Promise<any[]> => {
    const response = await api.get('/api/alerts', {
      params: { unsent_only: unsentOnly }
    })
    return response.data
  },

  // Trigger analysis
  triggerAnalysis: async (): Promise<any> => {
    const response = await api.post('/api/analyze/trigger')
    return response.data
  },
}

export default api
