import streamlit as st
import yfinance as yf
import plotly.express as px
import datetime
import pandas as pd

from components.kpi import value_display
from components.ui import hide_streamlit_elt

st.set_page_config(page_title="Silver COMEX Analytics", layout="wide",initial_sidebar_state="collapsed")
hide_streamlit_elt()

st.title("Silver COMEX Analytics (SI)")

value_display("SI=F")

now = datetime.date.today()
start_def = now - datetime.timedelta(days=365)
start = st.date_input("From", value=start_def)
end = st.date_input("To", value=now)

if start > end:
    st.error("The start date must be earlier than the end date.")
else:
    df = yf.download(
        "SI=F",
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
            title=f"Silver COMEX future chart from {start} to {end}",
            labels={"index": "Date", "Close": "Closing price (USD)"},
        )
        fig.update_layout(xaxis_title="Date", yaxis_title="Closing price (USD)")
        fig.update_traces(line=dict(color="silver"))

        st.plotly_chart(fig, use_container_width=True)

        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(
                """
                <style>
                    .silver-hover {
                        display: inline-block;
                        transition: color 0.3s, text-shadow 0.3s;
                        font-weight: bold;
                        color: inherit;
                    }

                    .silver-hover:hover {
                        color: silver;
                        text-shadow: 0 0 10px rgba(192, 192, 192, 0.8), 0 0 20px rgba(192, 192, 192, 0.6);
                    }
                </style>

                <div>
                  <p>
                    <span class="silver-hover">Silver</span> is a precious and industrial metal with unique dual-use value in both economic and technological domains:
                    <ul>
                      <li>The best natural electrical conductor, used in electronics, batteries, and solar panels</li>
                      <li>Historically used as currency and store of value, often seen as "Gold’s cousin"</li>
                      <li>Highly reflective and antimicrobial, with applications in medicine and optics</li>
                    </ul>
                    Silver is both a financial asset and a key industrial component.  
                    Its price is influenced by:
                    <ul>
                      <li>Global demand in electronics and green tech (solar, EVs)</li>
                      <li>Investment demand (coins, ETFs, futures)</li>
                      <li>Inflation and interest rate expectations</li>
                      <li>Correlation with gold and other commodities</li>
                    </ul>
                    As both a hedge and a growth metal, silver sits at the crossroads of finance and industry — volatile, but strategically significant.
                  </p>
                </div>
                """,
                unsafe_allow_html=True,
            )


        with col2:
            st.image(
                "images/scottsdale-mint-M6f-OZK0N6w-unsplash.jpg",
                caption="Silver Coins",
                use_container_width=True,
            )

