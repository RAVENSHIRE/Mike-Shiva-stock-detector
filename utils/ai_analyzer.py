"""
AI Analyzer Utility
Uses LLM to analyze catalysts and market sentiment
"""

import os
from openai import OpenAI
from typing import Optional, Dict
import json

class AIAnalyzer:
    """AI-powered analysis using OpenAI"""
    
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key:
            self.client = OpenAI()
            self.enabled = True
        else:
            self.client = None
            self.enabled = False
            print("Warning: OPENAI_API_KEY not set. AI analysis disabled.")
    
    def detect_catalysts(self, symbol: str) -> Optional[Dict]:
        """
        Use AI to detect catalysts for a stock
        
        Args:
            symbol: Stock ticker symbol
        
        Returns:
            Dictionary with catalyst information and score
        """
        if not self.enabled:
            return {'score': 50, 'catalysts': []}
        
        try:
            prompt = f"""Analyze the stock {symbol} for potential catalysts that could drive price movement.

Consider:
- Recent SEC filings (8-K, 10-Q, S-1)
- FDA approvals or clinical trial results (if biotech)
- Partnership announcements
- Insider buying activity
- IPO or uplisting news
- Product launches
- Earnings surprises

Respond in JSON format:
{{
  "score": <0-100>,
  "catalysts": ["catalyst1", "catalyst2"],
  "confidence": "high|medium|low"
}}

If no recent catalysts found, return score of 50."""

            response = self.client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You are a financial analyst specializing in catalyst detection for stock trading."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=300
            )
            
            result = json.loads(response.choices[0].message.content)
            return result
            
        except Exception as e:
            print(f"AI analysis error for {symbol}: {e}")
            return {'score': 50, 'catalysts': []}
    
    def analyze_pre_mover_probability(self, stock_data: Dict) -> Dict:
        """
        Use AI to provide overall pre-mover probability assessment
        
        Args:
            stock_data: Dictionary with stock metrics
        
        Returns:
            AI assessment with reasoning
        """
        if not self.enabled:
            return {
                'assessment': 'AI analysis unavailable',
                'confidence': 'low'
            }
        
        try:
            prompt = f"""Analyze this stock for pre-mover potential:

Symbol: {stock_data.get('symbol')}
Current Price: ${stock_data.get('price')}
Volume Change: {stock_data.get('volume_change')}%
Momentum Score: {stock_data.get('momentum_score')}/100
Sector: {stock_data.get('sector')}

Based on this data, assess the likelihood this stock will make a significant move (>10%) in the next 1-3 days.

Respond in JSON format:
{{
  "assessment": "<brief assessment>",
  "confidence": "high|medium|low",
  "key_factors": ["factor1", "factor2"]
}}"""

            response = self.client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You are an expert stock market analyst specializing in pre-mover detection."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=200
            )
            
            result = json.loads(response.choices[0].message.content)
            return result
            
        except Exception as e:
            print(f"AI probability analysis error: {e}")
            return {
                'assessment': 'Analysis error',
                'confidence': 'low'
            }
