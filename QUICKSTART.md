# ⚡ Quick Start Guide

Get the Mike-Shiva Stock Detector running in **under 10 minutes**.

---

## 🚀 Step 1: Clone the Repository

```bash
git clone https://github.com/RAVENSHIRE/Mike-Shiva-stock-detector.git
cd Mike-Shiva-stock-detector
```

---

## 🐍 Step 2: Set Up Python Environment

**Option A: Using venv (recommended)**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Option B: Using conda**
```bash
conda create -n stock_detector python=3.11
conda activate stock_detector
```

---

## 📦 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- pandas & numpy (data analysis)
- yfinance (market data)
- openai (AI analysis)
- python-dotenv (environment variables)
- And more...

---

## 🔑 Step 4: Set Up API Keys

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Get your **OpenAI API key** from: https://platform.openai.com/api-keys

3. Edit `.env` and add your key:
```dotenv
OPENAI_API_KEY=sk-your-actual-key-here
```

> **Note:** The OpenAI API key is required for AI-powered catalyst detection. Without it, the system will still work but with reduced functionality.

---

## 🎯 Step 5: Run Your First Scan

```bash
python run_daily_scan.py
```

You should see output like:

```
🚀 MIKE-SHIVA PRE-MOVER STOCK DETECTOR - DAILY SCAN 🚀
======================================================================
📅 Date: 2025-12-05 08:00:00
🎯 Target: Identify stocks BEFORE they blast
📊 Scanning: 12 IPO candidates + 3 bellwethers
======================================================================

🔧 Initializing Pre-Mover Detector...
✓ Detector ready

🔍 Scanning market...

✅ FOUND 2 HIGH-PROBABILITY PRE-MOVERS
...
```

---

## 🎨 Step 6: Customize Your Watchlist

Edit `config/config.py` to add your own stocks:

```python
# Add your own stocks to the IPO watchlist
IPO_WATCHLIST = [
    'DTBK',  # Databricks
    'YOUR_STOCK_HERE',  # Add your picks
]

# Or modify the bellwether list
BELLWETHER_STOCKS = [
    'NVDA',  # Nvidia
    'YOUR_FAVORITE_STOCK',
]
```

---

## 📊 Step 7: View Results

Scan results are saved to `reports/` directory as JSON files:

```bash
cat reports/daily_scan_20251205_080000.json
```

---

## 🎓 Step 8: Start the 60-Day Gameplan

Read the complete gameplan:

```bash
cat docs/60_DAY_GAMEPLAN.md
```

Or open it in your favorite markdown viewer.

---

## 🆘 Troubleshooting

### "ModuleNotFoundError: No module named 'yfinance'"
**Solution:** Make sure you activated your virtual environment and ran `pip install -r requirements.txt`

### "OpenAI API key not found"
**Solution:** Check that your `.env` file exists and contains `OPENAI_API_KEY=your-key-here`

### "No pre-mover candidates found"
**Solution:** This is normal! Not every scan will find candidates. Try:
- Lowering `MIN_PROBABILITY_SCORE` in `config/config.py`
- Running the scan at different times of day
- Adding more stocks to your watchlist

### "Rate limit exceeded"
**Solution:** Yahoo Finance has rate limits. Wait a few minutes and try again.

---

## 🎯 Next Steps

1. **Read the full README:** `README.md`
2. **Review the 60-day gameplan:** `docs/60_DAY_GAMEPLAN.md`
3. **Start tracking your progress:** `docs/DAILY_TRACKER.md`
4. **Explore the code:** Start with `agents/pre_mover_agent.py`
5. **Join the community:** Share your results and learnings!

---

## 📚 Additional Resources

- **Moondev YouTube:** https://youtube.com/@moondevonyt
- **Yahoo Finance API Docs:** https://pypi.org/project/yfinance/
- **OpenAI API Docs:** https://platform.openai.com/docs/
- **Python for Finance:** https://www.udemy.com/course/python-for-finance-and-trading-algorithms/

---

**You're all set! Happy scanning! 🔥**

*If you found this helpful, give the repo a ⭐ on GitHub!*
