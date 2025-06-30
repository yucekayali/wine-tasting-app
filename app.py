import streamlit as st
from questions import appearance_questions, aroma_questions, taste_questions
from wine_notes import generate_note

st.title("🍷 Wine Tasting Assistant")

st.header("1. Appearance")
appearance = {}
for q, options in appearance_questions.items():
    appearance[q] = st.selectbox(f"Select {q}", options)

st.header("2. Aroma")
aroma = {}
for q, options in aroma_questions.items():
    aroma[q] = st.selectbox(f"Select {q}", options)

st.header("3. Taste")
taste = {}
for q, options in taste_questions.items():
    taste[q] = st.selectbox(f"Select {q}", options)

st.header("4. Wine Name")
wine_name = st.text_input("Enter the wine name")

if st.button("Generate Wine Note"):
    note = generate_note(wine_name, appearance, aroma, taste)
    st.subheader("📄 Tasting Note")
    st.markdown(note)
