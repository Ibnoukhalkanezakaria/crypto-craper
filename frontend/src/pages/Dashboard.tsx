import { useQuery } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import { apiService } from '../services/api'
import { FiStar, FiRefreshCw } from 'react-icons/fi'
import StatsCards from '../components/StatsCards'
import PhaseDistributionChart from '../components/PhaseDistributionChart'

export default function Dashboard() {
  const { data: coins, isLoading, refetch } = useQuery({
    queryKey: ['coins'],
    queryFn: () => apiService.getCoins({ limit: 100 }),
    refetchInterval: 60000, // Refetch every minute
  })

  const { data: stats } = useQuery({
    queryKey: ['stats'],
    queryFn: apiService.getOverviewStats,
    refetchInterval: 60000,
  })

  const getPhaseColor = (phase: string) => {
    const colors: Record<string, string> = {
      accumulation: 'text-green-400',
      expansion: 'text-blue-400',
      hype: 'text-yellow-400',
      crash: 'text-red-400',
      unknown: 'text-gray-400',
    }
    return colors[phase.toLowerCase()] || 'text-gray-400'
  }

  const getRecommendationBadge = (recommendation: string) => {
    const classes: Record<string, string> = {
      strong_buy: 'badge-green',
      buy: 'badge-blue',
      hold: 'badge-yellow',
      sell: 'badge-red',
      avoid: 'badge-red',
    }
    return classes[recommendation.toLowerCase()] || 'badge-yellow'
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-white mb-2">
            Market Overview
          </h1>
          <p className="text-gray-400">
            Real-time cryptocurrency analysis powered by AI
          </p>
        </div>
        <button
          onClick={() => refetch()}
          className="btn-primary flex items-center gap-2"
        >
          <FiRefreshCw />
          Refresh Data
        </button>
      </div>

      {/* Stats Cards */}
      {stats && <StatsCards stats={stats} />}

      {/* Phase Distribution Chart */}
      <PhaseDistributionChart />

      {/* Top Opportunities */}
      <div className="card">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold text-white">
            Top Opportunities
          </h2>
          <span className="text-gray-400 text-sm">
            Updated {new Date().toLocaleTimeString()}
          </span>
        </div>

        {isLoading ? (
          <div className="text-center py-12 text-gray-400">
            Loading coins...
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead>
                <tr className="border-b border-gray-700">
                  <th className="text-left py-3 px-4 text-gray-400 font-semibold">
                    Rank
                  </th>
                  <th className="text-left py-3 px-4 text-gray-400 font-semibold">
                    Coin
                  </th>
                  <th className="text-right py-3 px-4 text-gray-400 font-semibold">
                    Price
                  </th>
                  <th className="text-center py-3 px-4 text-gray-400 font-semibold">
                    Phase
                  </th>
                  <th className="text-right py-3 px-4 text-gray-400 font-semibold">
                    Score
                  </th>
                  <th className="text-center py-3 px-4 text-gray-400 font-semibold">
                    Recommendation
                  </th>
                  <th className="text-center py-3 px-4 text-gray-400 font-semibold">
                    Actions
                  </th>
                </tr>
              </thead>
              <tbody>
                {coins
                  ?.sort((a, b) => b.opportunity_score - a.opportunity_score)
                  .slice(0, 20)
                  .map((coin, index) => (
                    <tr
                      key={coin.symbol}
                      className="border-b border-gray-800 hover:bg-gray-800/50 transition-colors"
                    >
                      <td className="py-4 px-4 text-gray-400">
                        #{index + 1}
                      </td>
                      <td className="py-4 px-4">
                        <Link
                          to={`/coin/${coin.symbol}`}
                          className="flex items-center gap-3 hover:text-crypto-blue transition-colors"
                        >
                          <div>
                            <div className="font-semibold text-white">
                              {coin.symbol}
                            </div>
                            <div className="text-sm text-gray-400">
                              {coin.name}
                            </div>
                          </div>
                        </Link>
                      </td>
                      <td className="py-4 px-4 text-right text-white font-mono">
                        ${coin.current_price?.toLocaleString(undefined, {
                          minimumFractionDigits: 2,
                          maximumFractionDigits: 2,
                        })}
                      </td>
                      <td className="py-4 px-4 text-center">
                        <span className={`font-semibold capitalize ${getPhaseColor(coin.current_phase)}`}>
                          {coin.current_phase}
                        </span>
                        <div className="text-xs text-gray-500">
                          {(coin.phase_confidence * 100).toFixed(0)}%
                        </div>
                      </td>
                      <td className="py-4 px-4 text-right">
                        <div className="flex items-center justify-end gap-2">
                          <div className="text-2xl font-bold text-white">
                            {coin.opportunity_score.toFixed(0)}
                          </div>
                          <div className="text-sm text-gray-400">/100</div>
                        </div>
                        <div className="w-full bg-gray-700 rounded-full h-1.5 mt-2">
                          <div
                            className="bg-crypto-blue h-1.5 rounded-full"
                            style={{ width: `${coin.opportunity_score}%` }}
                          ></div>
                        </div>
                      </td>
                      <td className="py-4 px-4 text-center">
                        <span className={`${getRecommendationBadge(coin.recommendation)}`}>
                          {coin.recommendation.replace('_', ' ').toUpperCase()}
                        </span>
                      </td>
                      <td className="py-4 px-4 text-center">
                        <button
                          className="text-gray-400 hover:text-yellow-400 transition-colors"
                          title="Add to Watchlist"
                        >
                          <FiStar className={coin.in_watchlist ? 'fill-yellow-400 text-yellow-400' : ''} />
                        </button>
                      </td>
                    </tr>
                  ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  )
}
