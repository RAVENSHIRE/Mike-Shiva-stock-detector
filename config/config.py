"""
Configuration file for Mike-Shiva Stock Detector
Pre-Mover Detection System based on Moondev Framework
"""

import os
from dotenv import load_dotenv

load_dotenv()

# =============================================================================
# API KEYS & AUTHENTICATION
# =============================================================================

# OpenAI API (for AI analysis)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')

# Yahoo Finance (free, no key needed)
USE_YAHOO_FINANCE = True

# Alpha Vantage (optional, for additional data)
ALPHA_VANTAGE_KEY = os.getenv('ALPHA_VANTAGE_KEY', '')

# =============================================================================
# PRE-MOVER DETECTION SETTINGS
# =============================================================================

# Momentum thresholds
MOMENTUM_DAYS = 7  # Look back 3-7 days for price acceleration
MIN_PRICE_CHANGE = 0.05  # Minimum 5% price change to consider
MIN_RELATIVE_STRENGTH = 1.2  # Must be 20% stronger than sector

# Volume settings
UNUSUAL_VOLUME_THRESHOLD = 1.5  # 150% of 20-day average
VOLUME_LOOKBACK_DAYS = 20
MIN_ACCUMULATION_DAYS = 3  # Minimum days of rising volume

# Sector rotation
TRACK_SECTORS = [
    'Technology',
    'Healthcare', 
    'Financials',
    'Biotechnology',
    'Artificial Intelligence',
    'Fintech'
]

# IPO tracking (2025-2026 focus)
IPO_WATCHLIST = [
    # AI & Machine Learning
    'DTBK',  # Databricks (expected 2026)
    'CRBR',  # Cerebras Systems
    'LMBD',  # Lambda Labs
    
    # Fintech & Crypto
    'KRKN',  # Kraken
    'CNSYS', # Consensys
    'BTGO',  # BitGo
    'UPGD',  # Upgrade
    
    # Enterprise & Cloud
    'CHSY',  # Cohesity
    'MTVT',  # Motive Technologies
    
    # Consumer
    'STRV',  # Strava
    'ANMC',  # Animoca Brands
]

# Related public companies (bellwethers)
BELLWETHER_STOCKS = [
    'NVDA',  # Nvidia (AI chips)
    'AVGO',  # Broadcom (AI chips)
    'MRVL',  # Marvell (AI chips - potential doubler)
]

# =============================================================================
# RISK MANAGEMENT
# =============================================================================

# Entry rules
MAX_POSITION_SIZE = 0.05  # Max 5% of portfolio per position
MIN_LIQUIDITY = 100000  # Minimum $100k daily volume

# Exit rules
MICROCAP_PROFIT_TARGET = 0.30  # 30% profit target for micro-caps
LARGECAP_PROFIT_TARGET = 0.15  # 15% profit target for large caps
STOP_LOSS_PERCENT = 0.08  # 8% stop loss

# Position management
PARTIAL_SELL_AT = 0.20  # Sell 50% at 20% profit
TRAIL_STOP_ACTIVATION = 0.15  # Activate trailing stop at 15% profit
TRAIL_STOP_DISTANCE = 0.05  # Trail by 5%

# =============================================================================
# DATA SOURCES
# =============================================================================

# Market data refresh intervals (seconds)
REALTIME_REFRESH = 60  # 1 minute for active monitoring
DAILY_SCAN_TIME = "09:30"  # Market open time (EST)
PREMARKET_SCAN_TIME = "08:00"  # Pre-market scan time

# Data retention
HISTORICAL_DAYS = 365  # Keep 1 year of historical data
CACHE_EXPIRY = 300  # Cache API responses for 5 minutes

# =============================================================================
# AI AGENT SETTINGS
# =============================================================================

# Model selection
AI_MODEL = "gpt-4.1-mini"  # Fast and cost-effective
USE_SWARM_MODE = False  # Set to True for multi-model consensus

# Swarm models (if USE_SWARM_MODE = True)
SWARM_MODELS = [
    "gpt-4.1-mini",
    "gemini-2.5-flash",
]

# Analysis parameters
MIN_PROBABILITY_SCORE = 70  # Minimum 70/100 to flag as pre-mover
MAX_STOCKS_PER_SCAN = 10  # Return top 10 candidates

# =============================================================================
# NOTIFICATION SETTINGS
# =============================================================================

# Alert methods
ENABLE_CONSOLE_ALERTS = True
ENABLE_FILE_LOGGING = True
LOG_FILE_PATH = "logs/detector.log"

# Alert thresholds
ALERT_ON_HIGH_PROBABILITY = 85  # Alert if probability > 85%
ALERT_ON_VOLUME_SPIKE = 2.0  # Alert if volume > 200% of average

# =============================================================================
# BACKTESTING SETTINGS
# =============================================================================

BACKTEST_START_DATE = "2024-01-01"
BACKTEST_END_DATE = "2025-12-31"
INITIAL_CAPITAL = 10000
COMMISSION = 0.001  # 0.1% commission per trade

# =============================================================================
# DEVELOPMENT & DEBUGGING
# =============================================================================

DEBUG_MODE = False
VERBOSE_LOGGING = True
SAVE_ANALYSIS_REPORTS = True
REPORTS_DIR = "reports/"
