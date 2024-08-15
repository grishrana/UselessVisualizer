import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import time


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
    st.write(f"**Real time {stock_name} price data:** ")
    df = getData(stock_name)
    if df.empty:
        st.error("Invalid Ticker", icon="🚨")

    else:
        st.write(df)


st.header(f"**CandleStick Analysis {stock_name}**")

today = datetime.datetime.now()
col1, col2 = st.columns(2)
with col1:
    end = st.date_input(
        "Enter End Date", datetime.date(today.year, today.month, today.day)
    )

with col2:
    start = st.date_input(
        "Enter Start Date", datetime.date(today.year, today.month, today.day - 7)
    )


filtered_df = df[
    (df["Date"] >= pd.Timestamp(start)) & (df["Date"] <= pd.Timestamp(end))
]
fig = go.Figure(
    data=[
        go.Candlestick(
            x=filtered_df["Date"],
            open=filtered_df["Open"],
            high=filtered_df["High"],
            close=filtered_df["Close"],
            low=filtered_df["Low"],
        )
    ]
)

fig.update_layout(
    xaxis_title="Date", yaxis_title="Price", xaxis_rangeslider_visible=False
)

st.plotly_chart(fig)

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
