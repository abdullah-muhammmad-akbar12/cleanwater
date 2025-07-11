import streamlit as st
import pandas as pd

st.title("📊 Latest Non-Clean Water Results")

st.markdown("""
<div class="card">
  Test results coming soon. Stay tuned for updates on local water safety.
</div>
""", unsafe_allow_html=True)

df = pd.DataFrame({
    "Sample ID": ["S-001", "S-002"],
    "Location": ["Well A", "Stream B"],
    "E. coli (cfu/ml)": [300, 180],
    "pH": [6.4, 7.1],
    "Turbidity (NTU)": [25, 18]
})
st.dataframe(df)