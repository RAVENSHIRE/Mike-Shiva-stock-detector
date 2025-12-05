"""
Data Fetcher Utility
Handles fetching stock market data from various sources
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from typing import Optional
import time

class DataFetcher:
    """Fetch stock market data from Yahoo Finance and other sources"""
    
    def __init__(self):
        self.cache = {}
        self.cache_expiry = {}
    
    def get_stock_data(self, symbol: str, days: int = 30) -> Optional[pd.DataFrame]:
        """
        Fetch historical stock data
        
        Args:
            symbol: Stock ticker symbol
            days: Number of days of historical data
        
        Returns:
            DataFrame with OHLCV data or None if fetch fails
        """
        # Check cache
        cache_key = f"{symbol}_{days}"
        if cache_key in self.cache:
            if time.time() < self.cache_expiry.get(cache_key, 0):
                return self.cache[cache_key]
        
        try:
            # Fetch data from Yahoo Finance
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days + 10)  # Extra buffer
            
            ticker = yf.Ticker(symbol)
            data = ticker.history(start=start_date, end=end_date)
            
            if data.empty:
                return None
            
            # Cache the data
            self.cache[cache_key] = data
            self.cache_expiry[cache_key] = time.time() + 300  # 5 min cache
            
            return data
            
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None
    
    def get_current_price(self, symbol: str) -> Optional[float]:
        """Get current stock price"""
        try:
            ticker = yf.Ticker(symbol)
            data = ticker.history(period='1d')
            if not data.empty:
                return data['Close'].iloc[-1]
        except:
            pass
        return None
    
    def get_sector_performance(self) -> dict:
        """Get sector performance data"""
        # Simplified - in production would fetch real sector data
        sectors = {
            'Technology': 0.02,
            'Healthcare': 0.01,
            'Financials': -0.005,
            'Biotechnology': 0.03,
            'AI': 0.05,
            'Fintech': 0.025
        }
        return sectors
