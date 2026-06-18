'''
Stocks Earnings Dashboard - Earnings Pipeline
Pulls earnings dates, EPS estimates vs actuals for each stock.
Calculates surprise % = how much a company beat or missed analyst expectations.
'''
import yfinance as yf
import pandas as pd
from data_pull import STOCKS

def get_earnings_data(ticker):
    stock = yf.Ticker(ticker)
    # Get stock info (open, close, dates, etc.) in a dataframe 
    earnings = stock.earnings_dates
    earnings = earnings.dropna(subset = ['EPS Estimate', 'Reported EPS'])

    # Calculate surprise percentage for more accurate depiction of earnings performance 
    earnings = earnings.copy()
    earnings['surprise_pct'] = (earnings['Reported EPS'] - earnings['EPS Estimate']) / earnings['EPS Estimate'] * 100
    earnings['Ticker'] = ticker
    return earnings

# get_earnings_data function test case
#print(get_earnings_data("AAPL"))
