"""
Market phase detection agent using machine learning.
Detects: Hype, Crash, Accumulation, Expansion phases.
"""
import numpy as np
import pandas as pd
from typing import Dict, Tuple, List
from datetime import datetime, timedelta
from loguru import logger
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import os

from models.database import MarketPhase


class PhaseDetectorAgent:
    """
    Autonomous agent for detecting market phases using ML.
    
    Phases:
    - HYPE: Rapid price increase, high volume, parabolic move
    - CRASH: Sharp decline, panic selling, capitulation
    - ACCUMULATION: Sideways movement, low volatility, decreasing volume
    - EXPANSION: Steady uptrend, increasing volume, healthy growth
    """
    
    def __init__(self, model_path: str = "models/phase_detector.pkl"):
        self.model_path = model_path
        self.model = None
        self.scaler = StandardScaler()
        self.load_model()
    
    def load_model(self):
        """Load pre-trained model or create new one."""
        if os.path.exists(self.model_path):
            try:
                self.model = joblib.load(self.model_path)
                logger.info(f"Loaded phase detection model from {self.model_path}")
            except Exception as e:
                logger.error(f"Error loading model: {e}")
                self.model = None
        
        if self.model is None:
            logger.info("Initializing new phase detection model")
            self.model = RandomForestClassifier(
                n_estimators=100,
                max_depth=10,
                random_state=42
            )
    
    def save_model(self):
        """Save trained model to disk."""
        try:
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            joblib.dump(self.model, self.model_path)
            logger.info(f"Saved model to {self.model_path}")
        except Exception as e:
            logger.error(f"Error saving model: {e}")
    
    def calculate_features(self, price_data: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate features for phase detection.
        
        Args:
            price_data: DataFrame with OHLCV data
            
        Returns:
            DataFrame with calculated features
        """
        df = price_data.copy()
        
        # Price change features
        df['returns_1d'] = df['close'].pct_change(1)
        df['returns_7d'] = df['close'].pct_change(7)
        df['returns_30d'] = df['close'].pct_change(30)
        
        # Volatility
        df['volatility_7d'] = df['returns_1d'].rolling(7).std()
        df['volatility_30d'] = df['returns_1d'].rolling(30).std()
        
        # Volume features
        df['volume_ma_7'] = df['volume'].rolling(7).mean()
        df['volume_ma_30'] = df['volume'].rolling(30).mean()
        df['volume_ratio'] = df['volume'] / df['volume_ma_30']
        
        # Price momentum
        df['rsi_14'] = self._calculate_rsi(df['close'], 14)
        df['roc_14'] = df['close'].pct_change(14)
        
        # Moving averages
        df['ma_20'] = df['close'].rolling(20).mean()
        df['ma_50'] = df['close'].rolling(50).mean()
        df['ma_200'] = df['close'].rolling(200).mean()
        
        # Price position relative to MAs
        df['price_to_ma20'] = (df['close'] - df['ma_20']) / df['ma_20']
        df['price_to_ma50'] = (df['close'] - df['ma_50']) / df['ma_50']
        df['price_to_ma200'] = (df['close'] - df['ma_200']) / df['ma_200']
        
        # Bollinger Bands
        df['bb_middle'] = df['close'].rolling(20).mean()
        df['bb_std'] = df['close'].rolling(20).std()
        df['bb_upper'] = df['bb_middle'] + (df['bb_std'] * 2)
        df['bb_lower'] = df['bb_middle'] - (df['bb_std'] * 2)
        df['bb_position'] = (df['close'] - df['bb_lower']) / (df['bb_upper'] - df['bb_lower'])
        
        # ATH/ATL distance
        df['distance_from_ath'] = (df['high'].rolling(365).max() - df['close']) / df['high'].rolling(365).max()
        df['distance_from_atl'] = (df['close'] - df['low'].rolling(365).min()) / df['close']
        
        # Trend strength
        df['adx'] = self._calculate_adx(df, 14)
        
        return df
    
    def _calculate_rsi(self, prices: pd.Series, period: int = 14) -> pd.Series:
        """Calculate Relative Strength Index."""
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
    def _calculate_adx(self, df: pd.DataFrame, period: int = 14) -> pd.Series:
        """Calculate Average Directional Index (trend strength)."""
        high = df['high']
        low = df['low']
        close = df['close']
        
        plus_dm = high.diff()
        minus_dm = -low.diff()
        
        plus_dm[plus_dm < 0] = 0
        minus_dm[minus_dm < 0] = 0
        
        tr = pd.concat([
            high - low,
            abs(high - close.shift()),
            abs(low - close.shift())
        ], axis=1).max(axis=1)
        
        atr = tr.rolling(period).mean()
        plus_di = 100 * (plus_dm.rolling(period).mean() / atr)
        minus_di = 100 * (minus_dm.rolling(period).mean() / atr)
        
        dx = 100 * abs(plus_di - minus_di) / (plus_di + minus_di)
        adx = dx.rolling(period).mean()
        
        return adx
    
    def detect_phase_rules_based(self, features: pd.Series) -> Tuple[MarketPhase, float]:
        """
        Rule-based phase detection (fallback when ML model not trained).
        
        Args:
            features: Series with calculated features
            
        Returns:
            Tuple of (phase, confidence)
        """
        # HYPE detection
        if (features['returns_7d'] > 0.3 and  # >30% gain in 7 days
            features['volume_ratio'] > 2 and   # Volume 2x above average
            features['rsi_14'] > 70 and        # Overbought
            features['bb_position'] > 0.9):    # Near upper Bollinger Band
            return MarketPhase.HYPE, 0.85
        
        # CRASH detection
        if (features['returns_7d'] < -0.25 and  # >25% loss in 7 days
            features['volume_ratio'] > 1.5 and   # High volume
            features['rsi_14'] < 30):            # Oversold
            return MarketPhase.CRASH, 0.85
        
        # ACCUMULATION detection
        if (abs(features['returns_30d']) < 0.15 and  # Low price movement
            features['volatility_30d'] < 0.02 and     # Low volatility
            features['volume_ratio'] < 0.8 and        # Below average volume
            features['distance_from_ath'] > 0.5):     # Far from ATH
            return MarketPhase.ACCUMULATION, 0.75
        
        # EXPANSION detection
        if (features['returns_30d'] > 0.15 and     # Positive 30d return
            features['returns_30d'] < 0.5 and      # Not parabolic
            features['price_to_ma50'] > 0 and      # Above MA50
            features['adx'] > 25 and               # Strong trend
            features['volume_ratio'] > 1.0):       # Good volume
            return MarketPhase.EXPANSION, 0.80
        
        return MarketPhase.UNKNOWN, 0.5
    
    def detect_phase(self, price_data: pd.DataFrame) -> Dict:
        """
        Detect current market phase for a coin.
        
        Args:
            price_data: DataFrame with OHLCV data (at least 200 days)
            
        Returns:
            Dictionary with phase, confidence, and metadata
        """
        try:
            if len(price_data) < 200:
                logger.warning(f"Insufficient data for phase detection: {len(price_data)} days")
                return {
                    "phase": MarketPhase.UNKNOWN,
                    "confidence": 0.0,
                    "error": "Insufficient historical data"
                }
            
            # Calculate features
            df_features = self.calculate_features(price_data)
            
            # Get latest features
            latest = df_features.iloc[-1]
            
            # Feature columns for ML
            feature_cols = [
                'returns_1d', 'returns_7d', 'returns_30d',
                'volatility_7d', 'volatility_30d',
                'volume_ratio', 'rsi_14', 'roc_14',
                'price_to_ma20', 'price_to_ma50', 'price_to_ma200',
                'bb_position', 'distance_from_ath', 'distance_from_atl',
                'adx'
            ]
            
            # Check if we have a trained model
            if hasattr(self.model, 'predict_proba'):
                try:
                    # Prepare features
                    X = latest[feature_cols].values.reshape(1, -1)
                    X = np.nan_to_num(X, nan=0.0)
                    
                    # Predict
                    probabilities = self.model.predict_proba(X)[0]
                    phase_idx = np.argmax(probabilities)
                    confidence = probabilities[phase_idx]
                    
                    phases = [MarketPhase.ACCUMULATION, MarketPhase.EXPANSION, 
                             MarketPhase.HYPE, MarketPhase.CRASH]
                    detected_phase = phases[phase_idx]
                    
                except Exception as e:
                    logger.warning(f"ML prediction failed, using rule-based: {e}")
                    detected_phase, confidence = self.detect_phase_rules_based(latest)
            else:
                # Use rule-based detection
                detected_phase, confidence = self.detect_phase_rules_based(latest)
            
            return {
                "phase": detected_phase,
                "confidence": float(confidence),
                "features": {
                    "returns_7d": float(latest['returns_7d']),
                    "returns_30d": float(latest['returns_30d']),
                    "volatility_30d": float(latest['volatility_30d']),
                    "volume_ratio": float(latest['volume_ratio']),
                    "rsi": float(latest['rsi_14']),
                    "distance_from_ath": float(latest['distance_from_ath']),
                },
                "timestamp": datetime.utcnow().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Error detecting phase: {e}")
            return {
                "phase": MarketPhase.UNKNOWN,
                "confidence": 0.0,
                "error": str(e)
            }
    
    def get_recommendation(self, phase: MarketPhase, confidence: float) -> str:
        """
        Get investment recommendation based on phase.
        
        Args:
            phase: Detected market phase
            confidence: Confidence score
            
        Returns:
            Recommendation string
        """
        if confidence < 0.6:
            return "HOLD - Low confidence in phase detection"
        
        recommendations = {
            MarketPhase.HYPE: "AVOID/SELL - High risk of correction",
            MarketPhase.CRASH: "HOLD/WAIT - Avoid catching falling knife",
            MarketPhase.ACCUMULATION: "BUY - Ideal accumulation zone",
            MarketPhase.EXPANSION: "BUY/HOLD - Healthy uptrend",
            MarketPhase.UNKNOWN: "HOLD - Unclear market phase"
        }
        
        return recommendations.get(phase, "HOLD")
    
    def train_model(self, labeled_data: pd.DataFrame):
        """
        Train the phase detection model on labeled data.
        
        Args:
            labeled_data: DataFrame with features and 'phase' labels
        """
        try:
            logger.info("Training phase detection model...")
            
            feature_cols = [
                'returns_1d', 'returns_7d', 'returns_30d',
                'volatility_7d', 'volatility_30d',
                'volume_ratio', 'rsi_14', 'roc_14',
                'price_to_ma20', 'price_to_ma50', 'price_to_ma200',
                'bb_position', 'distance_from_ath', 'distance_from_atl',
                'adx'
            ]
            
            X = labeled_data[feature_cols].values
            X = np.nan_to_num(X, nan=0.0)
            y = labeled_data['phase'].values
            
            # Scale features
            X_scaled = self.scaler.fit_transform(X)
            
            # Train model
            self.model.fit(X_scaled, y)
            
            # Save model
            self.save_model()
            
            logger.info("Model training completed successfully")
            
        except Exception as e:
            logger.error(f"Error training model: {e}")


# Example usage
if __name__ == "__main__":
    # Create sample data
    dates = pd.date_range(start='2023-01-01', periods=365, freq='D')
    sample_data = pd.DataFrame({
        'timestamp': dates,
        'open': np.random.randn(365).cumsum() + 100,
        'high': np.random.randn(365).cumsum() + 105,
        'low': np.random.randn(365).cumsum() + 95,
        'close': np.random.randn(365).cumsum() + 100,
        'volume': np.random.randint(1000000, 10000000, 365)
    })
    
    detector = PhaseDetectorAgent()
    result = detector.detect_phase(sample_data)
    
    print(f"Detected Phase: {result['phase']}")
    print(f"Confidence: {result['confidence']:.2f}")
    print(f"Recommendation: {detector.get_recommendation(result['phase'], result['confidence'])}")
