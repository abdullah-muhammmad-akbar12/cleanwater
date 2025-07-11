import streamlit as st

st.set_page_config(page_title="ClearDrop", layout="centered")

# ✅ Force sidebar to show
st.sidebar.title("🔹 ClearDrop")
st.sidebar.info("Use sidebar to explore pages.")

# ✅ Load CSS directly
with open("styles.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Main content
st.markdown("<h1 class='hero-text'>💧 Drink Clean, Live Better</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="section-text">
Clean water is essential for health. Learn how to ensure safe drinking, understand contamination dangers, and empower communities.  
Your health starts with a single drop.
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.info("Navigate using the sidebar to see data, tips, and diseases.")

