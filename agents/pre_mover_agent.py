"""
Pre-Mover Detection Agent
Based on Moondev AI Agent Framework

This agent identifies stocks that are likely to appear on tomorrow's "Top Daily Movers" 
list BEFORE the price explodes, using multi-layer analysis including momentum, volume, 
sector rotation, and AI-powered catalyst detection.

Author: Mike-Shiva
Date: December 2025
"""

import sys
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import *
from utils.data_fetcher import DataFetcher
from utils.technical_analysis import TechnicalAnalyzer
from utils.ai_analyzer import AIAnalyzer
from utils.logger import setup_logger

logger = setup_logger(__name__)


class PreMoverDetector:
    """
    Main Pre-Mover Detection Agent
    
    Analyzes stocks using multiple layers:
    1. Momentum Conditions
    2. Volume & Liquidity Analysis
    3. Sector Rotation Logic
    4. Catalyst & Micro-catalyst Detection
    5. Red-Flag Removal
    """
    
    def __init__(self):
        """Initialize the Pre-Mover Detector"""
        self.data_fetcher = DataFetcher()
        self.technical_analyzer = TechnicalAnalyzer()
        self.ai_analyzer = AIAnalyzer()
        
        logger.info("Pre-Mover Detector initialized")
        logger.info(f"Tracking {len(IPO_WATCHLIST)} IPO candidates")
        logger.info(f"Monitoring {len(TRACK_SECTORS)} sectors")
    
    def scan_market(self, stock_list: Optional[List[str]] = None) -> List[Dict]:
        """
        Scan the market for pre-mover candidates
        
        Args:
            stock_list: Optional list of stock symbols to scan. 
                       If None, scans IPO watchlist + bellwethers
        
        Returns:
            List of candidate stocks with analysis
        """
        if stock_list is None:
            stock_list = IPO_WATCHLIST + BELLWETHER_STOCKS
        
        logger.info(f"Starting market scan for {len(stock_list)} stocks...")
        
        candidates = []
        
        for symbol in stock_list:
            try:
                analysis = self.analyze_stock(symbol)
                
                if analysis and analysis['probability_score'] >= MIN_PROBABILITY_SCORE:
                    candidates.append(analysis)
                    logger.info(f"✓ {symbol}: Pre-mover candidate (score: {analysis['probability_score']})")
                else:
                    logger.debug(f"✗ {symbol}: Below threshold")
                    
            except Exception as e:
                logger.error(f"Error analyzing {symbol}: {e}")
                continue
        
        # Sort by probability score (highest first)
        candidates.sort(key=lambda x: x['probability_score'], reverse=True)
        
        # Return top N candidates
        top_candidates = candidates[:MAX_STOCKS_PER_SCAN]
        
        logger.info(f"Scan complete. Found {len(top_candidates)} high-probability pre-movers")
        
        return top_candidates
    
    def analyze_stock(self, symbol: str) -> Optional[Dict]:
        """
        Perform comprehensive analysis on a single stock
        
        Args:
            symbol: Stock ticker symbol
        
        Returns:
            Analysis dictionary or None if analysis fails
        """
        logger.debug(f"Analyzing {symbol}...")
        
        # Fetch market data
        data = self.data_fetcher.get_stock_data(symbol, days=MOMENTUM_DAYS + VOLUME_LOOKBACK_DAYS)
        
        if data is None or len(data) < MOMENTUM_DAYS:
            logger.warning(f"{symbol}: Insufficient data")
            return None
        
        # Layer 1: Momentum Analysis
        momentum_score = self._analyze_momentum(symbol, data)
        
        # Layer 2: Volume Analysis
        volume_score = self._analyze_volume(symbol, data)
        
        # Layer 3: Sector Rotation
        sector_score = self._analyze_sector_rotation(symbol)
        
        # Layer 4: Catalyst Detection
        catalyst_score = self._detect_catalysts(symbol)
        
        # Layer 5: Red Flag Check
        has_red_flags = self._check_red_flags(symbol, data)
        
        if has_red_flags:
            logger.debug(f"{symbol}: Red flags detected, skipping")
            return None
        
        # Calculate overall probability score (weighted average)
        probability_score = (
            momentum_score * 0.30 +
            volume_score * 0.30 +
            sector_score * 0.20 +
            catalyst_score * 0.20
        )
        
        # Determine expected move window
        move_window = self._determine_move_window(momentum_score, volume_score, catalyst_score)
        
        # Get current price and key metrics
        current_price = data['Close'].iloc[-1]
        volume_change = (data['Volume'].iloc[-1] / data['Volume'].iloc[-VOLUME_LOOKBACK_DAYS:-1].mean() - 1) * 100
        
        # Compile analysis result
        analysis = {
            'symbol': symbol,
            'probability_score': round(probability_score, 1),
            'current_price': round(current_price, 2),
            'momentum_score': round(momentum_score, 1),
            'volume_score': round(volume_score, 1),
            'sector_score': round(sector_score, 1),
            'catalyst_score': round(catalyst_score, 1),
            'volume_change_pct': round(volume_change, 1),
            'move_window': move_window,
            'reasons': self._generate_reasons(momentum_score, volume_score, sector_score, catalyst_score),
            'timestamp': datetime.now().isoformat()
        }
        
        return analysis
    
    def _analyze_momentum(self, symbol: str, data) -> float:
        """Analyze momentum conditions (Layer 1)"""
        score = 0.0
        
        # Price acceleration (3-7 day)
        price_change = (data['Close'].iloc[-1] / data['Close'].iloc[-MOMENTUM_DAYS] - 1)
        if price_change >= MIN_PRICE_CHANGE:
            score += 40
        
        # Rising relative strength vs sector
        rs = self.technical_analyzer.calculate_relative_strength(symbol, data)
        if rs >= MIN_RELATIVE_STRENGTH:
            score += 30
        
        # Pre-breakout compression or coil pattern
        if self.technical_analyzer.detect_coiling_pattern(data):
            score += 30
        
        return min(score, 100)
    
    def _analyze_volume(self, symbol: str, data) -> float:
        """Analyze volume & liquidity (Layer 2)"""
        score = 0.0
        
        # Unusual volume check
        avg_volume = data['Volume'].iloc[-VOLUME_LOOKBACK_DAYS:-1].mean()
        current_volume = data['Volume'].iloc[-1]
        
        if current_volume >= avg_volume * UNUSUAL_VOLUME_THRESHOLD:
            score += 50
        
        # Accumulation signatures (higher lows + rising volume)
        if self.technical_analyzer.detect_accumulation(data, MIN_ACCUMULATION_DAYS):
            score += 50
        
        return min(score, 100)
    
    def _analyze_sector_rotation(self, symbol: str) -> float:
        """Analyze sector rotation logic (Layer 3)"""
        # Simplified sector analysis
        # In production, this would check which sectors are gaining capital
        
        # Check if stock is in a hot sector (IPO pipeline)
        if symbol in IPO_WATCHLIST:
            return 80  # High score for IPO candidates
        
        if symbol in BELLWETHER_STOCKS:
            return 70  # Good score for bellwethers
        
        return 50  # Neutral score
    
    def _detect_catalysts(self, symbol: str) -> float:
        """Detect catalysts & micro-catalysts (Layer 4)"""
        # Use AI to detect catalysts from news, filings, etc.
        catalyst_info = self.ai_analyzer.detect_catalysts(symbol)
        
        if catalyst_info:
            return catalyst_info.get('score', 50)
        
        return 50  # Neutral if no catalyst data
    
    def _check_red_flags(self, symbol: str, data) -> bool:
        """Check for red flags (Layer 5)"""
        # Dead ticker (no volume)
        if data['Volume'].iloc[-5:].mean() < MIN_LIQUIDITY:
            return True
        
        # Extreme volatility without substance
        if self.technical_analyzer.is_pump_and_dump(data):
            return True
        
        return False
    
    def _determine_move_window(self, momentum: float, volume: float, catalyst: float) -> str:
        """Determine expected move window based on scores"""
        avg_score = (momentum + volume + catalyst) / 3
        
        if avg_score >= 80:
            return "today"
        elif avg_score >= 65:
            return "tomorrow"
        else:
            return "this week"
    
    def _generate_reasons(self, momentum: float, volume: float, sector: float, catalyst: float) -> List[str]:
        """Generate human-readable reasons for the pre-mover signal"""
        reasons = []
        
        if momentum >= 70:
            reasons.append("Strong momentum acceleration detected")
        if volume >= 70:
            reasons.append("Unusual volume spike with accumulation pattern")
        if sector >= 70:
            reasons.append("In hot sector with capital inflow")
        if catalyst >= 70:
            reasons.append("Positive catalyst identified")
        
        return reasons
    
    def save_results(self, candidates: List[Dict], filename: Optional[str] = None):
        """Save analysis results to file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{REPORTS_DIR}pre_movers_{timestamp}.json"
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, 'w') as f:
            json.dump({
                'scan_time': datetime.now().isoformat(),
                'candidates_found': len(candidates),
                'candidates': candidates
            }, f, indent=2)
        
        logger.info(f"Results saved to {filename}")


def main():
    """Main execution function"""
    print("=" * 60)
    print("🔥 MIKE-SHIVA PRE-MOVER STOCK DETECTOR 🔥")
    print("=" * 60)
    print()
    
    # Initialize detector
    detector = PreMoverDetector()
    
    # Run market scan
    print("🔍 Scanning market for pre-mover candidates...")
    print()
    
    candidates = detector.scan_market()
    
    # Display results
    if candidates:
        print(f"✅ Found {len(candidates)} high-probability pre-movers:")
        print()
        
        for i, candidate in enumerate(candidates, 1):
            print(f"{i}. {candidate['symbol']} - Score: {candidate['probability_score']}/100")
            print(f"   Price: ${candidate['current_price']}")
            print(f"   Move Window: {candidate['move_window']}")
            print(f"   Reasons:")
            for reason in candidate['reasons']:
                print(f"     • {reason}")
            print()
        
        # Save results
        detector.save_results(candidates)
    else:
        print("❌ No pre-mover candidates found in this scan")
        print("   Try again later or adjust detection thresholds in config.py")
    
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
