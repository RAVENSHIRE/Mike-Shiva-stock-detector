#!/usr/bin/env python3
"""
SPY PreMover Detector - Interactive Tutorial
Learn how the system works step-by-step

Author: Mike-Shiva
Date: December 2025
"""

import os
import sys
from pathlib import Path

def print_header(title):
    """Print a nice header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")

def wait_for_user():
    """Wait for user to press Enter"""
    input("\n👉 Press Enter to continue...")

def tutorial_intro():
    """Introduction to the tutorial"""
    print_header("🎓 WELCOME TO SPY PREMOVER DETECTOR TUTORIAL")
    
    print("This interactive tutorial will walk you through:")
    print("  1. Understanding the code structure")
    print("  2. How the 5-layer detection works")
    print("  3. Running your first scan")
    print("  4. Interpreting results")
    print("  5. Adjusting parameters")
    print("\n⏱️  Estimated time: 15-20 minutes")
    
    wait_for_user()

def tutorial_structure():
    """Explain the code structure"""
    print_header("📁 STEP 1: CODE STRUCTURE")
    
    print("The project is organized like this:\n")
    print("SPY-PreMover-Detector/")
    print("├── agents/")
    print("│   └── pre_mover_agent.py    ← 🎯 MAIN DETECTION LOGIC")
    print("├── config/")
    print("│   └── config.py              ← ⚙️  ALL SETTINGS HERE")
    print("├── utils/")
    print("│   ├── data_fetcher.py        ← 📊 Gets stock data")
    print("│   ├── technical_analysis.py  ← 📈 Calculates indicators")
    print("│   └── ai_analyzer.py         ← 🤖 AI catalyst detection")
    print("└── run_daily_scan.py          ← ▶️  RUN THIS DAILY")
    
    print("\n💡 Key Insight:")
    print("   Everything flows through pre_mover_agent.py")
    print("   It calls the utils to get data and analyze it")
    
    wait_for_user()

def tutorial_5_layers():
    """Explain the 5-layer detection system"""
    print_header("🎯 STEP 2: THE 5-LAYER DETECTION SYSTEM")
    
    print("The detector analyzes stocks using 5 layers:\n")
    
    print("LAYER 1: MOMENTUM ANALYSIS")
    print("  • Detects 3-7 day price acceleration")
    print("  • Looks for 'coiling' patterns (consolidation before breakout)")
    print("  • Calculates relative strength vs sector")
    print("  • Score: 0-100 (higher = stronger momentum)\n")
    
    print("LAYER 2: VOLUME ANALYSIS")
    print("  • Identifies unusual volume spikes (>150% of average)")
    print("  • Detects accumulation patterns (smart money buying)")
    print("  • Filters out low-liquidity stocks")
    print("  • Score: 0-100 (higher = more unusual volume)\n")
    
    print("LAYER 3: SECTOR ROTATION")
    print("  • Tracks which sectors are hot (AI, Fintech, Biotech)")
    print("  • Identifies capital flow into sectors")
    print("  • Boosts stocks in trending sectors")
    print("  • Score: 0-100 (higher = hotter sector)\n")
    
    print("LAYER 4: AI CATALYST DETECTION")
    print("  • Uses GPT-4.1 to analyze news and filings")
    print("  • Detects micro-catalysts (FDA approvals, partnerships)")
    print("  • Identifies positive sentiment")
    print("  • Score: 0-100 (higher = stronger catalyst)\n")
    
    print("LAYER 5: RED-FLAG REMOVAL")
    print("  • Filters out pump-and-dump schemes")
    print("  • Removes dead/delisted tickers")
    print("  • Checks for dilution events")
    print("  • Binary: PASS or FAIL\n")
    
    print("🎯 FINAL SCORE:")
    print("   Average of all 4 scores (if passes red-flag check)")
    print("   Only stocks scoring 60+ are considered 'pre-movers'")
    
    wait_for_user()

def tutorial_config():
    """Show how to configure the system"""
    print_header("⚙️  STEP 3: CONFIGURATION")
    
    print("All settings are in config/config.py\n")
    
    print("KEY SETTINGS YOU CAN ADJUST:\n")
    
    print("1. DETECTION THRESHOLDS")
    print("   MIN_MOMENTUM_SCORE = 60")
    print("   MIN_VOLUME_SPIKE = 1.5  # 150% of average")
    print("   MIN_PROBABILITY_SCORE = 60")
    print("   → Lower these to find MORE candidates (less strict)")
    print("   → Raise these to find FEWER candidates (more strict)\n")
    
    print("2. WATCHLIST")
    print("   IPO_WATCHLIST = ['DTBK', 'KRKN', 'CRBR', ...]")
    print("   → Add your own stock tickers here\n")
    
    print("3. API KEYS")
    print("   Set in .env file:")
    print("   OPENAI_API_KEY=your-key-here\n")
    
    print("💡 Pro Tip:")
    print("   Start with default settings, then adjust based on results")
    
    wait_for_user()

def tutorial_first_scan():
    """Guide through running first scan"""
    print_header("▶️  STEP 4: RUNNING YOUR FIRST SCAN")
    
    print("Let's run a scan right now!\n")
    
    print("The scan will:")
    print("  1. Fetch data for all watchlist stocks")
    print("  2. Run 5-layer analysis on each")
    print("  3. Score and rank candidates")
    print("  4. Display top pre-movers")
    print("  5. Save results to reports/\n")
    
    run_now = input("Run scan now? (y/n): ").strip().lower()
    
    if run_now == 'y':
        print("\n🚀 Starting scan...\n")
        print("="*70)
        
        # Import and run the scanner
        try:
            from run_daily_scan import main as run_scan
            run_scan()
        except Exception as e:
            print(f"\n❌ Error running scan: {e}")
            print("\nMake sure you've:")
            print("  1. Run ./setup.sh")
            print("  2. Set OPENAI_API_KEY in .env")
            print("  3. Installed all dependencies")
    else:
        print("\n✅ Skipped scan for now")
        print("   Run it later with: python run_daily_scan.py")
    
    wait_for_user()

def tutorial_interpret_results():
    """Explain how to interpret results"""
    print_header("📊 STEP 5: INTERPRETING RESULTS")
    
    print("When you run a scan, you'll see output like this:\n")
    
    print("──────────────────────────────────────────────────────────")
    print("#1. DTBK - PROBABILITY: 85/100")
    print("──────────────────────────────────────────────────────────")
    print("💰 Current Price: $150.25")
    print("📈 Volume Change: +210.5%")
    print("⏰ Expected Move: TODAY")
    print("")
    print("📊 Breakdown:")
    print("   • Momentum Score:  80/100  ← Price accelerating")
    print("   • Volume Score:    90/100  ← Unusual volume spike")
    print("   • Sector Score:    80/100  ← Hot sector (AI)")
    print("   • Catalyst Score:  90/100  ← Positive news detected")
    print("")
    print("🔥 Key Reasons:")
    print("   ✓ Strong momentum acceleration detected")
    print("   ✓ Unusual volume spike with accumulation pattern")
    print("   ✓ In hot sector with capital inflow")
    print("   ✓ Positive catalyst: 'Databricks announces new AI platform'")
    print("──────────────────────────────────────────────────────────\n")
    
    print("HOW TO USE THIS:\n")
    
    print("✅ HIGH PROBABILITY (80-100):")
    print("   → Strong candidate, do further research")
    print("   → Check the chart yourself")
    print("   → Verify the catalyst is real")
    print("   → Consider entering a position\n")
    
    print("⚠️  MEDIUM PROBABILITY (60-79):")
    print("   → Potential candidate, needs more confirmation")
    print("   → Watch for additional signals")
    print("   → May be early, keep on watchlist\n")
    
    print("❌ LOW PROBABILITY (<60):")
    print("   → Not a pre-mover yet")
    print("   → System filtered it out")
    
    print("\n💡 Remember:")
    print("   This is a SCREENING TOOL, not a buy signal")
    print("   Always do your own research!")
    print("   Never risk more than you can afford to lose")
    
    wait_for_user()

def tutorial_adjustments():
    """Show how to adjust parameters"""
    print_header("🔧 STEP 6: ADJUSTING PARAMETERS")
    
    print("Based on your results, you can fine-tune the system:\n")
    
    print("PROBLEM: Too many candidates (20+)")
    print("SOLUTION: Make it more strict")
    print("  • Increase MIN_PROBABILITY_SCORE to 70")
    print("  • Increase MIN_MOMENTUM_SCORE to 70")
    print("  • Increase MIN_VOLUME_SPIKE to 2.0\n")
    
    print("PROBLEM: No candidates found")
    print("SOLUTION: Make it less strict")
    print("  • Decrease MIN_PROBABILITY_SCORE to 50")
    print("  • Decrease MIN_MOMENTUM_SCORE to 50")
    print("  • Decrease MIN_VOLUME_SPIKE to 1.3\n")
    
    print("PROBLEM: Too many false positives")
    print("SOLUTION: Focus on quality")
    print("  • Enable AI catalyst detection (costs API credits)")
    print("  • Increase sector score weight")
    print("  • Add more red-flag filters\n")
    
    print("📝 To adjust:")
    print("  1. Open config/config.py")
    print("  2. Change the values")
    print("  3. Save the file")
    print("  4. Run scan again")
    
    wait_for_user()

def tutorial_daily_routine():
    """Explain the daily routine"""
    print_header("📅 STEP 7: DAILY ROUTINE")
    
    print("Here's your daily workflow:\n")
    
    print("🌅 BEFORE MARKET OPEN (7:30-8:00 AM ET)")
    print("  1. Run: python run_daily_scan.py")
    print("  2. Review top 5 candidates")
    print("  3. Do quick research on each")
    print("  4. Check charts and news")
    print("  5. Add to watchlist\n")
    
    print("📈 DURING MARKET HOURS (9:30 AM - 4:00 PM ET)")
    print("  1. Monitor your watchlist")
    print("  2. Look for entry points")
    print("  3. Set stop losses")
    print("  4. Take profits on moves\n")
    
    print("🌙 AFTER MARKET CLOSE (4:00-5:00 PM ET)")
    print("  1. Review what worked/didn't work")
    print("  2. Adjust parameters if needed")
    print("  3. Check for after-hours news")
    print("  4. Prepare for tomorrow\n")
    
    print("⏱️  Total time: ~30 minutes per day")
    
    wait_for_user()

def tutorial_next_steps():
    """Show next steps"""
    print_header("🎯 NEXT STEPS")
    
    print("You're now ready to use SPY PreMover Detector!\n")
    
    print("IMMEDIATE ACTIONS:")
    print("  ✅ Run your first scan: python run_daily_scan.py")
    print("  ✅ Review the results")
    print("  ✅ Adjust config if needed")
    print("  ✅ Set up for tomorrow 8 AM\n")
    
    print("LEARNING MORE:")
    print("  📖 Read docs/PRODUCT_DEVELOPMENT_PLAN.md")
    print("  📖 Study the code in agents/pre_mover_agent.py")
    print("  📖 Join trading communities (r/algotrading)\n")
    
    print("ADVANCED:")
    print("  🔬 Run backtests on historical data")
    print("  🔧 Add custom indicators")
    print("  🤖 Train your own AI models")
    print("  📊 Build a dashboard\n")
    
    print("⚠️  REMEMBER:")
    print("  • This is a tool, not a crystal ball")
    print("  • Always paper trade first")
    print("  • Never risk more than you can afford to lose")
    print("  • Do your own research")
    
    print("\n" + "="*70)
    print("  🎉 TUTORIAL COMPLETE! GOOD LUCK! 🚀")
    print("="*70 + "\n")

def main():
    """Run the tutorial"""
    tutorial_intro()
    tutorial_structure()
    tutorial_5_layers()
    tutorial_config()
    tutorial_first_scan()
    tutorial_interpret_results()
    tutorial_adjustments()
    tutorial_daily_routine()
    tutorial_next_steps()

if __name__ == "__main__":
    main()
