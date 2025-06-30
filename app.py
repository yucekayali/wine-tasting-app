import streamlit as st
from questions import appearance_questions, aroma_questions, taste_questions
from wine_notes import generate_note
from pdf_generator import create_pdf

st.set_page_config(page_title="Wine Tasting Assistant", page_icon="🍷")

st.title("🍷 Wine Tasting Assistant")

# --- Giriş Alanları ---
st.header("1. Appearance")
appearance = {}
for q, opts in appearance_questions.items():
    appearance[q] = st.selectbox(q.capitalize(), opts)

st.header("2. Aroma")
aroma = {}
for q, opts in aroma_questions.items():
    aroma[q] = st.selectbox(q.capitalize(), opts)

st.header("3. Taste")
taste = {}
for q, opts in taste_questions.items():
    taste[q] = st.selectbox(q.capitalize(), opts)

st.header("4. Wine Name")
wine_name = st.text_input("Enter the name of the wine")

uploaded_file = st.file_uploader("📸 Upload a photo of the wine bottle (optional)", type=["jpg", "jpeg", "png"])

# --- Tadım Notu Oluştur ---
if st.button("📝 Generate Tasting Note"):
    note, prompt = generate_note(wine_name, appearance, aroma, taste)
    st.session_state["note"] = note
    st.session_state["prompt"] = prompt
    st.session_state["uploaded_file"] = uploaded_file
    st.session_state["wine_name"] = wine_name

# --- Not ve PDF Opsiyonu ---
if "note" in st.session_state:
    st.subheader("📄 Tasting Note")
    st.markdown(st.session_state["note"])

    st.subheader("📥 Optional: Download as PDF")
    if st.button("📄 Create PDF"):
        pdf_file = create_pdf(st.session_state["note"], st.session_state["uploaded_file"])
        st.download_button(
            label="⬇️ Download PDF",
            data=pdf_file,
            file_name=f"{st.session_state['wine_name']}_tasting_note.pdf",
            mime="application/pdf"
        )

    st.markdown(f"📷 **Suggested Image Prompt:** _{st.session_state['prompt']}_")
