import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

st.title("**Stock Data Visualization**")


@st.cache_data
def getData(stock="AAPL") -> pd.DataFrame:
    stock = yf.Ticker(stock)
    stock_price_data = stock.history(period="max")
    return stock_price_data.sort_values(by="Date", ascending=False)


stock_name = st.text_input("Enter stock ticker symbol: ", "AAPL")
if stock_name:
    st.write(f"Real time {stock_name} price data: ")
    df = getData(stock_name)
    if df.empty:
        st.error("Invalid Ticker", icon="🚨")

    else:
        st.write(df)
