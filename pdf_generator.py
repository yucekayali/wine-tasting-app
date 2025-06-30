from fpdf import FPDF
from PIL import Image
import io

def create_pdf(note_text, image_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in note_text.strip().split("\n"):
        pdf.multi_cell(0, 10, line)

    if image_file:
        img = Image.open(image_file)
        img_path = "/tmp/wine_photo.jpg"
        img.save(img_path)
        current_y = pdf.get_y() + 10
        pdf.image(img_path, x=10, y=current_y, w=100)

    # Doğrudan bellek çıktısı
    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    return io.BytesIO(pdf_bytes)
