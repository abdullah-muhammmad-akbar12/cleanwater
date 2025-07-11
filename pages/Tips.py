import streamlit as st

st.title("💡 Tips for Cleaner Water")
cols = st.columns(2)

tips = {
    "Boil Water": "Boiling for at least 1 minute kills most bacteria and viruses.",
    "Use Water Filters": "Certified filters remove many harmful substances.",
    "Let Water Stand": "Let sediment settle before using water.",
    "Chemical Disinfection": "Use chlorine or iodine tablets as directed."
}

i = 0
for tip, desc in tips.items():
    with cols[i % 2]:
        st.markdown(f"""
        <div class="tip-card">
            <div class="tip-title">{tip}</div>
            <div class="tip-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)
    i += 1