import streamlit as st
import yfinance as yf
import ta
import streamlit_autorefresh as sta


def value_display(product):
    st.markdown("""
    <style>
    
    .live-label {
      position: absolute;
      display: inline-flex;
      align-items: center;
      font-size: 1rem;
      font-weight: 600;
      margin-top: 2em;
    }
    .live-label .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background-color: red;
      animation: pulse 1s infinite;
      margin-right: 0.4rem;
    }
    @keyframes pulse {
      0%,100% { opacity: 1; }
      50%     { opacity: 0.4; }
    }
    </style>
    """, unsafe_allow_html=True)

    sta.st_autorefresh(interval=10 * 1000, key="refresh")
    product = yf.Ticker(product)
    current_price = product.info["regularMarketPrice"]
    previous_price = product.info["previousClose"]
    delta = current_price - previous_price
    percent_delta = (delta / previous_price) * 100

    st.markdown(f"""
    <div class="live-label">
      <div class="dot"></div>
      Current price
    </div>
    """, unsafe_allow_html=True)
    st.metric(
            label="",
            value=f"${current_price:,.2f}",
            delta=f"{percent_delta:+.2f}%"
    )

def sma(product):
    product = yf.Ticker(product)
    data = product.history(period="2y")
    # Supposons que `data` contient un DataFrame avec 'Close'
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window=14).rsi()

    st.subheader("Indicateurs techniques")
    st.line_chart(data[['Close', 'SMA_20']])
    st.line_chart(data['RSI'])
