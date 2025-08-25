import streamlit as st
import pandas as pd
import io
from nifty50_data import fetch_nifty50_data
from plot_utils import plot_dark_mode

# Streamlit page setup
st.set_page_config(layout="wide", page_title="Nifty 50 Financial Dashboard")
st.title("📊 Nifty 50 Stock Dashboard")
st.markdown("Visualizing Book Value, Current Price, and P/B Ratios for Nifty 50 companies")

# Load the data
with st.spinner("📡 Fetching Nifty 50 data..."):
    df = fetch_nifty50_data()
    st.success("✅ Data loaded successfully!")

# Display data table
st.subheader("📈 Financial Data")
st.dataframe(df, use_container_width=True)

# Plot the chart
st.subheader("📉 Financial Chart")
fig = plot_dark_mode(df)
st.pyplot(fig)

# Prepare image buffer for download button
buf = io.BytesIO()
fig.savefig(buf, format="png", bbox_inches='tight', facecolor=fig.get_facecolor())
buf.seek(0)

# Download button right after the plot
st.download_button(
    label="📥 Download Chart as PNG",
    data=buf,
    file_name="nifty50chart.png",
    mime="image/png"
)

# Footer caption
st.caption("Data Source: yfinance | Built with ❤️ using Streamlit and Matplotlib")
