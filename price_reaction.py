'''
Stock Earnings Dashboard — Price Reaction Analysis

Pairs each earnings date from earnings.py with its pre and post-earnings
trading days from data_pull.py, calculating the resulting price move
("Price Reaction %") for comparison against EPS Surprise %.
'''

import yfinance as yf
import pandas as pd
from data_pull import STOCKS, get_stock_info
from earnings import get_earnings_data

'''
Get price reaction data (how much a stock moved, pre and post-earnings trading days) in a dataframe

param ticker: stock ticker symbol (e.g. AAPL, MSFT, etc.)
return: price reaction data (pre and post-earnings trading days, price reaction %, EPS surprise %)
'''
def get_price_reaction(ticker):
    results = []
    stock = yf.Ticker(ticker)

    # Collect stock info, history, and earning data to add to dataframe
    earnings = get_earnings_data(ticker)
    hist, info = get_stock_info(ticker)
    
    # loop through earnings dates to calculate percent change 
    for date in earnings.index:
        idx = hist.index.searchsorted(date)
        if idx == 0 or idx >= len(hist):
            continue # skip if earnings date is outside of historical data range
        if date.hour >= 12:  # AMC: reported after market close
            day_before = hist.iloc[idx - 1]
            day_after = hist.iloc[idx]
        else:  # BMO: reported before market open
            if idx - 2 < 0:
                continue
            day_before = hist.iloc[idx - 2]
            day_after = hist.iloc[idx - 1]

        pct_change = (day_after['Close'] - day_before['Close']) / day_before['Close'] * 100

        results.append({
            "Ticker": ticker,
            "Earnings Date": date,
            "Price Reaction %": pct_change,
            "Surprise %": earnings.loc[date, 'surprise_pct']
        })
        
    # Add information about stock into one, cohesive dataframe
    return pd.DataFrame(results)
