"""
Technical Analysis Utility
Provides technical indicators and pattern detection
"""

import pandas as pd
import numpy as np
from typing import Optional

class TechnicalAnalyzer:
    """Technical analysis tools for stock data"""
    
    def calculate_relative_strength(self, symbol: str, data: pd.DataFrame) -> float:
        """
        Calculate relative strength vs sector
        
        Args:
            symbol: Stock symbol
            data: Stock price data
        
        Returns:
            Relative strength ratio (>1 means outperforming)
        """
        # Simplified calculation
        # In production, would compare to sector index
        
        recent_return = (data['Close'].iloc[-1] / data['Close'].iloc[-7] - 1)
        
        # Assume sector average is 0% (neutral)
        sector_return = 0.0
        
        if sector_return == 0:
            return 1.0 + recent_return
        
        return (1 + recent_return) / (1 + sector_return)
    
    def detect_coiling_pattern(self, data: pd.DataFrame, window: int = 5) -> bool:
        """
        Detect coiling/compression pattern
        Price trades in tight range before explosive move
        
        Args:
            data: Stock price data
            window: Number of days to check
        
        Returns:
            True if coiling pattern detected
        """
        if len(data) < window:
            return False
        
        recent_data = data.iloc[-window:]
        
        # Calculate price range
        high = recent_data['High'].max()
        low = recent_data['Low'].min()
        avg_price = recent_data['Close'].mean()
        
        # Coiling if range is < 5% of average price
        price_range_pct = (high - low) / avg_price
        
        return price_range_pct < 0.05
    
    def detect_accumulation(self, data: pd.DataFrame, min_days: int = 3) -> bool:
        """
        Detect accumulation pattern (higher lows + rising volume)
        
        Args:
            data: Stock price data
            min_days: Minimum consecutive days required
        
        Returns:
            True if accumulation detected
        """
        if len(data) < min_days + 1:
            return False
        
        recent_data = data.iloc[-(min_days + 1):]
        
        # Check for higher lows
        lows = recent_data['Low'].values
        higher_lows = all(lows[i] >= lows[i-1] * 0.98 for i in range(1, len(lows)))
        
        # Check for rising volume
        volumes = recent_data['Volume'].values
        rising_volume = volumes[-1] > volumes[0]
        
        return higher_lows and rising_volume
    
    def is_pump_and_dump(self, data: pd.DataFrame) -> bool:
        """
        Detect potential pump and dump schemes
        
        Args:
            data: Stock price data
        
        Returns:
            True if pump and dump pattern detected
        """
        if len(data) < 10:
            return False
        
        recent_data = data.iloc[-10:]
        
        # Extreme volatility (>50% swings)
        max_price = recent_data['High'].max()
        min_price = recent_data['Low'].min()
        volatility = (max_price - min_price) / min_price
        
        # Very low volume after spike
        volume_drop = recent_data['Volume'].iloc[-1] / recent_data['Volume'].iloc[-5:-1].mean()
        
        return volatility > 0.5 and volume_drop < 0.3
    
    def calculate_rsi(self, data: pd.DataFrame, period: int = 14) -> float:
        """
        Calculate Relative Strength Index
        
        Args:
            data: Stock price data
            period: RSI period
        
        Returns:
            RSI value (0-100)
        """
        if len(data) < period + 1:
            return 50.0
        
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi.iloc[-1]
    
    def calculate_macd(self, data: pd.DataFrame) -> dict:
        """
        Calculate MACD (Moving Average Convergence Divergence)
        
        Args:
            data: Stock price data
        
        Returns:
            Dictionary with MACD, signal, and histogram
        """
        exp1 = data['Close'].ewm(span=12, adjust=False).mean()
        exp2 = data['Close'].ewm(span=26, adjust=False).mean()
        
        macd = exp1 - exp2
        signal = macd.ewm(span=9, adjust=False).mean()
        histogram = macd - signal
        
        return {
            'macd': macd.iloc[-1],
            'signal': signal.iloc[-1],
            'histogram': histogram.iloc[-1]
        }
    
    def detect_breakout(self, data: pd.DataFrame, lookback: int = 20) -> bool:
        """
        Detect price breakout above resistance
        
        Args:
            data: Stock price data
            lookback: Days to look back for resistance level
        
        Returns:
            True if breakout detected
        """
        if len(data) < lookback + 1:
            return False
        
        # Find resistance (highest high in lookback period)
        resistance = data['High'].iloc[-(lookback+1):-1].max()
        
        # Check if current price broke above resistance
        current_price = data['Close'].iloc[-1]
        
        return current_price > resistance * 1.02  # 2% above resistance
