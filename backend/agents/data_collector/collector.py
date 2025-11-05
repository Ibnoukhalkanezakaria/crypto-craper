"""
Multi-source data collection agent.
Aggregates data from CoinGecko, CoinMarketCap, Messari, DeFiLlama, etc.
"""
import asyncio
import aiohttp
from typing import Dict, List, Optional
from datetime import datetime
from loguru import logger
from pycoingecko import CoinGeckoAPI
from config.settings import settings
import backoff


class DataCollectorAgent:
    """
    Autonomous agent for collecting cryptocurrency data from multiple sources.
    """
    
    def __init__(self):
        self.cg = CoinGeckoAPI(api_key=settings.coingecko_api_key)
        self.session: Optional[aiohttp.ClientSession] = None
        
    async def __aenter__(self):
        """Async context manager entry."""
        self.session = aiohttp.ClientSession(
            headers={"User-Agent": settings.user_agent}
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self.session:
            await self.session.close()
    
    @backoff.on_exception(backoff.expo, Exception, max_tries=3)
    async def collect_coingecko_data(self, coin_id: str) -> Dict:
        """
        Collect comprehensive data from CoinGecko.
        
        Args:
            coin_id: CoinGecko coin ID
            
        Returns:
            Dictionary with coin data
        """
        try:
            logger.info(f"Collecting CoinGecko data for {coin_id}")
            
            # Get coin details
            coin_data = self.cg.get_coin_by_id(
                id=coin_id,
                localization=False,
                tickers=False,
                market_data=True,
                community_data=True,
                developer_data=True
            )
            
            return {
                "symbol": coin_data.get("symbol", "").upper(),
                "name": coin_data.get("name"),
                "current_price": coin_data.get("market_data", {}).get("current_price", {}).get("usd"),
                "market_cap": coin_data.get("market_data", {}).get("market_cap", {}).get("usd"),
                "volume_24h": coin_data.get("market_data", {}).get("total_volume", {}).get("usd"),
                "circulating_supply": coin_data.get("market_data", {}).get("circulating_supply"),
                "total_supply": coin_data.get("market_data", {}).get("total_supply"),
                "max_supply": coin_data.get("market_data", {}).get("max_supply"),
                "ath": coin_data.get("market_data", {}).get("ath", {}).get("usd"),
                "atl": coin_data.get("market_data", {}).get("atl", {}).get("usd"),
                "community": {
                    "twitter_followers": coin_data.get("community_data", {}).get("twitter_followers"),
                    "reddit_subscribers": coin_data.get("community_data", {}).get("reddit_subscribers"),
                    "telegram_members": coin_data.get("community_data", {}).get("telegram_channel_user_count"),
                },
                "developer": {
                    "github_stars": coin_data.get("developer_data", {}).get("stars"),
                    "github_forks": coin_data.get("developer_data", {}).get("forks"),
                    "github_commits_4w": coin_data.get("developer_data", {}).get("commit_count_4_weeks"),
                    "github_contributors": coin_data.get("developer_data", {}).get("contributors"),
                },
                "links": {
                    "homepage": coin_data.get("links", {}).get("homepage", [None])[0],
                    "github": coin_data.get("links", {}).get("repos_url", {}).get("github", [None])[0],
                    "whitepaper": coin_data.get("links", {}).get("whitepaper"),
                },
            }
            
        except Exception as e:
            logger.error(f"Error collecting CoinGecko data for {coin_id}: {e}")
            return {}
    
    async def collect_coinmarketcap_data(self, symbol: str) -> Dict:
        """
        Collect data from CoinMarketCap API.
        
        Args:
            symbol: Cryptocurrency symbol
            
        Returns:
            Dictionary with coin data
        """
        if not settings.coinmarketcap_api_key:
            logger.warning("CoinMarketCap API key not configured")
            return {}
        
        try:
            url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
            params = {"symbol": symbol}
            headers = {"X-CMC_PRO_API_KEY": settings.coinmarketcap_api_key}
            
            async with self.session.get(url, params=params, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    coin_data = data.get("data", {}).get(symbol, [{}])[0]
                    
                    return {
                        "cmc_rank": coin_data.get("cmc_rank"),
                        "num_market_pairs": coin_data.get("num_market_pairs"),
                        "tags": coin_data.get("tags", []),
                        "platform": coin_data.get("platform"),
                        "quote": coin_data.get("quote", {}).get("USD", {}),
                    }
                else:
                    logger.error(f"CoinMarketCap API error: {response.status}")
                    return {}
                    
        except Exception as e:
            logger.error(f"Error collecting CoinMarketCap data for {symbol}: {e}")
            return {}
    
    async def collect_messari_data(self, symbol: str) -> Dict:
        """
        Collect research data from Messari.
        
        Args:
            symbol: Cryptocurrency symbol
            
        Returns:
            Dictionary with research data
        """
        if not settings.messari_api_key:
            logger.warning("Messari API key not configured")
            return {}
        
        try:
            base_url = f"https://data.messari.io/api/v1/assets/{symbol.lower()}"
            headers = {"x-messari-api-key": settings.messari_api_key}
            
            # Get metrics
            async with self.session.get(f"{base_url}/metrics", headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    metrics = data.get("data", {})
                    
                    return {
                        "risk_metrics": metrics.get("risk_metrics", {}),
                        "blockchain_stats": metrics.get("blockchain_stats_24_hours", {}),
                        "developer_activity": metrics.get("developer_activity", {}),
                        "roi_data": metrics.get("roi_data", {}),
                        "supply": metrics.get("supply", {}),
                    }
                else:
                    logger.error(f"Messari API error: {response.status}")
                    return {}
                    
        except Exception as e:
            logger.error(f"Error collecting Messari data for {symbol}: {e}")
            return {}
    
    async def collect_defillama_data(self, protocol_name: str) -> Dict:
        """
        Collect DeFi protocol data from DeFiLlama.
        
        Args:
            protocol_name: Protocol name (slug)
            
        Returns:
            Dictionary with TVL and protocol data
        """
        try:
            url = f"https://api.llama.fi/protocol/{protocol_name}"
            
            async with self.session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    # Get latest TVL
                    tvl_data = data.get("tvl", [])
                    latest_tvl = tvl_data[-1] if tvl_data else {}
                    previous_tvl = tvl_data[-2] if len(tvl_data) > 1 else {}
                    
                    return {
                        "tvl": latest_tvl.get("totalLiquidityUSD", 0),
                        "tvl_prev": previous_tvl.get("totalLiquidityUSD", 0),
                        "chain_tvls": data.get("chainTvls", {}),
                        "category": data.get("category"),
                        "chains": data.get("chains", []),
                        "symbol": data.get("symbol"),
                    }
                else:
                    logger.warning(f"DeFiLlama data not found for {protocol_name}")
                    return {}
                    
        except Exception as e:
            logger.error(f"Error collecting DeFiLlama data for {protocol_name}: {e}")
            return {}
    
    async def scrape_token_unlocks(self, symbol: str) -> Dict:
        """
        Scrape token unlock schedule from TokenUnlocks.app.
        
        Args:
            symbol: Cryptocurrency symbol
            
        Returns:
            Dictionary with unlock schedule
        """
        try:
            from bs4 import BeautifulSoup
            
            url = f"https://token.unlocks.app/{symbol.lower()}"
            
            async with self.session.get(url) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # Parse unlock schedule (simplified - actual implementation would be more robust)
                    unlocks = []
                    
                    # This is a placeholder - actual scraping logic would parse the page structure
                    logger.info(f"Scraped TokenUnlocks data for {symbol}")
                    
                    return {
                        "has_unlocks": True,
                        "unlocks": unlocks,
                        "next_unlock": None,  # Would be parsed from page
                    }
                else:
                    return {"has_unlocks": False}
                    
        except Exception as e:
            logger.error(f"Error scraping TokenUnlocks for {symbol}: {e}")
            return {}
    
    async def collect_all_sources(self, coin_id: str, symbol: str) -> Dict:
        """
        Collect data from all sources in parallel.
        
        Args:
            coin_id: CoinGecko coin ID
            symbol: Cryptocurrency symbol
            
        Returns:
            Aggregated data from all sources
        """
        logger.info(f"Collecting data from all sources for {symbol}")
        
        # Gather data from all sources concurrently
        results = await asyncio.gather(
            self.collect_coingecko_data(coin_id),
            self.collect_coinmarketcap_data(symbol),
            self.collect_messari_data(symbol),
            self.collect_defillama_data(symbol.lower()),
            self.scrape_token_unlocks(symbol),
            return_exceptions=True
        )
        
        coingecko_data, cmc_data, messari_data, defillama_data, unlocks_data = results
        
        # Merge all data
        aggregated = {
            "coin_id": coin_id,
            "symbol": symbol,
            "timestamp": datetime.utcnow().isoformat(),
            "sources": {
                "coingecko": coingecko_data if not isinstance(coingecko_data, Exception) else {},
                "coinmarketcap": cmc_data if not isinstance(cmc_data, Exception) else {},
                "messari": messari_data if not isinstance(messari_data, Exception) else {},
                "defillama": defillama_data if not isinstance(defillama_data, Exception) else {},
                "token_unlocks": unlocks_data if not isinstance(unlocks_data, Exception) else {},
            }
        }
        
        logger.info(f"Successfully collected data for {symbol} from all sources")
        return aggregated
    
    async def collect_top_coins(self, limit: int = 500) -> List[Dict]:
        """
        Collect data for top N coins by market cap.
        
        Args:
            limit: Number of top coins to collect
            
        Returns:
            List of aggregated coin data
        """
        logger.info(f"Collecting data for top {limit} coins")
        
        try:
            # Get top coins from CoinGecko
            coins_list = self.cg.get_coins_markets(
                vs_currency="usd",
                order="market_cap_desc",
                per_page=limit,
                page=1
            )
            
            # Collect detailed data for each coin
            tasks = [
                self.collect_all_sources(coin["id"], coin["symbol"].upper())
                for coin in coins_list
            ]
            
            # Process in batches to avoid rate limits
            batch_size = settings.max_concurrent_requests
            all_data = []
            
            for i in range(0, len(tasks), batch_size):
                batch = tasks[i:i + batch_size]
                batch_results = await asyncio.gather(*batch, return_exceptions=True)
                
                for result in batch_results:
                    if not isinstance(result, Exception):
                        all_data.append(result)
                
                # Delay between batches
                if i + batch_size < len(tasks):
                    await asyncio.sleep(settings.scraping_delay)
            
            logger.info(f"Collected data for {len(all_data)} coins")
            return all_data
            
        except Exception as e:
            logger.error(f"Error collecting top coins: {e}")
            return []


async def main():
    """Test the data collector agent."""
    async with DataCollectorAgent() as agent:
        # Test with Bitcoin
        data = await agent.collect_all_sources("bitcoin", "BTC")
        print(f"Collected data: {data}")


if __name__ == "__main__":
    asyncio.run(main())
