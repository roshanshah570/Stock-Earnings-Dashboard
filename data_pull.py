'''
Stocks Earnings Dashboard - Data Pipeline
Pulls 2 years of historical data for 20 stocks across 4 sectors using yfinance API.
Used as data foundation for earnings analysis and dashboard visualizations.
'''

import yfinance as yf
import pandas as pd

STOCKS  = {
    "Technology": ["AAPL", "MSFT", "NVDA", "META", "ADBE"],
    "Industrials": ["CAT", "HON", "GE", "DE", "MMM"],
    "Energy": ["XOM", "CVX", "COP", "EOG", "VLO"],
    "Consumer Defensive": ["WMT", "PG", "KO", "COST", "MDLZ"]
}

'''
Get stock info (open, close, dates, etc.) in a dataframe

param ticker: stock ticker symbol (e.g. AAPL, MSFT, etc.)
return: historical stock data (2 years) and stock info (company name, sector, etc.)
'''
def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="2y")
    info = stock.info 
    return hist, info

# Test to make sure get_stock_info works
#hist, info = get_stock_info("AAPL")
#print(f"Company: {info.get('longName')}")
#print(f"Sector:  {info.get('sector')}")
#print(f"Rows:    {len(hist)}")
#print(hist.head())