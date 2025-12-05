# ⏰ Quick Start Guide for 8 AM Market Open

**You have 5 hours. Let's get you ready! 🚀**

---

## 🎯 Goal

Be fully operational by 8 AM tomorrow to scan for pre-mover stocks before market open.

---

## ⚡ 30-Minute Setup (Do This NOW)

### Step 1: Clone & Setup (10 minutes)

```bash
# Clone the repository
git clone https://github.com/RAVENSHIRE/SPY-PreMover-Detector.git
cd SPY-PreMover-Detector

# Run automated setup
chmod +x setup.sh
./setup.sh
```

**What this does:**
- Creates virtual environment
- Installs all dependencies
- Creates necessary directories
- Verifies everything works

---

### Step 2: Get OpenAI API Key (5 minutes)

1. Go to: https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)

**Cost:** ~$0.10-0.50 per day for AI analysis

---

### Step 3: Configure (5 minutes)

```bash
# Edit .env file
nano .env  # or use any text editor
```

Add your API key:
```
OPENAI_API_KEY=sk-your-actual-key-here
```

Save and exit (Ctrl+X, then Y, then Enter)

---

### Step 4: Test Run (10 minutes)

```bash
# Activate virtual environment
source venv/bin/activate

# Run your first scan
python run_daily_scan.py
```

**Expected output:**
```
🚀 SPY PRE-MOVER DETECTOR - DAILY SCAN 🚀
======================================================================
📅 Date: 2025-12-05 03:30:00
🎯 Target: Identify stocks BEFORE they blast
📊 Scanning: 12 IPO candidates + 3 bellwethers
======================================================================

✅ FOUND 2 HIGH-PROBABILITY PRE-MOVERS
...
```

**If you see this, YOU'RE READY! ✅**

---

## 📚 Learn the System (Optional - 20 minutes)

```bash
# Run interactive tutorial
python tutorial.py
```

This walks you through:
- How the code works
- What each score means
- How to adjust parameters
- Daily routine

---

## 🔬 Validate with Backtest (Optional - 15 minutes)

```bash
# Run backtest on historical data
python backtest.py
```

This tests the detector on known movers from 2024-2025 to see if it would have caught them.

**Good result:** 60%+ detection rate

---

## 📅 Your 8 AM Routine (5 minutes daily)

### 7:55 AM - Activate Environment
```bash
cd SPY-PreMover-Detector
source venv/bin/activate
```

### 8:00 AM - Run Scan
```bash
python run_daily_scan.py
```

### 8:02 AM - Review Results
- Look at top 5 candidates
- Note the scores and reasons
- Check charts on TradingView/Yahoo Finance

### 8:05 AM - Research Top Picks
- Google the catalyst mentioned
- Verify news is real
- Check sector strength
- Look at chart pattern

### 8:10 AM - Make Watchlist
- Add top 2-3 to your broker's watchlist
- Set price alerts
- Plan entry/exit points

### 9:30 AM - Market Open
- Monitor your watchlist
- Look for entry opportunities
- Use stop losses!

---

## 🔧 Troubleshooting

### "No candidates found"
**Solution:** Lower the thresholds

```bash
# Edit config
nano config/config.py
```

Change:
```python
MIN_PROBABILITY_SCORE = 50  # Was 60
MIN_MOMENTUM_SCORE = 50     # Was 60
MIN_VOLUME_SPIKE = 1.3      # Was 1.5
```

### "Too many candidates (20+)"
**Solution:** Raise the thresholds

```python
MIN_PROBABILITY_SCORE = 70  # Was 60
MIN_MOMENTUM_SCORE = 70     # Was 60
MIN_VOLUME_SPIKE = 2.0      # Was 1.5
```

### "OpenAI API error"
**Solution:** Check your API key

```bash
# Verify key is set
cat .env | grep OPENAI_API_KEY

# Should show: OPENAI_API_KEY=sk-...
```

### "Module not found"
**Solution:** Reinstall dependencies

```bash
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🎯 What to Expect Tomorrow

### Realistic Expectations

**Good Day:**
- 2-5 pre-mover candidates
- 1-2 actually move significantly
- Catch 1 early for profit

**Average Day:**
- 0-2 candidates
- May not move immediately
- Keep on watchlist for next day

**Bad Day:**
- 0 candidates
- Market is choppy/sideways
- No clear opportunities

**Remember:** Not every day will have pre-movers. That's normal!

---

## 💡 Pro Tips

### For Best Results

1. **Run BEFORE market open** (7:30-8:30 AM ET)
   - Fresh data
   - Time to research
   - Beat the crowd

2. **Always verify the catalyst**
   - Google the news
   - Check company website
   - Verify it's real and recent

3. **Check the chart yourself**
   - Look for clean breakout patterns
   - Avoid stocks in downtrends
   - Confirm volume is unusual

4. **Use stop losses**
   - Set 5-7% below entry
   - Protect your capital
   - Live to trade another day

5. **Take profits**
   - Don't be greedy
   - 10-15% gains are excellent
   - Partial profits at resistance

### Risk Management

- **Never risk more than 2% per trade**
- **Start with paper trading** (practice account)
- **Keep a trading journal**
- **Review what worked/didn't work**

---

## 📊 Understanding Scores

### Probability Score (0-100)

- **80-100:** 🔥 STRONG - High confidence pre-mover
- **70-79:** ✅ GOOD - Solid candidate, do research
- **60-69:** ⚠️  OK - Possible, needs confirmation
- **<60:** ❌ WEAK - Filtered out

### What Each Layer Means

**Momentum (80+):** Price is accelerating, building energy

**Volume (80+):** Unusual buying, smart money accumulating

**Sector (80+):** Hot sector, capital flowing in

**Catalyst (80+):** Positive news detected by AI

---

## 🚨 Important Reminders

### This is NOT

- ❌ A guaranteed profit system
- ❌ Financial advice
- ❌ A replacement for research
- ❌ A "get rich quick" scheme

### This IS

- ✅ A screening tool
- ✅ An early warning system
- ✅ A starting point for research
- ✅ A way to find opportunities faster

---

## 📞 Getting Help

### If Something Goes Wrong

1. **Check the tutorial:**
   ```bash
   python tutorial.py
   ```

2. **Read the docs:**
   ```bash
   cat docs/PRODUCT_DEVELOPMENT_PLAN.md
   ```

3. **Check GitHub Issues:**
   https://github.com/RAVENSHIRE/SPY-PreMover-Detector/issues

4. **Community:**
   - r/algotrading
   - r/daytrading
   - Moondev YouTube

---

## ✅ Pre-8AM Checklist

Before you go to sleep tonight, make sure:

- [ ] Ran `./setup.sh` successfully
- [ ] Added OPENAI_API_KEY to .env
- [ ] Ran test scan and got results
- [ ] Understand what the scores mean
- [ ] Know your 8 AM routine
- [ ] Set alarm for 7:55 AM
- [ ] Have broker account ready
- [ ] Know your risk management rules

---

## 🎉 You're Ready!

**Tomorrow at 8 AM:**
1. Run the scan (5 min)
2. Review results (5 min)
3. Research top picks (10 min)
4. Add to watchlist (2 min)
5. Wait for market open (9:30 AM)

**Total time: ~22 minutes**

---

## 🌟 Final Thoughts

You now have a powerful tool to identify pre-mover stocks. Use it wisely:

- **Be patient** - Not every day has opportunities
- **Be disciplined** - Follow your rules
- **Be realistic** - Small consistent gains > home runs
- **Be careful** - Protect your capital

**Good luck tomorrow! 🚀**

---

*Created by Mike-Shiva with Manus AI | December 2025*
