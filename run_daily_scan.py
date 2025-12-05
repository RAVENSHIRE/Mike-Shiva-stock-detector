#!/usr/bin/env python3
"""
Daily Pre-Mover Scanner
Run this script every morning before market open to identify potential movers

Usage:
    python run_daily_scan.py
    
    Or schedule with cron:
    0 8 * * 1-5 cd /path/to/Mike-Shiva-stock-detector && python run_daily_scan.py
"""

import sys
import os
from datetime import datetime

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.pre_mover_agent import PreMoverDetector
from config.config import *

def print_banner():
    """Print welcome banner"""
    print("\n" + "=" * 70)
    print("🚀 MIKE-SHIVA PRE-MOVER STOCK DETECTOR - DAILY SCAN 🚀")
    print("=" * 70)
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🎯 Target: Identify stocks BEFORE they blast")
    print(f"📊 Scanning: {len(IPO_WATCHLIST)} IPO candidates + {len(BELLWETHER_STOCKS)} bellwethers")
    print("=" * 70)
    print()

def print_results(candidates):
    """Print scan results in a nice format"""
    if not candidates:
        print("❌ NO HIGH-PROBABILITY PRE-MOVERS FOUND")
        print("\n💡 Tips:")
        print("   • Try lowering MIN_PROBABILITY_SCORE in config.py")
        print("   • Check if market conditions are favorable")
        print("   • Scan again in a few hours")
        return
    
    print(f"✅ FOUND {len(candidates)} HIGH-PROBABILITY PRE-MOVERS\n")
    
    for i, stock in enumerate(candidates, 1):
        print(f"{'─' * 70}")
        print(f"#{i}. {stock['symbol']} - PROBABILITY: {stock['probability_score']}/100")
        print(f"{'─' * 70}")
        print(f"💰 Current Price: ${stock['current_price']}")
        print(f"📈 Volume Change: {stock['volume_change_pct']:+.1f}%")
        print(f"⏰ Expected Move: {stock['move_window'].upper()}")
        print(f"\n📊 Breakdown:")
        print(f"   • Momentum Score:  {stock['momentum_score']}/100")
        print(f"   • Volume Score:    {stock['volume_score']}/100")
        print(f"   • Sector Score:    {stock['sector_score']}/100")
        print(f"   • Catalyst Score:  {stock['catalyst_score']}/100")
        
        if stock.get('reasons'):
            print(f"\n🔥 Key Reasons:")
            for reason in stock['reasons']:
                print(f"   ✓ {reason}")
        
        print()
    
    print("=" * 70)
    print("\n⚠️  IMPORTANT REMINDERS:")
    print("   1. This is NOT financial advice - do your own research")
    print("   2. Check the 4 early-blast signs before entering:")
    print("      • Volume spike BEFORE price move")
    print("      • Coiling pattern (tight range)")
    print("      • Low float + catalyst")
    print("      • Sector hotness")
    print("   3. Enter at the 'power zone' - NOT after the spike")
    print("   4. Set stop-loss and profit targets BEFORE entering")
    print("=" * 70)
    print()

def main():
    """Main execution"""
    print_banner()
    
    # Initialize detector
    print("🔧 Initializing Pre-Mover Detector...")
    detector = PreMoverDetector()
    print("✓ Detector ready\n")
    
    # Run scan
    print("🔍 Scanning market...\n")
    candidates = detector.scan_market()
    
    # Print results
    print_results(candidates)
    
    # Save results
    if candidates:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/daily_scan_{timestamp}.json"
        detector.save_results(candidates, filename)
        print(f"💾 Results saved to: {filename}\n")
    
    print("✅ Daily scan complete!\n")

if __name__ == "__main__":
    main()
