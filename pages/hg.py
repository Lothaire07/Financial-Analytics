import streamlit as st
import yfinance as yf
import plotly.express as px
import datetime
import pandas as pd

from components.kpi import value_display
from components.ui import hide_streamlit_elt

st.set_page_config(page_title="Copper COMEX Analytics", layout="wide",initial_sidebar_state="collapsed")
hide_streamlit_elt()

st.title("Copper COMEX Analytics (HG)")

value_display("HG=F")

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
            title=f"Copper COMEX future chart from {start} to {end}",
            labels={"index": "Date", "Close": "Closing price (USD)"},
        )
        fig.update_layout(xaxis_title="Date", yaxis_title="Closing price (USD)")
        fig.update_traces(line=dict(color="darkorange"))

        st.plotly_chart(fig, use_container_width=True)

        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(
                """
                <style>
                    .copper-hover {
                        display: inline-block;
                        transition: color 0.3s, text-shadow 0.3s;
                        font-weight: bold;
                        color: inherit;
                    }

                    .copper-hover:hover {
                        color: #b87333;
                        text-shadow: 0 0 10px rgba(184, 115, 51, 0.8), 0 0 20px rgba(184, 115, 51, 0.6);
                    }
                </style>

                <div>
                  <p>
                    <span class="copper-hover">Copper</span> is a critical industrial metal valued for both its physical properties and its economic significance:
                    <ul>
                      <li>Highly conductive, making it essential for electrical wiring and electronics</li>
                      <li>Ductile and malleable, used in construction and manufacturing</li>
                      <li>Resistant to corrosion, especially in plumbing and renewable energy systems</li>
                    </ul>
                    Copper plays a vital role in the global transition to clean energy and electrification.  
                    Its price is influenced by:
                    <ul>
                      <li>Global industrial activity and construction demand</li>
                      <li>Supply levels from top producers like Chile and Peru</li>
                      <li>Trends in renewable energy infrastructure (e.g., EVs, solar)</li>
                      <li>Macroeconomic indicators and inventories</li>
                    </ul>
                    Often called “Dr. Copper” for its ability to reflect economic health, copper remains a fundamental indicator of growth and industrial momentum worldwide.
                  </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st.image(
                "images/calitore-xPVUA7Jrl58-unsplash.jpg",
                caption="Copper Wires",
                use_container_width=True,
            )

