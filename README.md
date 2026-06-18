# Stock Earnings Dashboard

An interactive dashboard analyzing whether EPS earnings surprises predict stock price movements across 20 stocks in 4 sectors (Technology, Industrials, Energy, Consumer Defensive).

## What It Does
- Pulls 2 years of live stock data for 20 stocks across Tech, Finance, Energy, and Consumer Defensive sectors
- Calculates EPS surprise % (how much a company beat/missed analyst expectations)
- Measures same-day price reaction around each earnings date
- Visualizes the relationship interactively with Plotly Dash

## How To Run
```bash
git clone https://github.com/roshanshah570/Stock-Earnings-Dashboard
cd Stock-Earnings-Dashboard
pip install -r requirements.txt
python app.py
# Open http://127.0.0.1:8050
```

## Key Findings
- The data shows near-zero correlation (r = -0.0) between how much a company beat earnings expectations (Surprise %) and how much its stock moved that day (% Change). This means beating expectations doesn't move the stock price, because professional investors have already bought the stock weeks before based on their own predictions. This is important as it affect many people investing in stocks today and could change their investment practices.
- Additionally, the Energy sector showed the highest average EPS surprise %. This may reflect how analysts consistently underestimate energy demand, especially as AI and data centers become increasingly energy-intensive. Energy is a vital but often overlooked resource, and as AI grows, the gap between analyst forecasts and actual energy company performance may continue to widen.

## Stack
Python · Pandas · Plotly Dash · yfinance