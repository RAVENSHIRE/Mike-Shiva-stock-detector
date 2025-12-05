# 🚀 SPY PreMover Detector

**Identify stocks BEFORE they appear on daily movers lists using AI-powered multi-layer analysis.**

Detect pre-mover opportunities in real-time by analyzing momentum, volume, sector rotation, and AI-detected catalysts. Built for the 2025-2026 IPO boom in AI, Fintech, and Biotech.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-412991.svg)](https://openai.com/)

---

## ✨ Key Features

- **🎯 5-Layer Detection System:** Momentum, Volume, Sector Rotation, AI Catalysts, Red-Flag Removal
- **🤖 AI-Powered Analysis:** Uses GPT-4.1-mini to detect micro-catalysts from news and filings
- **📊 2025-2026 IPO Focus:** Pre-configured watchlist for upcoming IPOs (Databricks, Kraken, Cerebras)
- **⚡ Automated Daily Scans:** Run before market open to catch opportunities early
- **📈 Backtesting Ready:** Validate strategies on historical data
- **🔔 Smart Alerts:** Get notified of high-probability pre-movers

---

## 🎯 What is a "Pre-Mover"?

A **pre-mover** is a stock showing early signs of a significant price move BEFORE it appears on popular screeners and movers lists. By the time a stock shows up on "top gainers," you're already late.

**SPY PreMover Detector** identifies these opportunities by analyzing:
- **Momentum acceleration** (3-7 day price patterns)
- **Unusual volume** (150%+ of average)
- **Sector strength** (capital flowing into hot sectors)
- **Positive catalysts** (FDA approvals, partnerships, IPO news)
- **Clean charts** (filters out pump-and-dumps)

---

## 🚀 Quick Start (10 Minutes)

### 1. Clone the Repository
```bash
git clone https://github.com/RAVENSHIRE/SPY-PreMover-Detector.git
cd SPY-PreMover-Detector
```

### 2. Set Up Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure API Keys
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### 4. Run Your First Scan
```bash
python run_daily_scan.py
```

**That's it!** You'll see a ranked list of pre-mover candidates with detailed analysis.

---

## 📊 Example Output

```
🚀 SPY PRE-MOVER DETECTOR - DAILY SCAN 🚀
======================================================================
📅 Date: 2025-12-05 08:00:00
🎯 Target: Identify stocks BEFORE they blast
📊 Scanning: 12 IPO candidates + 3 bellwethers
======================================================================

✅ FOUND 3 HIGH-PROBABILITY PRE-MOVERS

──────────────────────────────────────────────────────────────────────
#1. DTBK - PROBABILITY: 85/100
──────────────────────────────────────────────────────────────────────
💰 Current Price: $150.25
📈 Volume Change: +210.5%
⏰ Expected Move: TODAY

📊 Breakdown:
   • Momentum Score:  80/100
   • Volume Score:    90/100
   • Sector Score:    80/100
   • Catalyst Score:  90/100

🔥 Key Reasons:
   ✓ Strong momentum acceleration detected
   ✓ Unusual volume spike with accumulation pattern
   ✓ In hot sector with capital inflow
   ✓ Positive catalyst: "Databricks announces new AI platform"
```

---

## 📚 Documentation

- **[Quick Start Guide](./QUICKSTART.md)** - Get running in 10 minutes
- **[60-Day Development Plan](./docs/PRODUCT_DEVELOPMENT_PLAN.md)** - Build it yourself from scratch
- **[Project Summary](./docs/PROJECT_SUMMARY.md)** - Detailed component breakdown

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Language** | Python 3.11+ | Core development |
| **Data Analysis** | pandas, numpy | Data manipulation |
| **Market Data** | yfinance | Free stock data |
| **AI** | OpenAI GPT-4.1-mini | Catalyst detection |
| **Version Control** | Git, GitHub | Code management |

---

## ⚖️ Disclaimer

**This is NOT financial advice. For educational purposes only.**

Never risk money you cannot afford to lose. Always paper trade first. Do your own research.

---

## 📄 License

MIT License - Free to use and modify

---

**Built by Mike-Shiva with Manus AI | December 2025**
