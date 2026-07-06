# Stock Earnings Dashboard

An interactive dashboard analyzing whether EPS earnings surprises predict stock price movements across 20 stocks in 4 sectors (Technology, Industrials, Energy, Consumer Defensive).

## What It Does
- Pulls 2 years of live stock data for 20 stocks across Technology, Industrials, Energy, and Consumer Defensive sectors
- Calculates EPS surprise % (how much a company beat/missed analyst expectations), using a corrected formula that avoids sign errors on negative EPS estimates and filters out unstable near-zero denominators
- Measures price reaction around each earnings date, correctly windowed for whether the company reports before market open (BMO) or after market close (AMC)
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
- The data shows a weak positive correlation (r = 0.19) between EPS surprise % and price reaction % across the 20-stock sample. Larger earnings beats are associated with more positive price reactions, but the relationship is weak. This suggests that while surprises do move prices to some degree, much of the reaction is likely driven by other factors, (forward guidance, broader market conditions, sector trends) not fully captured by surprise percent alone. This is consistent with prior research on earnings announcements and market efficiency, where surprise magnitude is one factor among many and not a dominant predictor.
- (Note: earlier versions of this analysis reported a near-zero correlation. That result was affected by a data quality issue — an extreme outlier from a near-zero EPS estimate — and an indexing bug that mismeasured the price reaction window for stocks reporting before market open. Both have been corrected.)

# Live Deployment
https://market-earnings-monitor-732893358511.us-central1.run.app

## Stack
Python · Pandas · Plotly Dash · yfinance

## Data Notes

- Price reaction is measured using the trading days immediately before and after each earnings date, adjusted for whether the report was BMO or AMC.
- Rows with an EPS Estimate near zero (|estimate| ≤ 0.10) are excluded, since dividing by a near-zero denominator produces extreme, unreliable surprise percentages.
