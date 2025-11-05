"""
On-chain analytics agent.
Integrates with Glassnode, Santiment, CryptoQuant for whale tracking and metrics.
"""
import aiohttp
from typing import Dict, Optional
from datetime import datetime, timedelta
from loguru import logger
from config.settings import settings
import backoff


class OnChainAnalyticsAgent:
    """
    Agent for collecting and analyzing on-chain metrics.
    Tracks whale activity, exchange flows, holder behavior.
    """
    
    def __init__(self):
        self.session: Optional[aiohttp.ClientSession] = None
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    @backoff.on_exception(backoff.expo, Exception, max_tries=3)
    async def get_glassnode_metrics(self, symbol: str) -> Dict:
        """
        Fetch on-chain metrics from Glassnode.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., BTC, ETH)
            
        Returns:
            Dictionary with on-chain metrics
        """
        if not settings.glassnode_api_key:
            logger.warning("Glassnode API key not configured")
            return {}
        
        try:
            base_url = "https://api.glassnode.com/v1/metrics"
            params = {
                "a": symbol.upper(),
                "api_key": settings.glassnode_api_key,
                "s": int((datetime.now() - timedelta(days=7)).timestamp()),
                "i": "24h"
            }
            
            metrics_to_fetch = [
                "addresses/active_count",
                "addresses/new_non_zero_count",
                "distribution/balance_1pct_holders",
                "transactions/count",
                "transactions/transfers_volume_sum",
                "market/mvrv",
                "indicators/sopr",
                "indicators/net_unrealized_profit_loss",
                "supply/profit_relative",
            ]
            
            results = {}
            
            for metric in metrics_to_fetch:
                try:
                    url = f"{base_url}/{metric}"
                    async with self.session.get(url, params=params) as response:
                        if response.status == 200:
                            data = await response.json()
                            if data:
                                latest = data[-1] if isinstance(data, list) else data
                                metric_name = metric.split('/')[-1]
                                results[metric_name] = latest.get('v', 0)
                except Exception as e:
                    logger.warning(f"Error fetching {metric}: {e}")
                    continue
            
            logger.info(f"Fetched {len(results)} Glassnode metrics for {symbol}")
            return results
            
        except Exception as e:
            logger.error(f"Error fetching Glassnode data: {e}")
            return {}
    
    @backoff.on_exception(backoff.expo, Exception, max_tries=3)
    async def get_santiment_metrics(self, symbol: str) -> Dict:
        """
        Fetch on-chain and social metrics from Santiment.
        
        Args:
            symbol: Cryptocurrency symbol
            
        Returns:
            Dictionary with metrics
        """
        if not settings.santiment_api_key:
            logger.warning("Santiment API key not configured")
            return {}
        
        try:
            url = "https://api.santiment.net/graphql"
            headers = {
                "Authorization": f"Apikey {settings.santiment_api_key}",
                "Content-Type": "application/json"
            }
            
            # GraphQL query for multiple metrics
            query = """
            query {
                getMetric(metric: "active_addresses_24h") {
                    timeseriesData(
                        slug: "%s"
                        from: "%s"
                        to: "%s"
                        interval: "1d"
                    ) {
                        datetime
                        value
                    }
                }
            }
            """ % (
                symbol.lower(),
                (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
                datetime.now().strftime("%Y-%m-%d")
            )
            
            async with self.session.post(url, json={"query": query}, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    timeseries = data.get("data", {}).get("getMetric", {}).get("timeseriesData", [])
                    
                    if timeseries:
                        latest = timeseries[-1]
                        return {
                            "active_addresses": latest.get("value", 0),
                            "timestamp": latest.get("datetime")
                        }
                    
            return {}
            
        except Exception as e:
            logger.error(f"Error fetching Santiment data: {e}")
            return {}
    
    async def detect_whale_activity(self, symbol: str) -> Dict:
        """
        Detect whale accumulation/distribution patterns.
        
        Args:
            symbol: Cryptocurrency symbol
            
        Returns:
            Dictionary with whale activity signals
        """
        try:
            glassnode_data = await self.get_glassnode_metrics(symbol)
            
            # Analyze whale behavior
            whale_holders = glassnode_data.get("balance_1pct_holders", 0)
            
            # Simple heuristic - would be more sophisticated in production
            is_accumulating = False
            confidence = 0.0
            
            if whale_holders > 0:
                is_accumulating = True  # Placeholder logic
                confidence = 0.7
            
            return {
                "is_accumulating": is_accumulating,
                "confidence": confidence,
                "whale_holder_percentage": whale_holders,
                "signal": "BULLISH" if is_accumulating else "NEUTRAL"
            }
            
        except Exception as e:
            logger.error(f"Error detecting whale activity: {e}")
            return {
                "is_accumulating": False,
                "confidence": 0.0,
                "signal": "UNKNOWN"
            }
    
    async def get_exchange_flows(self, symbol: str) -> Dict:
        """
        Analyze exchange inflow/outflow patterns.
        
        Args:
            symbol: Cryptocurrency symbol
            
        Returns:
            Dictionary with exchange flow data
        """
        try:
            # This would integrate with CryptoQuant or similar
            # Placeholder implementation
            
            return {
                "exchange_inflow": 0.0,
                "exchange_outflow": 0.0,
                "net_flow": 0.0,
                "signal": "NEUTRAL",
                "interpretation": "Data not available"
            }
            
        except Exception as e:
            logger.error(f"Error getting exchange flows: {e}")
            return {}
    
    async def calculate_onchain_score(self, symbol: str) -> float:
        """
        Calculate composite on-chain health score.
        
        Args:
            symbol: Cryptocurrency symbol
            
        Returns:
            Score from 0-100
        """
        try:
            glassnode_data = await self.get_glassnode_metrics(symbol)
            whale_data = await self.detect_whale_activity(symbol)
            
            score = 50.0  # Base score
            
            # Adjust based on whale accumulation
            if whale_data.get("is_accumulating"):
                score += 20 * whale_data.get("confidence", 0)
            
            # Adjust based on active addresses (network health)
            active_addresses = glassnode_data.get("active_count", 0)
            if active_addresses > 100000:  # Healthy network
                score += 10
            
            # Adjust based on MVRV ratio
            mvrv = glassnode_data.get("mvrv", 1.0)
            if 0.8 < mvrv < 2.0:  # Healthy range
                score += 10
            elif mvrv > 3.0:  # Overheated
                score -= 20
            
            # Normalize to 0-100
            score = max(0, min(100, score))
            
            logger.info(f"On-chain score for {symbol}: {score:.2f}")
            return score
            
        except Exception as e:
            logger.error(f"Error calculating on-chain score: {e}")
            return 50.0  # Neutral score on error


class SentimentAnalysisAgent:
    """
    Agent for social sentiment analysis.
    Integrates with LunarCrush, Twitter API, Reddit, etc.
    """
    
    def __init__(self):
        self.session: Optional[aiohttp.ClientSession] = None
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    @backoff.on_exception(backoff.expo, Exception, max_tries=3)
    async def get_lunarcrush_data(self, symbol: str) -> Dict:
        """
        Fetch social metrics from LunarCrush.
        
        Args:
            symbol: Cryptocurrency symbol
            
        Returns:
            Dictionary with social metrics
        """
        if not settings.lunarcrush_api_key:
            logger.warning("LunarCrush API key not configured")
            return {}
        
        try:
            url = "https://api.lunarcrush.com/v2"
            params = {
                "data": "assets",
                "key": settings.lunarcrush_api_key,
                "symbol": symbol.upper()
            }
            
            async with self.session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    asset_data = data.get("data", [{}])[0]
                    
                    return {
                        "galaxy_score": asset_data.get("galaxy_score", 0),
                        "alt_rank": asset_data.get("alt_rank", 0),
                        "social_volume": asset_data.get("social_volume", 0),
                        "social_dominance": asset_data.get("social_dominance", 0),
                        "sentiment": asset_data.get("average_sentiment", 0),
                        "twitter_followers": asset_data.get("twitter_followers", 0),
                        "url_shares": asset_data.get("url_shares", 0),
                    }
                else:
                    logger.error(f"LunarCrush API error: {response.status}")
                    return {}
                    
        except Exception as e:
            logger.error(f"Error fetching LunarCrush data: {e}")
            return {}
    
    async def analyze_sentiment(self, symbol: str) -> Dict:
        """
        Perform comprehensive sentiment analysis.
        
        Args:
            symbol: Cryptocurrency symbol
            
        Returns:
            Dictionary with sentiment metrics
        """
        try:
            lunarcrush_data = await self.get_lunarcrush_data(symbol)
            
            # Calculate composite sentiment score
            sentiment_score = lunarcrush_data.get("sentiment", 0)
            galaxy_score = lunarcrush_data.get("galaxy_score", 0)
            
            # Normalize to -1 to 1 scale
            normalized_sentiment = (sentiment_score - 3) / 2  # Assuming 1-5 scale
            
            # Classify sentiment
            if normalized_sentiment > 0.3:
                label = "POSITIVE"
            elif normalized_sentiment < -0.3:
                label = "NEGATIVE"
            else:
                label = "NEUTRAL"
            
            return {
                "sentiment_score": normalized_sentiment,
                "sentiment_label": label,
                "social_volume": lunarcrush_data.get("social_volume", 0),
                "galaxy_score": galaxy_score,
                "alt_rank": lunarcrush_data.get("alt_rank", 0),
                "confidence": 0.7 if galaxy_score > 50 else 0.5
            }
            
        except Exception as e:
            logger.error(f"Error analyzing sentiment: {e}")
            return {
                "sentiment_score": 0.0,
                "sentiment_label": "NEUTRAL",
                "confidence": 0.0
            }
    
    async def calculate_sentiment_score(self, symbol: str) -> float:
        """
        Calculate composite sentiment score.
        
        Args:
            symbol: Cryptocurrency symbol
            
        Returns:
            Score from 0-100
        """
        try:
            sentiment_data = await self.analyze_sentiment(symbol)
            
            # Base score
            score = 50.0
            
            # Adjust based on sentiment
            sentiment = sentiment_data.get("sentiment_score", 0)
            score += sentiment * 30  # -30 to +30 adjustment
            
            # Adjust based on social volume
            social_volume = sentiment_data.get("social_volume", 0)
            if social_volume > 1000:
                score += 10
            
            # Adjust based on galaxy score
            galaxy_score = sentiment_data.get("galaxy_score", 0)
            if galaxy_score > 70:
                score += 10
            elif galaxy_score < 30:
                score -= 10
            
            # Normalize
            score = max(0, min(100, score))
            
            logger.info(f"Sentiment score for {symbol}: {score:.2f}")
            return score
            
        except Exception as e:
            logger.error(f"Error calculating sentiment score: {e}")
            return 50.0


# Example usage
if __name__ == "__main__":
    import asyncio
    
    async def test():
        async with OnChainAnalyticsAgent() as onchain_agent:
            metrics = await onchain_agent.get_glassnode_metrics("BTC")
            print(f"Glassnode metrics: {metrics}")
            
            score = await onchain_agent.calculate_onchain_score("BTC")
            print(f"On-chain score: {score}")
        
        async with SentimentAnalysisAgent() as sentiment_agent:
            sentiment = await sentiment_agent.analyze_sentiment("BTC")
            print(f"Sentiment: {sentiment}")
    
    asyncio.run(test())
