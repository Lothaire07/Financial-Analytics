import streamlit as st
import yfinance as yf
import plotly.express as px
import datetime
import pandas as pd

from components.kpi import value_display
from components.ui import hide_sidebar_nav

st.set_page_config(page_title="Aluminium COMEX Analytics", layout="wide",initial_sidebar_state="collapsed")
hide_sidebar_nav()

st.title("Aluminium COMEX Analytics (AX)")

value_display("ALI=F")

now = datetime.date.today()
start_def = now - datetime.timedelta(days=365)
start = st.date_input("From", value=start_def)
end = st.date_input("To", value=now)

if start > end:
    st.error("The start date must be earlier than the end date.")
else:
    df = yf.download(
        "ALI=F",
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
            title=f"Aluminium COMEX future chart from {start} to {end}",
            labels={"index": "Date", "Close": "Closing price (USD)"},
        )
        fig.update_layout(xaxis_title="Date", yaxis_title="Closing price (USD)")
        fig.update_traces(line=dict(color="lightblue"))

        st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(
            """
        <style>
            .aluminum-hover {
              display: inline-block;
              transition: color 0.3s, text-shadow 0.3s;
              font-weight: bold;
              color: inherit;
            }

            .aluminum-hover:hover {
              color: lightblue;
              text-shadow: 0 0 10px rgba(153, 233, 255, 0.8), 0 0 20px rgba(153, 233, 255, 0.6);
            }  

        </style>

    </style>

    <div>
      <p>
        <span class="aluminum-hover">Aluminum</span> is a lightweight, highly versatile metal known for its physical and economic utility:
        <ul>
          <li>Exceptionally light and strong, ideal for transportation and aerospace</li>
          <li>Resistant to corrosion due to its natural oxide layer</li>
          <li>Abundant and easily recyclable, making it key in sustainable industries</li>
        </ul>
        As a critical industrial metal, aluminum demand is tied closely to global infrastructure and economic cycles.  
        Its price is influenced by:
        <ul>
          <li>Global manufacturing activity</li>
          <li>Energy costs (notably electricity for smelting)</li>
          <li>Supply from major producers like China and Russia</li>
          <li>Trade policies and tariffs</li>
        </ul>
        Valued for both its industrial and environmental role, aluminum continues to shape modern economies through innovation and scale.
      </p>
    </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.image(
            "images/s-tsuchiya-0o5F-A-FsYw-unsplash.jpg",
            caption="Aluminum Structure",
            use_container_width=True,
        )
