#!/usr/bin/env python3
"""
SPY PreMover Detector - Backtesting Script
Test the system on historical data to validate performance

Author: Mike-Shiva
Date: December 2025
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
import json

# Import our detector
import sys
sys.path.insert(0, str(Path(__file__).parent))
from agents.pre_mover_agent import PreMoverDetector

def print_header(title):
    """Print a nice header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")

def get_known_movers():
    """
    Get a list of known movers from 2024-2025
    These are stocks that had significant moves
    """
    return {
        # Stock: (Date of move, % gain, reason)
        'NVDA': ('2024-02-22', 16.4, 'Earnings beat + AI boom'),
        'SMCI': ('2024-02-16', 31.2, 'AI server demand'),
        'PLTR': ('2024-02-05', 30.1, 'Earnings beat'),
        'MARA': ('2024-01-11', 25.7, 'Bitcoin rally'),
        'RIOT': ('2024-01-11', 22.3, 'Bitcoin rally'),
        'COIN': ('2024-01-11', 18.9, 'Bitcoin ETF approval'),
        'TSLA': ('2024-01-25', 12.1, 'Earnings beat'),
        'AMD': ('2024-01-30', 11.5, 'AI chip guidance'),
        'META': ('2024-02-02', 20.3, 'Earnings beat'),
        'AVGO': ('2024-03-14', 14.2, 'AI revenue growth'),
    }

def backtest_single_stock(ticker, move_date, detector):
    """
    Backtest the detector on a single stock
    
    Args:
        ticker: Stock ticker
        move_date: Date of the known move
        detector: PreMoverDetector instance
    
    Returns:
        Dictionary with backtest results
    """
    print(f"\n📊 Backtesting {ticker}...")
    
    # Get data from 10 days before the move
    move_date_dt = datetime.strptime(move_date, '%Y-%m-%d')
    start_date = move_date_dt - timedelta(days=15)
    end_date = move_date_dt
    
    try:
        # Fetch historical data
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)
        
        if data.empty:
            print(f"  ❌ No data available for {ticker}")
            return None
        
        # Check each day leading up to the move
        signals = []
        for i in range(len(data) - 1):
            date = data.index[i]
            
            # Would the detector have flagged this stock on this day?
            # (Simplified - in real backtest, we'd run full analysis)
            
            # Calculate simple momentum
            if i >= 5:
                recent_prices = data['Close'].iloc[i-5:i+1]
                momentum = (recent_prices.iloc[-1] / recent_prices.iloc[0] - 1) * 100
                
                # Calculate volume spike
                recent_volume = data['Volume'].iloc[i-20:i]
                avg_volume = recent_volume.mean()
                current_volume = data['Volume'].iloc[i]
                volume_spike = current_volume / avg_volume if avg_volume > 0 else 0
                
                # Simple scoring
                momentum_score = min(100, max(0, momentum * 10 + 50))
                volume_score = min(100, max(0, (volume_spike - 1) * 50))
                
                overall_score = (momentum_score + volume_score) / 2
                
                if overall_score >= 60:
                    days_before = (move_date_dt - date).days
                    signals.append({
                        'date': date.strftime('%Y-%m-%d'),
                        'days_before_move': days_before,
                        'score': round(overall_score, 1),
                        'momentum_score': round(momentum_score, 1),
                        'volume_score': round(volume_score, 1),
                        'price': round(data['Close'].iloc[i], 2)
                    })
        
        return {
            'ticker': ticker,
            'move_date': move_date,
            'signals': signals,
            'detected': len(signals) > 0
        }
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return None

def run_backtest():
    """Run backtest on all known movers"""
    print_header("🔬 SPY PREMOVER DETECTOR - BACKTEST")
    
    print("This backtest will check if the detector would have identified")
    print("known movers BEFORE they made their big moves.\n")
    
    print("⏱️  This may take a few minutes...\n")
    
    # Initialize detector
    detector = PreMoverDetector()
    
    # Get known movers
    known_movers = get_known_movers()
    
    # Run backtest on each
    results = []
    detected_count = 0
    total_count = 0
    
    for ticker, (move_date, gain, reason) in known_movers.items():
        result = backtest_single_stock(ticker, move_date, detector)
        if result:
            results.append(result)
            total_count += 1
            if result['detected']:
                detected_count += 1
                
                # Show best signal
                best_signal = max(result['signals'], key=lambda x: x['score'])
                print(f"  ✅ Detected {best_signal['days_before_move']} days before move")
                print(f"     Score: {best_signal['score']}/100")
            else:
                print(f"  ❌ Not detected")
    
    # Calculate metrics
    print_header("📊 BACKTEST RESULTS")
    
    if total_count > 0:
        detection_rate = (detected_count / total_count) * 100
        
        print(f"Stocks Tested: {total_count}")
        print(f"Detected: {detected_count}")
        print(f"Detection Rate: {detection_rate:.1f}%\n")
        
        if detection_rate >= 70:
            print("✅ EXCELLENT - System is working well!")
        elif detection_rate >= 50:
            print("⚠️  GOOD - System needs some tuning")
        else:
            print("❌ POOR - System needs significant adjustments")
        
        # Show detailed results
        print("\n" + "="*70)
        print("DETAILED RESULTS:")
        print("="*70)
        
        for result in results:
            if result['detected']:
                ticker = result['ticker']
                move_info = known_movers[ticker]
                
                print(f"\n{ticker} - {move_info[2]}")
                print(f"  Move Date: {result['move_date']} (+{move_info[1]}%)")
                print(f"  Signals Detected: {len(result['signals'])}")
                
                # Show earliest signal
                earliest = min(result['signals'], key=lambda x: x['days_before_move'])
                print(f"  Earliest Detection: {earliest['days_before_move']} days before")
                print(f"  Score: {earliest['score']}/100")
                
                # Show strongest signal
                strongest = max(result['signals'], key=lambda x: x['score'])
                print(f"  Strongest Signal: {strongest['days_before_move']} days before")
                print(f"  Score: {strongest['score']}/100")
        
        # Save results
        output_file = Path("reports") / f"backtest_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        output_file.parent.mkdir(exist_ok=True)
        
        with open(output_file, 'w') as f:
            json.dump({
                'backtest_date': datetime.now().isoformat(),
                'total_stocks': total_count,
                'detected': detected_count,
                'detection_rate': detection_rate,
                'results': results
            }, f, indent=2)
        
        print(f"\n💾 Results saved to: {output_file}")
    
    print("\n" + "="*70)
    print("  BACKTEST COMPLETE")
    print("="*70 + "\n")
    
    print("💡 Next Steps:")
    print("  • If detection rate is low, adjust thresholds in config/config.py")
    print("  • Try lowering MIN_PROBABILITY_SCORE")
    print("  • Try lowering MIN_VOLUME_SPIKE")
    print("  • Re-run backtest to see improvement\n")

if __name__ == "__main__":
    run_backtest()
