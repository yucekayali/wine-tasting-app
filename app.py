import streamlit as st
from questions import appearance_questions, aroma_questions, taste_questions
from wine_notes import generate_note
import urllib.parse

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
    note, prompt = generate_note(wine_name, appearance, aroma, taste)
    st.subheader("📄 Tasting Note")
    st.markdown(note)

    # Görsel önerisi için Google arama linki
    encoded_prompt = urllib.parse.quote(prompt)
    search_url = f"https://www.google.com/search?tbm=isch&q={encoded_prompt}"

    st.markdown("### 🔍 Suggested Image")
    st.markdown(f"[Click here to search the image on Google Images]({search_url})")
    st.markdown(f"📷 **Prompt:** _{prompt}_")
