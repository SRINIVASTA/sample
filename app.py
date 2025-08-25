# app.py

import streamlit as st
from nifty50_data import fetch_nifty50_data
from plot_utils import plot_dark_mode

st.set_page_config(layout="wide", page_title="Nifty 50 Financial Dashboard")

st.title("📊 Nifty 50 Stock Dashboard")
st.markdown("Visualizing Book Value, Current Price, and P/B Ratios")

with st.spinner("Fetching Nifty 50 data..."):
    df = fetch_nifty50_data()
    st.success("Data loaded successfully!")

st.dataframe(df, use_container_width=True)

st.subheader("📉 Financial Chart")
fig = plot_dark_mode(df)
st.pyplot(fig)

st.caption("Data Source: yfinance")
