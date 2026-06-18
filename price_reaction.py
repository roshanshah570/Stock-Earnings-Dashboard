'''
Stock Earnings Dashboard - Price Reaction Analysis
Calculates the price move around earnings
'''

import yfinance as yf
import pandas as pd
from data_pull import STOCKS, get_stock_info
from earnings import get_earnings_data

def get_price_reaction(ticker):
    results = []
    stock = yf.Ticker(ticker)
    earnings = get_earnings_data(ticker)
    hist, info = get_stock_info(ticker)
    
    # loop through earnings dates and calculate price reaction 
    for date in earnings.index:
        idx = hist.index.searchsorted(date)
        if idx == 0 or idx >= len(hist):
            continue  # Skip if earnings date is out of historical data range
        day_before = hist.iloc[idx - 1]
        day_after = hist.iloc[idx]
        pct_change = (day_after['Close'] - day_before['Close']) / day_before['Close'] * 100
        results.append({
            "Ticker": ticker,
            "Earnings Date": date,
            "Price Reaction %": pct_change,
            "Surprise %": earnings.loc[date, 'surprise_pct']
        })
    return pd.DataFrame(results)

# Test to make sure get_price_reaction works
print(get_price_reaction("AAPL"))