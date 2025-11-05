"""
Composite scoring engine.
Combines fundamental, technical, on-chain, and sentiment analysis.
"""
from typing import Dict, List
from loguru import logger
from models.database import MarketPhase, Recommendation
import numpy as np


class ScoringEngine:
    """
    Multi-factor scoring engine for cryptocurrency opportunity assessment.
    """
    
    def __init__(self):
        # Weights for different factors (should sum to 1.0)
        self.weights = {
            "fundamental": 0.30,
            "technical": 0.25,
            "onchain": 0.25,
            "sentiment": 0.20
        }
        
        # Phase-based adjustments
        self.phase_multipliers = {
            MarketPhase.ACCUMULATION: 1.3,  # Boost accumulation phase
            MarketPhase.EXPANSION: 1.2,     # Boost expansion
            MarketPhase.HYPE: 0.6,          # Penalize hype
            MarketPhase.CRASH: 0.7,         # Penalize crash
            MarketPhase.UNKNOWN: 1.0        # Neutral
        }
    
    def calculate_fundamental_score(self, fundamental_data: Dict) -> float:
        """
        Calculate fundamental analysis score.
        
        Args:
            fundamental_data: Dictionary with fundamental metrics
            
        Returns:
            Score from 0-100
        """
        score = 0.0
        max_score = 100.0
        
        # Team score (25 points)
        team_score = fundamental_data.get("team_score", 0)
        github_commits = fundamental_data.get("github_commits_30d", 0)
        
        score += min(15, team_score * 0.15)
        if github_commits > 50:
            score += 10
        elif github_commits > 20:
            score += 5
        
        # Technology score (20 points)
        tech_score = fundamental_data.get("technology_score", 0)
        score += min(20, tech_score * 0.20)
        
        # Tokenomics (25 points)
        tokenomics_score = fundamental_data.get("tokenomics_score", 0)
        inflation_rate = fundamental_data.get("inflation_rate", 0)
        
        score += min(15, tokenomics_score * 0.15)
        
        # Penalize high inflation
        if inflation_rate > 10:
            score -= 10
        elif inflation_rate < 3:
            score += 10
        
        # Community strength (15 points)
        community_score = fundamental_data.get("community_score", 0)
        score += min(15, community_score * 0.15)
        
        # DeFi metrics (15 points)
        tvl = fundamental_data.get("tvl", 0)
        if tvl > 1_000_000_000:  # $1B+ TVL
            score += 15
        elif tvl > 100_000_000:  # $100M+ TVL
            score += 10
        elif tvl > 10_000_000:   # $10M+ TVL
            score += 5
        
        return min(max_score, max(0, score))
    
    def calculate_technical_score(self, price_data: Dict, phase_info: Dict) -> float:
        """
        Calculate technical analysis score.
        
        Args:
            price_data: Dictionary with price and technical indicators
            phase_info: Phase detection results
            
        Returns:
            Score from 0-100
        """
        score = 50.0  # Base score
        
        # RSI analysis (20 points)
        rsi = price_data.get("rsi", 50)
        if 30 < rsi < 40:  # Oversold but recovering
            score += 20
        elif 40 <= rsi <= 60:  # Neutral
            score += 10
        elif rsi > 70:  # Overbought
            score -= 15
        elif rsi < 30:  # Deeply oversold
            score += 5
        
        # Price vs MA analysis (20 points)
        price_to_ma50 = price_data.get("price_to_ma50", 0)
        price_to_ma200 = price_data.get("price_to_ma200", 0)
        
        if price_to_ma200 > 0 and price_to_ma50 > 0:
            score += 15  # Above both MAs
        elif price_to_ma200 < 0 and price_to_ma50 > 0:
            score += 10  # Golden cross potential
        
        # Volume trend (15 points)
        volume_ratio = price_data.get("volume_ratio", 1.0)
        if volume_ratio > 1.5:
            score += 10  # High volume
        elif volume_ratio > 1.0:
            score += 5
        
        # Bollinger Band position (15 points)
        bb_position = price_data.get("bb_position", 0.5)
        if 0.2 < bb_position < 0.4:  # Near lower band
            score += 15
        elif 0.4 <= bb_position <= 0.6:  # Middle
            score += 5
        elif bb_position > 0.8:  # Near upper band
            score -= 10
        
        # Distance from ATH (10 points)
        distance_from_ath = price_data.get("distance_from_ath", 0)
        if distance_from_ath > 0.7:  # >70% down from ATH
            score += 10
        elif distance_from_ath > 0.5:  # >50% down
            score += 5
        
        # Phase confidence bonus (10 points)
        phase_confidence = phase_info.get("confidence", 0)
        score += phase_confidence * 10
        
        return min(100, max(0, score))
    
    def calculate_opportunity_score(
        self,
        fundamental_score: float,
        technical_score: float,
        onchain_score: float,
        sentiment_score: float,
        phase: MarketPhase,
        phase_confidence: float
    ) -> Dict:
        """
        Calculate composite opportunity score.
        
        Args:
            fundamental_score: Score from fundamental analysis
            technical_score: Score from technical analysis
            onchain_score: Score from on-chain analysis
            sentiment_score: Score from sentiment analysis
            phase: Detected market phase
            phase_confidence: Confidence in phase detection
            
        Returns:
            Dictionary with scores and recommendation
        """
        # Calculate weighted composite score
        composite = (
            fundamental_score * self.weights["fundamental"] +
            technical_score * self.weights["technical"] +
            onchain_score * self.weights["onchain"] +
            sentiment_score * self.weights["sentiment"]
        )
        
        # Apply phase multiplier
        phase_multiplier = self.phase_multipliers.get(phase, 1.0)
        
        # Reduce multiplier impact if confidence is low
        adjusted_multiplier = 1.0 + (phase_multiplier - 1.0) * phase_confidence
        
        final_score = composite * adjusted_multiplier
        
        # Normalize to 0-100
        final_score = min(100, max(0, final_score))
        
        # Generate recommendation
        recommendation = self._generate_recommendation(
            final_score, phase, phase_confidence
        )
        
        return {
            "opportunity_score": round(final_score, 2),
            "fundamental_score": round(fundamental_score, 2),
            "technical_score": round(technical_score, 2),
            "onchain_score": round(onchain_score, 2),
            "sentiment_score": round(sentiment_score, 2),
            "phase": phase,
            "phase_confidence": round(phase_confidence, 2),
            "recommendation": recommendation,
            "weights": self.weights,
            "breakdown": {
                "fundamental_contribution": round(fundamental_score * self.weights["fundamental"], 2),
                "technical_contribution": round(technical_score * self.weights["technical"], 2),
                "onchain_contribution": round(onchain_score * self.weights["onchain"], 2),
                "sentiment_contribution": round(sentiment_score * self.weights["sentiment"], 2),
            }
        }
    
    def _generate_recommendation(
        self, 
        score: float, 
        phase: MarketPhase, 
        confidence: float
    ) -> str:
        """
        Generate investment recommendation.
        
        Args:
            score: Composite opportunity score
            phase: Market phase
            confidence: Phase detection confidence
            
        Returns:
            Recommendation enum
        """
        # Low confidence = Hold
        if confidence < 0.5:
            return Recommendation.HOLD
        
        # Phase-based recommendations
        if phase == MarketPhase.HYPE:
            return Recommendation.AVOID if score < 70 else Recommendation.HOLD
        
        if phase == MarketPhase.CRASH:
            return Recommendation.HOLD if score < 50 else Recommendation.BUY
        
        if phase == MarketPhase.ACCUMULATION:
            if score >= 75:
                return Recommendation.STRONG_BUY
            elif score >= 60:
                return Recommendation.BUY
            else:
                return Recommendation.HOLD
        
        if phase == MarketPhase.EXPANSION:
            if score >= 70:
                return Recommendation.BUY
            elif score >= 50:
                return Recommendation.HOLD
            else:
                return Recommendation.SELL
        
        # Default score-based
        if score >= 80:
            return Recommendation.STRONG_BUY
        elif score >= 65:
            return Recommendation.BUY
        elif score >= 40:
            return Recommendation.HOLD
        elif score >= 25:
            return Recommendation.SELL
        else:
            return Recommendation.AVOID
    
    def rank_coins(self, coins_scores: List[Dict]) -> List[Dict]:
        """
        Rank coins by opportunity score.
        
        Args:
            coins_scores: List of coin scoring results
            
        Returns:
            Sorted list of coins with ranks
        """
        # Sort by opportunity score
        sorted_coins = sorted(
            coins_scores,
            key=lambda x: x.get("opportunity_score", 0),
            reverse=True
        )
        
        # Add rank
        for i, coin in enumerate(sorted_coins, 1):
            coin["rank"] = i
        
        return sorted_coins
    
    def identify_top_opportunities(
        self,
        coins_scores: List[Dict],
        min_score: float = 70.0,
        preferred_phases: List[MarketPhase] = None
    ) -> List[Dict]:
        """
        Identify top investment opportunities.
        
        Args:
            coins_scores: List of coin scoring results
            min_score: Minimum opportunity score
            preferred_phases: List of preferred market phases
            
        Returns:
            Filtered list of top opportunities
        """
        if preferred_phases is None:
            preferred_phases = [MarketPhase.ACCUMULATION, MarketPhase.EXPANSION]
        
        opportunities = []
        
        for coin in coins_scores:
            score = coin.get("opportunity_score", 0)
            phase = coin.get("phase", MarketPhase.UNKNOWN)
            
            if score >= min_score and phase in preferred_phases:
                opportunities.append(coin)
        
        # Sort by score
        opportunities = sorted(
            opportunities,
            key=lambda x: x.get("opportunity_score", 0),
            reverse=True
        )
        
        return opportunities


# Example usage
if __name__ == "__main__":
    engine = ScoringEngine()
    
    # Sample data
    fundamental = {"team_score": 80, "technology_score": 75, "tokenomics_score": 70}
    technical = {"rsi": 35, "price_to_ma50": -0.1, "volume_ratio": 1.2}
    
    result = engine.calculate_opportunity_score(
        fundamental_score=75,
        technical_score=68,
        onchain_score=72,
        sentiment_score=65,
        phase=MarketPhase.ACCUMULATION,
        phase_confidence=0.85
    )
    
    print("Scoring Result:")
    print(f"Opportunity Score: {result['opportunity_score']}")
    print(f"Recommendation: {result['recommendation']}")
    print(f"Breakdown: {result['breakdown']}")
