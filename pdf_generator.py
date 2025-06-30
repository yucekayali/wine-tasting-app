from fpdf import FPDF
from PIL import Image
import io

def create_pdf(note_text, image_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Tadım notunu satır satır yaz
    for line in note_text.strip().split("\\n"):
        pdf.multi_cell(0, 10, line)

    # Şarap fotoğrafı ekle
    if image_file:
        img = Image.open(image_file)
        img_path = "/tmp/wine_photo.jpg"
        img.save(img_path)
        current_y = pdf.get_y() + 10
        pdf.image(img_path, x=10, y=current_y, w=100)

    # PDF çıktısını bellek içine yaz
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)
    return pdf_output
