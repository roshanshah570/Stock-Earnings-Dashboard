'''
Stocks Earnings Dashboard - Earnings Pipeline
Pulls earnings dates, EPS estimates vs actuals for each stock.
Calculates surprise % = how much a company beat or missed analyst expectations.
'''
import yfinance as yf
import pandas as pd
from data_pull import STOCKS


'''
Get earnings data (earnings dates, EPS estimates vs actuals) in a dataframe

param ticker: stock ticker symbol (e.g. AAPL, MSFT, etc.)
return: earnings data (earnings dates, EPS estimates vs actuals, surprise %)
'''
def get_earnings_data(ticker):
    stock = yf.Ticker(ticker)
    # Get stock info (open, close, dates, etc.) in a dataframe 
    earnings = stock.earnings_dates
    earnings = earnings.dropna(subset=['EPS Estimate', 'Reported EPS'])
    earnings = earnings.copy()
    # Drop unstable denominators to avoid skewed surprise % calculations
    earnings = earnings[earnings['EPS Estimate'].abs() > 0.10]

    # Use abs() in denominator to avoid sign-flip and calculate surprise % 
    earnings['surprise_pct'] = (earnings['Reported EPS'] - earnings['EPS Estimate']) / earnings['EPS Estimate'].abs() * 100
    earnings['Ticker'] = ticker
    return earnings

# get_earnings_data function test case
# print(get_earnings_data("VLO"))
