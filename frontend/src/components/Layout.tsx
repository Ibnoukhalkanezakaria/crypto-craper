import { Link, useLocation } from 'react-router-dom'
import { FiHome, FiStar, FiBarChart2, FiActivity, FiTrendingUp } from 'react-icons/fi'

interface LayoutProps {
  children: React.ReactNode
}

export default function Layout({ children }: LayoutProps) {
  const location = useLocation()

  const navItems = [
    { path: '/', label: 'Dashboard', icon: FiHome },
    { path: '/watchlist', label: 'Watchlist', icon: FiStar },
    { path: '/upcoming', label: 'Upcoming 2026', icon: FiTrendingUp },
    { path: '/analytics', label: 'Analytics', icon: FiBarChart2 },
  ]

  return (
    <div className="min-h-screen bg-crypto-darker">
      {/* Sidebar */}
      <aside className="fixed top-0 left-0 h-full w-64 bg-crypto-dark border-r border-gray-800 p-6">
        <div className="mb-8">
          <div className="flex items-center gap-2 mb-2">
            <FiActivity className="text-crypto-blue text-2xl" />
            <h1 className="text-xl font-bold text-white">Crypto AI Agent</h1>
          </div>
          <p className="text-gray-400 text-sm">Autonomous Research Platform</p>
        </div>

        <nav className="space-y-2">
          {navItems.map((item) => {
            const Icon = item.icon
            const isActive = location.pathname === item.path
            
            return (
              <Link
                key={item.path}
                to={item.path}
                className={`flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                  isActive
                    ? 'bg-crypto-blue text-white'
                    : 'text-gray-400 hover:bg-gray-800 hover:text-white'
                }`}
              >
                <Icon className="text-xl" />
                <span className="font-medium">{item.label}</span>
              </Link>
            )
          })}
        </nav>

        <div className="absolute bottom-6 left-6 right-6">
          <div className="card p-4">
            <div className="flex items-center gap-2 mb-2">
              <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
              <span className="text-sm text-gray-400">System Status</span>
            </div>
            <p className="text-xs text-gray-500">All agents operational</p>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="ml-64 p-8">
        {children}
      </main>
    </div>
  )
}
