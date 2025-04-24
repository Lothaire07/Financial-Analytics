import streamlit as st
import yfinance as yf
import plotly.express as px
import datetime
import pandas as pd

st.set_page_config(
    page_title="Copper COMEX Analytics",
    layout="wide"
)

st.title("Copper COMEX Analytics (HG)")

now = datetime.date.today()
start_def = now - datetime.timedelta(days=365)
start = st.date_input("From", value=start_def)
end = st.date_input("To", value=now)

if start > end:
    st.error("The start date must be earlier than the end date.")
else:
    df = yf.download(
        "HG=F",
        start=start.isoformat(),
        end=(end + datetime.timedelta(days=1)).isoformat(),
        progress=False
    )

    if df.empty:
        st.warning("No data retrieved.")
    else:
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        # Création du graphique
        fig = px.line(
            df,
            x=df.index,
            y="Close",
            title=f"Copper COMEX future chart from {start} to {end}",
            labels={
                "index": "Date",
                "Close": "Closing price (USD)"
            },
        )
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Closing price (USD)"

        )
        fig.update_traces(line=dict(color="darkorange"))

        st.plotly_chart(fig, use_container_width=True)
