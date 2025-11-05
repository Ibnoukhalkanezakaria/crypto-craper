import { Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Dashboard from './pages/Dashboard'
import Watchlist from './pages/Watchlist'
import CoinDetail from './pages/CoinDetail'
import Analytics from './pages/Analytics'
import UpcomingCoins from './pages/UpcomingCoins'

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/watchlist" element={<Watchlist />} />
        <Route path="/upcoming" element={<UpcomingCoins />} />
        <Route path="/coin/:symbol" element={<CoinDetail />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </Layout>
  )
}

export default App
