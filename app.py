import streamlit as st
from questions import appearance_questions, aroma_questions, taste_questions
from wine_notes import generate_note
from pdf_generator import create_pdf

st.title("🍷 Wine Tasting Assistant")

# 1. Tadım bilgilerini seç
st.header("1. Appearance")
appearance = {q: st.selectbox(q.capitalize(), opts) for q, opts in appearance_questions.items()}

st.header("2. Aroma")
aroma = {q: st.selectbox(q.capitalize(), opts) for q, opts in aroma_questions.items()}

st.header("3. Taste")
taste = {q: st.selectbox(q.capitalize(), opts) for q, opts in taste_questions.items()}

# 2. Şarap ismi
wine_name = st.text_input("4. Wine Name")

# 3. Şarap fotoğrafı yükle (opsiyonel)
uploaded_file = st.file_uploader("📸 Upload a photo of the wine bottle (optional)", type=["jpg", "jpeg", "png"])

# 4. Tadım notunu oluştur
if st.button("📝 Generate Tasting Note"):
    note, prompt = generate_note(wine_name, appearance, aroma, taste)
    
    st.subheader("📄 Tasting Note")
    st.markdown(note)

    # PDF opsiyonu göster
    st.subheader("📥 Optional: Download as PDF")
    if st.button("📄 Create PDF"):
        pdf_file = create_pdf(note, uploaded_file)
        st.download_button(
            label="⬇️ Download PDF",
            data=pdf_file,
            file_name=f"{wine_name}_tasting_note.pdf",
            mime="application/pdf"
        )

    # Görsel önerisi
    st.markdown(f"📷 **Suggested Image Prompt:** _{prompt}_")
