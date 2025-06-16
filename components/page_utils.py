# pages_utils.py
import streamlit as st
import yfinance as yf
import plotly.express as px
import datetime
import pandas as pd
from components.kpi import value_display
from components.ui import render_navbar, hide_streamlit_elt





def render_commodity_page(
        page_title: str,
        ticker: str,
        description_html: str,
        image_path: str,
        image_caption: str,
        line_color: str = "blue"
):
    st.set_page_config(page_title=page_title, layout="wide", initial_sidebar_state="collapsed")

    hide_streamlit_elt()
    render_navbar()

    st.title(page_title)

    value_display(ticker)

    now = datetime.date.today()
    start_def = now - datetime.timedelta(days=365)
    start = st.date_input("From", value=start_def)
    end = st.date_input("To", value=now)

    if start > end:
        st.error("The start date must be earlier than the end date.")
        return

    df = yf.download(
        ticker,
        start=start.isoformat(),
        end=(end + datetime.timedelta(days=1)).isoformat(),
        progress=False,
    )

    if df.empty:
        st.warning("No data retrieved.")
        return

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    fig = px.line(
        df,
        x=df.index,
        y="Close",
        title=f"{ticker} price chart from {start} to {end}",
        labels={"index": "Date", "Close": "Closing price (USD)"},
    )
    fig.update_layout(xaxis_title="Date", yaxis_title="Closing price (USD)")
    fig.update_traces(line=dict(color=line_color))

    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(description_html, unsafe_allow_html=True)

    with col2:
        st.image(image_path, caption=image_caption, use_container_width=True)