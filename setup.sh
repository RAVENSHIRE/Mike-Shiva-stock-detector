#!/bin/bash
# SPY PreMover Detector - Automated Setup Script
# Run this to get everything ready for 8 AM market open!

echo "🚀 SPY PREMOVER DETECTOR - AUTOMATED SETUP 🚀"
echo "=============================================="
echo ""

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✅ Found Python $python_version"
echo ""

# Create virtual environment
echo "🔧 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip -q
echo "✅ pip upgraded"
echo ""

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt -q
echo "✅ Dependencies installed"
echo ""

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "🔑 Creating .env file..."
    cp .env.example .env
    echo "⚠️  IMPORTANT: Edit .env and add your OPENAI_API_KEY"
    echo ""
else
    echo "✅ .env file already exists"
    echo ""
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p data reports notebooks
echo "✅ Directories created"
echo ""

# Run verification
echo "🧪 Running verification tests..."
python3 << 'EOF'
import sys

print("Testing imports...")
try:
    import pandas as pd
    print("✅ pandas")
    import numpy as np
    print("✅ numpy")
    import yfinance as yf
    print("✅ yfinance")
    from openai import OpenAI
    print("✅ openai")
    from dotenv import load_dotenv
    print("✅ python-dotenv")
    print("\n✅ All packages installed correctly!")
except ImportError as e:
    print(f"\n❌ Error: {e}")
    sys.exit(1)

# Test API key
import os
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
if api_key and api_key != 'your-openai-api-key-here':
    print("✅ OpenAI API key found")
else:
    print("⚠️  OpenAI API key not configured")
    print("   Edit .env and add: OPENAI_API_KEY=your-key-here")
EOF

echo ""
echo "=============================================="
echo "✅ SETUP COMPLETE!"
echo "=============================================="
echo ""
echo "📋 Next steps:"
echo "1. Edit .env and add your OPENAI_API_KEY"
echo "2. Run: python run_daily_scan.py"
echo "3. Or run tutorial: python tutorial.py"
echo ""
echo "🎯 Ready for 8 AM market open!"
echo ""
