import streamlit as st
from questions import appearance_questions, aroma_questions, taste_questions
from wine_notes import generate_note
from pdf_generator import create_pdf

st.title("🍷 Wine Tasting Assistant")

# 1. Tadım bilgileri
appearance = {q: st.selectbox(f"{q}", opts) for q, opts in appearance_questions.items()}
aroma = {q: st.selectbox(f"{q}", opts) for q, opts in aroma_questions.items()}
taste = {q: st.selectbox(f"{q}", opts) for q, opts in taste_questions.items()}

# 2. Şarap adı
wine_name = st.text_input("Enter the wine name")

# 3. Şarap fotoğrafı yükle
uploaded_file = st.file_uploader("📸 Upload a photo of the wine bottle", type=["jpg", "jpeg", "png"])

# 4. Generate note & PDF
if st.button("Generate PDF Tasting Note"):
    note, prompt = generate_note(wine_name, appearance, aroma, taste)
    pdf_file = create_pdf(note, uploaded_file)

    st.subheader("📄 Download your personalized PDF")
    st.download_button("⬇️ Download PDF", data=pdf_file, file_name=f"{wine_name}_tasting_note.pdf", mime="application/pdf")
    st.markdown(f"📷 Suggested Image Prompt: _{prompt}_")
