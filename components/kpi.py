import streamlit as st
import yfinance as yf


def value_display(product):
    product = yf.Ticker(product)
    data = product.history(period="2d")
    current_price = data["Close"].iloc[-1]
    previous_price = data["Close"].iloc[-2]
    delta = current_price - previous_price
    percent_delta = (delta / previous_price) * 100
    st.metric(
        label="Current data",
        value=f"${current_price:,.2f}",
        delta=f"{percent_delta:+.2f}%",
    )
