'''
Stocks Earnings Dashboard - Main Application
Interactive Plotly Dash dashboard displaying earnings surprise % vs stock price reaction
'''

import dash
from dash import dcc, html, Output, Input
import plotly.express as px
import pandas as pd
from data_pull import STOCKS
from price_reaction import get_price_reaction

all_data = []

for sector, tickers in STOCKS.items():
    for ticker in tickers:
        try:
            df = get_price_reaction(ticker)
            if df is not None and not df.empty:
                df["Sector"] = sector
                all_data.append(df)
        except Exception as e:
            print(f"Skipping {ticker}: {e}")

if all_data:
    df_all = pd.concat(all_data, ignore_index=True)
else:
    df_all = pd.DataFrame(columns=["Ticker", "Earnings Date", "Price Reaction %", "Surprise %", "Sector"])

corr = df_all["Surprise %"].corr(df_all["Price Reaction %"]).round(2)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Stock Earnings Surprise Dashboard", 
            style={"textAlign": "center", "fontFamily": "Arial"}),
    html.H3(f"Surprise % & Price Reaction % Correlation: {corr}", 
            style={"textAlign": "center", "fontFamily": "Arial"}),
    dcc.Graph(id="scatter-plot"),
    dcc.Graph(id="bar-chart"),
])

# Callback for scatter plot
@app.callback(
    Output("scatter-plot", "figure"),
    Input("scatter-plot", "id")
)
def update_scatter(_):
    fig = px.scatter(
        df_all,
        x="Surprise %",
        y="Price Reaction %",
        color="Sector",
        hover_data=["Ticker", "Earnings Date"],
        title="EPS Surprise % vs Stock Price Reaction %",
    )
    return fig


# Callback for bar chart
@app.callback(
    Output("bar-chart", "figure"),
    Input("bar-chart", "id")
)
def update_bar(_):
    avg = df_all.groupby("Sector")["Surprise %"].mean().reset_index()
    fig = px.bar(
        avg,
        x="Sector",
        y="Surprise %",
        color="Sector",
        title="Average EPS Surprise % by Sector",
    )
    return fig

if __name__ == "__main__":
    app.run()