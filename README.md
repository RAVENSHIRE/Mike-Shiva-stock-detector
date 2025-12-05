# 🔥 Mike-Shiva Stock Detector 🔥

**A pre-mover stock detection system designed to identify stocks that are about to blast—*before* they show up on the “Daily Movers” list.**

This project was built as part of a comprehensive 60-day gameplan to combine advanced algorithmic trading development with a rigorous academic schedule. It leverages the Moondev AI Agent framework to create a powerful, automated, and intelligent stock scanning system.

---

![Project Banner](https://i.imgur.com/your-banner-image.png)  <!-- Placeholder for a cool banner image -->

## 🚀 Key Features

- **Multi-Layer Analysis:** Goes beyond simple price checks by using a sophisticated multi-layer analysis:
  - **Momentum Conditions:** Detects 3-7 day price acceleration and pre-breakout compression patterns.
  - **Volume & Liquidity:** Identifies unusual volume spikes and accumulation signatures.
  - **Sector Rotation Logic:** Tracks capital flow into hot sectors like AI, Fintech, and Biotech.
  - **AI-Powered Catalysts:** Uses an LLM to detect micro-catalysts from news, filings, and social sentiment.
  - **Red-Flag Removal:** Automatically filters out dead tickers and potential pump-and-dumps.

- **2025-2026 IPO Focus:** Includes a built-in watchlist of high-potential upcoming IPOs in key growth sectors.

- **Moondev Framework:** Built on the principles of the Moondev AI Agent ecosystem for modularity and extensibility.

- **Automated Daily Scans:** Run the scanner daily before market open to get a fresh list of pre-mover candidates.

- **Configurable & Extensible:** Easily configure thresholds, watchlists, and API keys. The modular structure makes it easy to add new data sources or analysis layers.

- **Comprehensive Gameplan:** Comes with a full 60-day plan to guide you from setup to production, while also balancing academic studies.

---

## 🛠️ Technology Stack

- **Core Language:** Python 3.11+
- **Data Analysis:** pandas, numpy
- **Market Data:** yfinance (Yahoo Finance), Alpha Vantage
- **AI Analysis:** OpenAI (GPT-4.1-mini or newer)
- **Technical Indicators:** Custom-built + optional TA-Lib
- **Development:** VS Code, Git, GitHub
- **Virtual Environment:** venv or conda

---

## ⚙️ Setup & Installation

Follow these steps to get the Mike-Shiva Stock Detector up and running in minutes.

### 1. Clone the Repository

```bash
gh repo create Mike-Shiva-stock-detector --public --clone
cd Mike-Shiva-stock-detector
```

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies.

**Using `venv` (recommended):**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Using `conda`:**
```bash
conda create -n stock_detector python=3.11
conda activate stock_detector
```

### 3. Install Dependencies

Install all required packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Copy the example environment file and add your API keys.

```bash
cp .env.example .env
```

Now, open the `.env` file and add your **OpenAI API key**. You can get a free key from the [OpenAI Platform](https://platform.openai.com/api-keys).

```dotenv
# .env
OPENAI_API_KEY=your_openai_api_key_here
ALPHA_VANTAGE_KEY=your_alpha_vantage_key_here # Optional
```

---

## 📈 How to Use

Running the daily scan is simple. Just execute the `run_daily_scan.py` script from your terminal.

```bash
python run_daily_scan.py
```

This will trigger the `PreMoverDetector` agent, which will:
1.  Fetch the latest market data for the configured watchlist.
2.  Run the multi-layer analysis on each stock.
3.  Score each stock based on its 
pre-mover potential.
4.  Display a ranked list of the top candidates.
5.  Save the full analysis to a JSON file in the `reports/` directory.

### Example Output

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
   ✓ Positive catalyst identified: "Databricks announces new AI platform"

──────────────────────────────────────────────────────────────────────
#2. KRKN - PROBABILITY: 78/100
──────────────────────────────────────────────────────────────────────
...
```

---

## 🏗️ System Architecture

The system is designed with a modular architecture, making it easy to understand, maintain, and extend.

```
Mike-Shiva-stock-detector/
├── agents/                  # Core AI agents (PreMoverDetector)
│   └── pre_mover_agent.py
├── config/                  # Configuration files
│   └── config.py
├── data/                    # Raw and processed data (not in git)
├── docs/                    # Documentation and gameplan
│   ├── 60_DAY_GAMEPLAN.md
│   └── DAILY_TRACKER.md
├── notebooks/               # Jupyter notebooks for analysis
├── reports/                 # Daily scan reports (JSON)
├── strategies/              # Future: Different trading strategies
├── tests/                   # Unit and integration tests
├── utils/                   # Reusable utility modules
│   ├── data_fetcher.py
│   ├── technical_analysis.py
│   ├── ai_analyzer.py
│   └── logger.py
├── .env.example             # Example environment variables
├── .gitignore               # Files to ignore in git
├── README.md                # This file
├── requirements.txt         # Python dependencies
└── run_daily_scan.py        # Main executable script
```

---

## 🗺️ The 60-Day Gameplan

This repository is the direct result of the **60-Day Gameplan**, a detailed schedule designed to balance this project with a full university course load. The full plan can be found in the `docs/` directory.

-   **[📄 60-Day Gameplan](./docs/60_DAY_GAMEPLAN.md):** The complete day-by-day schedule for learning, development, and exam preparation.
-   **[📊 Daily Tracker](./docs/DAILY_TRACKER.md):** A markdown file to track your daily progress and keep yourself accountable.

This plan is designed to be a roadmap for anyone looking to build a substantial project while managing other commitments.

---

## ⚖️ Disclaimer

**This project is for educational purposes only. It is not financial advice.**

The information and analysis provided by the Mike-Shiva Stock Detector are not recommendations to buy or sell any security. Algorithmic trading is risky, and you should never risk money that you cannot afford to lose. Always do your own research and consult with a qualified financial advisor before making any investment decisions.

**Paper trade first.** Before using this system with real money, you should thoroughly backtest it and paper trade to understand its performance and risks.

---

## ✍️ Author

This project was created by **Mike-Shiva** with the assistance of **Manus AI**.

-   **GitHub:** [moondevonyt](https://github.com/moondevonyt)
-   **YouTube:** [MoonDev](https://youtube.com/@moondevonyt)

---

*This README was last updated on December 5, 2025.*
