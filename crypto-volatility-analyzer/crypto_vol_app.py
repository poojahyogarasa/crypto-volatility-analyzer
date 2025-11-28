import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# ---------------------------
# Helper: Compute volatility
# ---------------------------
def compute_volatility(df):
    data = df.copy()
    data['Return'] = data['Close'].pct_change().fillna(0)

    # Rolling volatility (not annualized, just raw std for window)
    data['Vol_7D'] = data['Return'].rolling(7).std()
    data['Vol_30D'] = data['Return'].rolling(30).std()
    data['Vol_90D'] = data['Return'].rolling(90).std()

    # Latest values
    vol_7d = data['Vol_7D'].iloc[-1]
    vol_30d = data['Vol_30D'].iloc[-1]
    vol_90d = data['Vol_90D'].iloc[-1]

    return data, vol_7d, vol_30d, vol_90d


def classify_risk(vol_30d):
    if np.isnan(vol_30d):
        return "Not enough data"
    # thresholds can be tuned
    if vol_30d < 0.02:
        return "🟢 Low Risk"
    elif vol_30d < 0.05:
        return "🟡 Medium Risk"
    else:
        return "🔴 High Risk"


# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="Crypto Volatility Analyzer", layout="wide")

st.title("💹 Cryptocurrency Volatility Analyzer")
st.write(
    "Upload price data for a cryptocurrency and analyze its **risk & volatility** "
    "over different time windows."
)

# Sidebar
st.sidebar.header("📂 Data Input")
uploaded_file = st.sidebar.file_uploader("Upload CSV with Date & Close columns", type=["csv"])

st.sidebar.markdown("---")
st.sidebar.write("👀 Tip: You can download BTC/ETH data from Yahoo Finance or any exchange, then upload here.")

st.markdown("### 1️⃣ Data Preview")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if 'Date' not in df.columns or 'Close' not in df.columns:
        st.error("CSV must contain at least **Date** and **Close** columns.")
    else:
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values('Date')
        df.set_index('Date', inplace=True)

        st.dataframe(df.head())

        # Run analysis
        if st.button("🚀 Analyze Volatility"):
            data, vol_7d, vol_30d, vol_90d = compute_volatility(df)

            # 2️⃣ Metrics
            st.markdown("### 2️⃣ Volatility Metrics (Std Dev of Daily Returns)")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("7D Volatility", f"{vol_7d*100:.2f}%" if not np.isnan(vol_7d) else "N/A")
            col2.metric("30D Volatility", f"{vol_30d*100:.2f}%" if not np.isnan(vol_30d) else "N/A")
            col3.metric("90D Volatility", f"{vol_90d*100:.2f}%" if not np.isnan(vol_90d) else "N/A")
            col4.metric("Risk Level (30D)", classify_risk(vol_30d))

            # 3️⃣ Price chart
            st.markdown("### 3️⃣ Price Chart")
            fig1, ax1 = plt.subplots(figsize=(10, 4))
            ax1.plot(data.index, data['Close'])
            ax1.set_ylabel("Price")
            ax1.set_xlabel("Date")
            ax1.set_title("Price Over Time")
            st.pyplot(fig1)

            # 4️⃣ Volatility chart (30D rolling)
            st.markdown("### 4️⃣ Rolling 30D Volatility")
            fig2, ax2 = plt.subplots(figsize=(10, 4))
            ax2.plot(data.index, data['Vol_30D'])
            ax2.set_ylabel("Volatility (Std Dev)")
            ax2.set_xlabel("Date")
            ax2.set_title("Rolling 30-Day Volatility")
            st.pyplot(fig2)

            # 5️⃣ Show last rows
            st.markdown("### 5️⃣ Last 10 Records")
            st.dataframe(data.tail(10))

else:
    st.info("Upload a CSV file with **Date** and **Close** columns to begin.")
