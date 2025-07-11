import streamlit as st

st.title("🦠 Waterborne Diseases")

diseases = [
    {
        "name": "Cholera",
        "symptoms": "Severe diarrhea, vomiting, dehydration.",
        "treatment": "Rehydration, antibiotics."
    },
    {
        "name": "Typhoid",
        "symptoms": "Fever, weakness, abdominal pain.",
        "treatment": "Antibiotics, fluids, rest."
    },
    {
        "name": "Hepatitis A",
        "symptoms": "Fatigue, jaundice, nausea.",
        "treatment": "Rest, fluids, no alcohol."
    }
]

for d in diseases:
    st.markdown(f"""
    <div class="disease-card">
        <div class="disease-name">🔹 {d['name']}</div>
        <div><strong>Symptoms:</strong> {d['symptoms']}</div>
        <div><strong>Treatment:</strong> {d['treatment']}</div>
    </div>
    """, unsafe_allow_html=True)