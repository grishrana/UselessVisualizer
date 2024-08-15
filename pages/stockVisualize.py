import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import time
from scipy.stats import linregress

st.title("**Stock Data Visualization**")


@st.cache_data
def getData(stock="AAPL") -> pd.DataFrame:
    stock = yf.Ticker(stock)
    stock_price_data = stock.history(period="max")
    stock_price_data.reset_index(inplace=True)
    stock_price_data["Date"] = pd.to_datetime(stock_price_data["Date"]).dt.tz_localize(
        None
    )
    return stock_price_data.sort_values(by="Date", ascending=False)


stock_name = st.text_input("Enter stock ticker symbol: ", "AAPL")


if stock_name:
    df = getData(stock_name)
    if df.empty:
        st.error("Invalid Ticker", icon="🚨")


today = datetime.datetime.now()
mindate = df.loc[0, "Date"]

col1, col2 = st.columns(2)
with col1:
    end = st.date_input(
        "Enter End Date",
        datetime.date(today.year, today.month, today.day),
        max_value=datetime.date(today.year, today.month, today.day),
        min_value=datetime.date(mindate.year, mindate.month, mindate.day),
    )

with col2:
    start = st.date_input(
        "Enter Start Date",
        datetime.date(today.year, today.month, today.day - 7),
        max_value=datetime.date(today.year, today.month, today.day),
        min_value=datetime.date(mindate.year, mindate.month, mindate.day),
    )


filtered_df = df[
    (df["Date"] >= pd.Timestamp(start)) & (df["Date"] <= pd.Timestamp(end))
]

st.write(f"**Real time {stock_name} price data:** ")
st.write(filtered_df)

st.header(f"**CandleStick Analysis {stock_name}**")


fig = go.Figure(
    data=[
        go.Candlestick(
            x=filtered_df["Date"],
            open=filtered_df["Open"],
            high=filtered_df["High"],
            close=filtered_df["Close"],
            low=filtered_df["Low"],
            name=stock_name,
        )
    ]
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Price",
    xaxis_rangeslider_visible=False,
    xaxis=dict(autorange="reversed"),
)

st.plotly_chart(fig)


st.subheader("**Stock Price Predictor**")
fig, axe = plt.subplots()
axe.scatter(df["Date"], df["Close"])
fifty_years_ago = today - datetime.timedelta(days=50 * 365.25)
calc_reg = linregress(
    df["Date"].map(datetime.datetime.toordinal),
    df["Close"],
)

new_dates = list(
    pd.date_range(
        start=df.iloc[-1]["Date"],
        end=(df.iloc[-1]["Date"] + pd.DateOffset(years=50)),
        freq="D",
    )
)

x_val = list(df["Date"]) + list(new_dates)
y_val = [
    (calc_reg.slope * datetime.datetime.toordinal(x)) + calc_reg.intercept
    for x in x_val
]

axe.plot(x_val, y_val, "r")
axe.set(
    title="Rise in Stock Price",
    xlabel="Date",
    ylabel="Close Price",
)
st.pyplot(fig)


st.subheader("**Correlation Heatmap**")

corr = df.corr()  # pyright: ignore
corr_masked = corr.where(np.identity(len(df.columns)).astype(bool))  # pyright: ignore
fig, axe = plt.subplots(figsize=(10, 10))
sns.heatmap(data=corr_masked, annot=True, fmt=".1f", ax=axe)

st.pyplot(fig)


st.subheader(f"**Line Chart of {stock_name}(daily) 📈**")
while True:
    with st.spinner("Loading Chart.. This might take a while.."):
        time.sleep(2)
