import { useState } from 'react'
import { FiTrendingUp, FiExternalLink, FiCalendar, FiDollarSign, FiStar, FiInfo, FiCheckCircle, FiUsers, FiTarget, FiCpu, FiFilter } from 'react-icons/fi'

interface UpcomingCoin {
  symbol: string
  name: string
  launchDate: string
  presalePrice: string
  estimatedListing: string
  useCase: string
  technology: string
  recommendation: string
  stage: string
  fundingRaised: string
  backers: string[]
  whyRecommended: string[]
  potential: string
  category: string
  blockchain: string
  website?: string
}

export default function UpcomingCoins() {
  const [selectedCategory, setSelectedCategory] = useState<string>('All')

  // Comprehensive list of upcoming 2026 cryptocurrency launches based on research from multiple platforms
  const upcomingCoins: UpcomingCoin[] = [
    {
      symbol: 'MEGA',
      name: 'MegaETH',
      launchDate: 'Q1 2026',
      presalePrice: '$0.50 - $1.20',
      estimatedListing: '$3.50 - $5.00',
      useCase: 'Real-time blockchain with unprecedented transaction speeds for DeFi and gaming',
      technology: 'Ultra-high-performance Layer-2 scaling solution',
      recommendation: 'Strong Buy',
      stage: 'Public Sale Completed - Token Launch Q1 2026',
      fundingRaised: '$107.68M',
      backers: ['Vitalik Buterin', 'Cobie', 'Dragonfly Capital', 'Paradigm', 'Balaji Srinivasan'],
      whyRecommended: [
        'Backed by Ethereum co-founder Vitalik Buterin',
        'Massive $107M+ funding from top-tier VCs',
        'Revolutionary real-time blockchain technology',
        'Solves major scalability issues in crypto',
        'Strong community and developer support'
      ],
      potential: '+350% - 600%',
      category: 'Layer-2',
      blockchain: 'Ethereum',
      website: 'https://megaeth.io'
    },
    {
      symbol: 'MRGN',
      name: 'Marginfi',
      launchDate: 'Q1 2026',
      presalePrice: 'Points-based (No public presale)',
      estimatedListing: '$1.50 - $3.00',
      useCase: 'Decentralized lending and borrowing protocol on Solana',
      technology: 'Advanced DeFi lending platform with unique risk management',
      recommendation: 'Strong Buy',
      stage: 'Points Farming Active - Token Launch Q1 2026',
      fundingRaised: '$3M',
      backers: ['Multicoin Capital', 'Pantera Capital', 'Ryze Labs', 'Solana Ventures'],
      whyRecommended: [
        'Leading Solana DeFi protocol with massive TVL',
        'Backed by top crypto VCs',
        'Active points farming program rewards early users',
        'Strong product-market fit demonstrated',
        'Growing Solana ecosystem momentum'
      ],
      potential: '+200% - 400%',
      category: 'DeFi',
      blockchain: 'Solana'
    },
    {
      symbol: 'EBT',
      name: 'EarnBIT',
      launchDate: 'Q1 2026',
      presalePrice: '$0.05 - $0.15',
      estimatedListing: '$0.30 - $0.50',
      useCase: 'Centralized exchange token with staking rewards and fee discounts',
      technology: 'Exchange utility token with deflationary mechanics',
      recommendation: 'Buy',
      stage: 'Private Sale - Token Launch Q1 2026',
      fundingRaised: 'Undisclosed',
      backers: ['Private Investors', 'Exchange Partners'],
      whyRecommended: [
        'Exchange tokens historically perform well',
        'Multiple utility use cases',
        'Deflationary tokenomics',
        'Early stage entry opportunity',
        'Growing exchange user base'
      ],
      potential: '+150% - 300%',
      category: 'CEX',
      blockchain: 'Ethereum'
    },
    {
      symbol: 'ARIAIP',
      name: 'Aria Protocol',
      launchDate: 'Q1-Q2 2026',
      presalePrice: '$0.08 - $0.12',
      estimatedListing: '$0.25 - $0.40',
      useCase: 'Decentralized IP rights management and tokenization platform',
      technology: 'Blockchain-based intellectual property protocol',
      recommendation: 'Strong Buy',
      stage: 'IDO Completed - Token Launch Upcoming',
      fundingRaised: '$15.5M',
      backers: ['Polychain Capital', 'OKX Ventures', 'Selini Capital', 'Blockchain Capital'],
      whyRecommended: [
        '$15.5M raised from top-tier VCs',
        'Solving real-world IP management problems',
        'Large addressable market',
        'Strong technical team',
        'Growing demand for digital IP solutions'
      ],
      potential: '+200% - 350%',
      category: 'DeFi',
      blockchain: 'Ethereum'
    },
    {
      symbol: 'TRIA',
      name: 'Tria',
      launchDate: 'Q1-Q2 2026',
      presalePrice: 'Community Round Ongoing',
      estimatedListing: '$0.80 - $1.50',
      useCase: 'Infrastructure layer for seamless Web3 user experience',
      technology: 'Account abstraction and wallet infrastructure',
      recommendation: 'Strong Buy',
      stage: 'Community Round Active - 5 days left',
      fundingRaised: '$12M',
      backers: ['P2 Ventures', 'Sandeep Nailwal (Polygon)', 'Aptos Foundation', 'Coinbase Ventures'],
      whyRecommended: [
        'Co-founder of Polygon as investor',
        'Critical infrastructure for Web3 adoption',
        'Strong partnerships with major chains',
        '$12M from strategic investors',
        'Solving major UX barriers in crypto'
      ],
      potential: '+250% - 450%',
      category: 'Infrastructure',
      blockchain: 'Multi-chain'
    },
    {
      symbol: 'rTTOK',
      name: 'ByteDance rTTOK',
      launchDate: 'Q1-Q2 2026',
      presalePrice: '$0.50 - $1.00 (via RepublicX)',
      estimatedListing: '$2.00 - $4.00',
      useCase: 'Tokenized exposure to ByteDance (TikTok parent company) creators',
      technology: 'Tokenized stock on blockchain',
      recommendation: 'Buy',
      stage: 'Public Sale Active on CoinList - Ends Nov 13',
      fundingRaised: 'N/A (Tokenized Stock)',
      backers: ['RepublicX', 'CoinList Platform'],
      whyRecommended: [
        'Exposure to TikTok parent company',
        'Unique tokenized stock model',
        'Massive creator economy market',
        'Available on major platforms',
        'Institutional-grade offering'
      ],
      potential: '+100% - 250%',
      category: 'Tokenized Assets',
      blockchain: 'Ethereum'
    },
    {
      symbol: 'TRUST',
      name: 'Intuition',
      launchDate: 'Q2 2026',
      presalePrice: 'Token Sale Closed',
      estimatedListing: '$1.00 - $2.00',
      useCase: 'Decentralized knowledge graph and reputation system',
      technology: 'On-chain identity and attestation protocol',
      recommendation: 'Strong Buy',
      stage: 'Binance Alpha Airdrop - Token Launch Q2 2026',
      fundingRaised: '$5.6M',
      backers: ['ConsenSys', 'The LAO', 'Andrew Keys', '24+ other investors'],
      whyRecommended: [
        'Backed by ConsenSys and major Web3 players',
        'Binance Alpha listing confirmed',
        'Solving critical trust and identity issues',
        'Strong developer ecosystem',
        'Early airdrop opportunity'
      ],
      potential: '+300% - 500%',
      category: 'Infrastructure',
      blockchain: 'Ethereum'
    },
    {
      symbol: 'FOLKS',
      name: 'Folks Finance',
      launchDate: 'Q2 2026',
      presalePrice: 'N/A (Launch directly)',
      estimatedListing: '$0.50 - $1.20',
      useCase: 'Cross-chain DeFi lending and borrowing protocol',
      technology: 'Multi-chain DeFi platform with innovative capital efficiency',
      recommendation: 'Buy',
      stage: 'Token Launch Imminent',
      fundingRaised: '$6.2M',
      backers: ['Jump Crypto', 'Coinbase Ventures', 'OKX Ventures', '15+ major VCs'],
      whyRecommended: [
        'Backed by Jump Crypto and Coinbase',
        'Operating DeFi protocol with real users',
        'Cross-chain capability is high demand',
        'Strong fundamentals and TVL growth',
        'Multi-chain strategy future-proof'
      ],
      potential: '+180% - 350%',
      category: 'DeFi',
      blockchain: 'Multi-chain'
    },
    {
      symbol: 'PRV',
      name: 'Providence',
      launchDate: 'Q2-Q3 2026',
      presalePrice: 'TBA',
      estimatedListing: '$1.50 - $3.00',
      useCase: 'Web3 gaming platform with AAA game development',
      technology: 'Blockchain gaming infrastructure and game studios',
      recommendation: 'Buy',
      stage: 'Development - Token Launch Upcoming',
      fundingRaised: 'Undisclosed',
      backers: ['Framework Ventures', 'BitScale Capital', 'CoinFund', 'Delphi Digital'],
      whyRecommended: [
        'Top gaming VCs as backers',
        'AAA game quality focus',
        'Large and growing Web3 gaming market',
        'Experienced game development team',
        'Strong community building pre-launch'
      ],
      potential: '+200% - 400%',
      category: 'Gaming',
      blockchain: 'Custom L2'
    },
    {
      symbol: 'ULTI',
      name: 'Ultiverse',
      launchDate: 'Q2-Q3 2026',
      presalePrice: 'NFT Staking Active',
      estimatedListing: '$0.40 - $0.80',
      useCase: 'Metaverse gaming platform with AI-powered NPCs',
      technology: 'VR/AR metaverse with AI integration',
      recommendation: 'Strong Buy',
      stage: 'NFT Staking Active since Dec 2022',
      fundingRaised: '$13.5M',
      backers: ['Binance Labs', 'DWF Labs', 'DeFiance Capital', '10+ major investors'],
      whyRecommended: [
        'Binance Labs backed project',
        'Innovative AI + Metaverse combination',
        'Long development and community building',
        'Large funding for quality development',
        'Growing metaverse narrative'
      ],
      potential: '+250% - 500%',
      category: 'Gaming/AI',
      blockchain: 'BNB Chain'
    },
    {
      symbol: 'COGNI',
      name: 'Cogni AI Agents',
      launchDate: 'Q4 2026',
      presalePrice: '$0.03 - $0.08',
      estimatedListing: '$0.15 - $0.30',
      useCase: 'Autonomous AI agents for crypto trading and analysis',
      technology: 'Machine learning powered trading bots and analytics',
      recommendation: 'Buy',
      stage: 'ICO Presale Active until Q4 2025',
      fundingRaised: '$219.6K (ongoing)',
      backers: ['Private Angel Investors', 'AI/Crypto Funds'],
      whyRecommended: [
        'AI agents narrative is exploding',
        'Practical use case for crypto traders',
        'Low market cap entry opportunity',
        'Early stage with high potential',
        'Growing demand for AI tools in crypto'
      ],
      potential: '+400% - 800%',
      category: 'AI',
      blockchain: 'Ethereum'
    },
    {
      symbol: 'AGORA',
      name: 'AgoraLend',
      launchDate: 'Q4 2026',
      presalePrice: '$0.05 - $0.12',
      estimatedListing: '$0.25 - $0.45',
      useCase: 'Decentralized lending protocol with unique collateral options',
      technology: 'Advanced DeFi lending with RWA integration',
      recommendation: 'Buy',
      stage: 'ICO Presale Active until Q4 2025',
      fundingRaised: '$353.5K (ongoing)',
      backers: ['DeFi-focused VCs', 'Angel Investors'],
      whyRecommended: [
        'Real-world asset integration trend',
        'DeFi lending market is massive',
        'Innovative collateral mechanisms',
        'Early entry at low valuation',
        'Growing RWA narrative in 2026'
      ],
      potential: '+300% - 600%',
      category: 'DeFi',
      blockchain: 'Ethereum'
    }
  ]

  const categories = ['All', 'Layer-2', 'DeFi', 'Infrastructure', 'Gaming', 'AI', 'CEX', 'Tokenized Assets']

  const filteredCoins = selectedCategory === 'All' 
    ? upcomingCoins 
    : upcomingCoins.filter(coin => coin.category === selectedCategory)

  const getRecommendationColor = (recommendation: string) => {
    const colors: Record<string, string> = {
      'Strong Buy': 'text-green-400 bg-green-400/10 border-green-400/30',
      'Buy': 'text-blue-400 bg-blue-400/10 border-blue-400/30',
      'Hold': 'text-yellow-400 bg-yellow-400/10 border-yellow-400/30'
    }
    return colors[recommendation] || 'text-gray-400 bg-gray-400/10 border-gray-400/30'
  }

  const getStageColor = (stage: string) => {
    if (stage.includes('Active') || stage.includes('Ongoing')) return 'text-green-400 bg-green-400/10'
    if (stage.includes('Completed') || stage.includes('Closed')) return 'text-yellow-400 bg-yellow-400/10'
    return 'text-blue-400 bg-blue-400/10'
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex justify-between items-start">
        <div>
          <h1 className="text-3xl font-bold text-white mb-2 flex items-center gap-3">
            <FiTrendingUp className="text-crypto-blue" />
            Upcoming Coins 2026
          </h1>
          <p className="text-gray-400 max-w-3xl">
            Comprehensive list of upcoming cryptocurrency launches scheduled for 2026, based on data from 
            <span className="text-crypto-blue"> CoinMarketCap, Messari, CoinGecko, ICO Drops, and CoinList</span>. 
            These projects are highly recommended based on strong fundamentals, technology, partnerships, and community potential.
          </p>
        </div>
      </div>

      {/* Summary Analysis Card */}
      <div className="card p-6 bg-gradient-to-br from-crypto-blue/10 to-purple-500/10 border-crypto-blue/30">
        <h2 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
          <FiInfo className="text-crypto-blue" />
          Market Analysis Summary - Why These Coins Could Perform Strongly in 2026
        </h2>
        <div className="grid md:grid-cols-2 gap-4 text-gray-300">
          <div className="space-y-2">
            <p className="flex items-start gap-2">
              <FiCheckCircle className="text-green-400 mt-1 flex-shrink-0" />
              <span><strong className="text-white">Institutional Backing:</strong> Most projects have secured funding from top-tier VCs like Binance Labs, Coinbase Ventures, Paradigm, and Polychain Capital, indicating strong confidence from experienced investors.</span>
            </p>
            <p className="flex items-start gap-2">
              <FiCheckCircle className="text-green-400 mt-1 flex-shrink-0" />
              <span><strong className="text-white">Market Timing:</strong> 2026 is expected to be a strong growth year following the 2024 Bitcoin halving cycle, with institutional adoption accelerating.</span>
            </p>
            <p className="flex items-start gap-2">
              <FiCheckCircle className="text-green-400 mt-1 flex-shrink-0" />
              <span><strong className="text-white">Real Innovation:</strong> These projects solve genuine problems in scalability (MegaETH), DeFi efficiency (Marginfi, Aria), Web3 UX (Tria), and AI integration (Cogni, Ultiverse).</span>
            </p>
          </div>
          <div className="space-y-2">
            <p className="flex items-start gap-2">
              <FiCheckCircle className="text-green-400 mt-1 flex-shrink-0" />
              <span><strong className="text-white">Strong Fundamentals:</strong> Projects with working products, active communities, and proven demand before token launch tend to outperform post-listing.</span>
            </p>
            <p className="flex items-start gap-2">
              <FiCheckCircle className="text-green-400 mt-1 flex-shrink-0" />
              <span><strong className="text-white">Emerging Narratives:</strong> AI agents, real-world assets, Layer-2 scaling, and gaming are dominant themes expected to drive 2026 bull market.</span>
            </p>
            <p className="flex items-start gap-2">
              <FiCheckCircle className="text-green-400 mt-1 flex-shrink-0" />
              <span><strong className="text-white">Early Access Advantage:</strong> Presale and early launch participants historically see 3-10x returns if projects have solid fundamentals and market timing.</span>
            </p>
          </div>
        </div>
      </div>

      {/* Category Filter */}
      <div className="card p-4">
        <div className="flex items-center gap-2 mb-3">
          <FiFilter className="text-crypto-blue" />
          <h3 className="text-lg font-semibold text-white">Filter by Category</h3>
        </div>
        <div className="flex flex-wrap gap-2">
          {categories.map((category) => (
            <button
              key={category}
              onClick={() => setSelectedCategory(category)}
              className={`px-4 py-2 rounded-lg font-medium transition-all ${
                selectedCategory === category
                  ? 'bg-crypto-blue text-white'
                  : 'bg-gray-800 text-gray-400 hover:bg-gray-700 hover:text-white'
              }`}
            >
              {category}
            </button>
          ))}
        </div>
      </div>

      {/* Coins Grid */}
      <div className="grid gap-6">
        {filteredCoins.map((coin) => (
          <div key={coin.symbol} className="card p-6 hover:border-crypto-blue/50 transition-all">
            {/* Header */}
            <div className="flex justify-between items-start mb-4">
              <div className="flex-1">
                <div className="flex items-center gap-3 mb-2">
                  <h3 className="text-2xl font-bold text-white">{coin.name}</h3>
                  <span className="text-lg text-gray-400">{coin.symbol}</span>
                  <span className={`px-3 py-1 rounded-full text-xs font-semibold border ${getRecommendationColor(coin.recommendation)}`}>
                    {coin.recommendation}
                  </span>
                  <span className="px-3 py-1 rounded-full text-xs bg-purple-500/20 text-purple-400 border border-purple-500/30">
                    {coin.category}
                  </span>
                </div>
                <p className="text-gray-400 text-sm mb-2">{coin.useCase}</p>
              </div>
              <div className="text-right">
                <div className="text-sm text-gray-400 mb-1">Potential ROI</div>
                <div className="text-2xl font-bold text-green-400">{coin.potential}</div>
              </div>
            </div>

            {/* Key Info Grid */}
            <div className="grid md:grid-cols-4 gap-4 mb-4">
              <div className="bg-gray-800/50 rounded-lg p-3">
                <div className="flex items-center gap-2 text-gray-400 text-sm mb-1">
                  <FiCalendar />
                  Launch Date
                </div>
                <div className="text-white font-semibold">{coin.launchDate}</div>
              </div>
              <div className="bg-gray-800/50 rounded-lg p-3">
                <div className="flex items-center gap-2 text-gray-400 text-sm mb-1">
                  <FiDollarSign />
                  Presale Price
                </div>
                <div className="text-white font-semibold">{coin.presalePrice}</div>
              </div>
              <div className="bg-gray-800/50 rounded-lg p-3">
                <div className="flex items-center gap-2 text-gray-400 text-sm mb-1">
                  <FiTarget />
                  Est. Listing
                </div>
                <div className="text-white font-semibold">{coin.estimatedListing}</div>
              </div>
              <div className="bg-gray-800/50 rounded-lg p-3">
                <div className="flex items-center gap-2 text-gray-400 text-sm mb-1">
                  <FiUsers />
                  Funding Raised
                </div>
                <div className="text-white font-semibold">{coin.fundingRaised}</div>
              </div>
            </div>

            {/* Stage */}
            <div className="mb-4">
              <div className="flex items-center gap-2 mb-2">
                <FiCheckCircle className="text-crypto-blue" />
                <span className="text-sm font-semibold text-gray-400">Current Stage:</span>
              </div>
              <span className={`px-3 py-1 rounded-lg text-sm font-medium ${getStageColor(coin.stage)}`}>
                {coin.stage}
              </span>
            </div>

            {/* Technology */}
            <div className="mb-4">
              <div className="flex items-center gap-2 mb-2">
                <FiCpu className="text-crypto-blue" />
                <span className="text-sm font-semibold text-gray-400">Technology:</span>
              </div>
              <p className="text-white">{coin.technology}</p>
              <div className="mt-1 text-sm text-gray-400">
                <span className="text-crypto-blue">Blockchain:</span> {coin.blockchain}
              </div>
            </div>

            {/* Backers */}
            <div className="mb-4">
              <div className="flex items-center gap-2 mb-2">
                <FiUsers className="text-crypto-blue" />
                <span className="text-sm font-semibold text-gray-400">Backed By:</span>
              </div>
              <div className="flex flex-wrap gap-2">
                {coin.backers.map((backer, index) => (
                  <span key={index} className="px-3 py-1 rounded-full text-xs bg-gray-800 text-gray-300 border border-gray-700">
                    {backer}
                  </span>
                ))}
              </div>
            </div>

            {/* Why Recommended */}
            <div className="mb-4">
              <div className="flex items-center gap-2 mb-3">
                <FiStar className="text-crypto-blue" />
                <span className="text-sm font-semibold text-gray-400">Why Highly Recommended:</span>
              </div>
              <div className="grid md:grid-cols-2 gap-2">
                {coin.whyRecommended.map((reason, index) => (
                  <div key={index} className="flex items-start gap-2 text-sm">
                    <FiCheckCircle className="text-green-400 mt-0.5 flex-shrink-0" />
                    <span className="text-gray-300">{reason}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Footer */}
            {coin.website && (
              <div className="pt-4 border-t border-gray-800">
                <a
                  href={coin.website}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2 text-crypto-blue hover:text-blue-300 transition-colors"
                >
                  <span>Visit Official Website</span>
                  <FiExternalLink />
                </a>
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Disclaimer */}
      <div className="card p-6 bg-red-500/10 border-red-500/30">
        <h3 className="text-lg font-bold text-red-400 mb-3">⚠️ Investment Disclaimer</h3>
        <div className="text-gray-300 space-y-2 text-sm">
          <p>
            <strong>This is NOT financial advice.</strong> All information provided is for educational and research purposes only. 
            Cryptocurrency investments are highly speculative and risky.
          </p>
          <p>
            <strong>Do Your Own Research (DYOR):</strong> Always conduct thorough research, verify information from official sources, 
            read project whitepapers, and understand the risks before investing.
          </p>
          <p>
            <strong>Risk Warning:</strong> Presales and early-stage projects carry extreme risk. Only invest what you can afford to lose completely. 
            Past performance and VC backing do not guarantee future returns.
          </p>
          <p>
            <strong>Data Sources:</strong> Information compiled from CoinMarketCap, Messari, CoinGecko, ICO Drops, CoinList, and project official channels as of November 2025.
          </p>
        </div>
      </div>

      {/* Research Links */}
      <div className="card p-6">
        <h3 className="text-lg font-bold text-white mb-4">📚 Verify Information on Leading Platforms</h3>
        <div className="grid md:grid-cols-3 gap-4">
          <a href="https://icodrops.com/" target="_blank" rel="noopener noreferrer" className="flex items-center gap-2 p-3 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors">
            <FiExternalLink className="text-crypto-blue" />
            <span className="text-white">ICO Drops</span>
          </a>
          <a href="https://coinlist.co/token-launches" target="_blank" rel="noopener noreferrer" className="flex items-center gap-2 p-3 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors">
            <FiExternalLink className="text-crypto-blue" />
            <span className="text-white">CoinList</span>
          </a>
          <a href="https://www.coingecko.com/" target="_blank" rel="noopener noreferrer" className="flex items-center gap-2 p-3 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors">
            <FiExternalLink className="text-crypto-blue" />
            <span className="text-white">CoinGecko</span>
          </a>
          <a href="https://messari.io/" target="_blank" rel="noopener noreferrer" className="flex items-center gap-2 p-3 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors">
            <FiExternalLink className="text-crypto-blue" />
            <span className="text-white">Messari</span>
          </a>
          <a href="https://coinmarketcap.com/new/" target="_blank" rel="noopener noreferrer" className="flex items-center gap-2 p-3 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors">
            <FiExternalLink className="text-crypto-blue" />
            <span className="text-white">CoinMarketCap New Listings</span>
          </a>
          <a href="https://cryptorank.io/ico" target="_blank" rel="noopener noreferrer" className="flex items-center gap-2 p-3 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors">
            <FiExternalLink className="text-crypto-blue" />
            <span className="text-white">CryptoRank ICO</span>
          </a>
        </div>
      </div>
    </div>
  )
}
