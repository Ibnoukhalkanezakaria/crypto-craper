import { type Stats } from '../services/api'
import { FiDatabase, FiActivity, FiStar, FiTrendingUp } from 'react-icons/fi'

interface StatsCardsProps {
  stats: Stats
}

export default function StatsCards({ stats }: StatsCardsProps) {
  const cards = [
    {
      title: 'Total Coins',
      value: stats.total_coins,
      icon: FiDatabase,
      color: 'text-blue-400',
      bgColor: 'bg-blue-500/10',
    },
    {
      title: 'Active Analysis',
      value: stats.total_coins,
      icon: FiActivity,
      color: 'text-green-400',
      bgColor: 'bg-green-500/10',
    },
    {
      title: 'Top Opportunities',
      value: stats.top_opportunities,
      icon: FiTrendingUp,
      color: 'text-yellow-400',
      bgColor: 'bg-yellow-500/10',
    },
    {
      title: 'Watchlist',
      value: stats.watchlist_count,
      icon: FiStar,
      color: 'text-purple-400',
      bgColor: 'bg-purple-500/10',
    },
  ]

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {cards.map((card) => {
        const Icon = card.icon
        return (
          <div key={card.title} className="card">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-gray-400 text-sm mb-1">{card.title}</p>
                <h3 className="text-3xl font-bold text-white">{card.value}</h3>
              </div>
              <div className={`${card.bgColor} ${card.color} p-4 rounded-lg`}>
                <Icon className="text-2xl" />
              </div>
            </div>
          </div>
        )
      })}
    </div>
  )
}
