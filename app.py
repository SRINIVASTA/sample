# app.py
# test_app.py
import streamlit as st
import matplotlib.pyplot as plt
import io

# Create a simple figure
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
buf = io.BytesIO()
fig.savefig(buf, format="png")
buf.seek(0)

st.pyplot(fig)

# Download button
st.download_button(
    label="📥 Download Test Chart",
    data=buf,
    file_name="test_chart.png",
    mime="image/png"
)
