import streamlit as st
import yfinance as yf
import plotly.express as px
import datetime
import pandas as pd

st.set_page_config(page_title="Gold COMEX Analytics", layout="wide")

st.title("Gold COMEX Analytics (GC)")

gold = yf.Ticker("GC=F")
data = gold.history(period="2d")
current_price = data["Close"].iloc[-1]
previous_price = data["Close"].iloc[-2]
delta = current_price - previous_price
percent_delta = (delta / previous_price) * 100
st.metric(
    label="Current data", value=f"${current_price:,.2f}", delta=f"{percent_delta:+.2f}%"
)

now = datetime.date.today()
start_def = now - datetime.timedelta(days=365)
start = st.date_input("From", value=start_def)
end = st.date_input("To", value=now)

if start > end:
    st.error("The start date must be earlier than the end date.")
else:
    df = yf.download(
        "GC=F",
        start=start.isoformat(),
        end=(end + datetime.timedelta(days=1)).isoformat(),
        progress=False,
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
            title=f"Gold COMEX future chart from {start} to {end}",
            labels={"index": "Date", "Close": "Closing price (USD)"},
        )
        fig.update_layout(xaxis_title="Date", yaxis_title="Closing price (USD)")
        fig.update_traces(line=dict(color="gold"))

        st.plotly_chart(fig, use_container_width=True)

        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(
                """
            <style>
                .gold-hover {
                  display: inline-block;
                  transition: color 0.3s, text-shadow 0.3s;
                  font-weight: bold;
                  color: inherit;
                }
                
                .gold-hover:hover {
                  color: goldenrod;
                  text-shadow: 0 0 10px rgba(255, 215, 0, 0.8), 0 0 20px rgba(255, 215, 0, 0.6);
                }  

            </style>

            <div>
              <p>
                <span class="gold-hover">Gold</span> is a precious metal with a unique blend of physical and economic properties:
                <ul>
                  <li>Chemically stable and resistant to corrosion</li>
                  <li>Highly conductive, used in electronics and industry</li>
                  <li>Historically valued as a store of wealth and a symbol of status</li>
                </ul>
                In the global economy, gold plays the role of a “safe haven” asset, attracting investors in times of uncertainty or inflation.  
                Its price is influenced by:
                <ul>
                  <li>Interest rates</li>
                  <li>Inflation expectations</li>
                  <li>Geopolitical tensions</li>
                  <li>Central bank reserves</li>
                </ul>
                Whether seen as a hedge against currency devaluation or a speculative instrument, gold remains one of the most traded and watched commodities in the world.
              </p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col2:
            st.image(
                "images/scottsdale-mint-2jjc94apOCY-unsplash.jpg",
                caption="Gold Ingot",
                use_container_width=True,
            )
