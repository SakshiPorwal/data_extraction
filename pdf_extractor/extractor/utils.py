import easyocr
import os
from PyPDF2 import PdfReader
from django.conf import settings

def extract_data_from_pdf(pdf_file):
    image_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
    os.makedirs(image_dir, exist_ok=True)

    pdf_path = os.path.join(image_dir, pdf_file.name)
    with open(pdf_path, 'wb') as destination:
        for chunk in pdf_file.chunks():
            destination.write(chunk)

    reader = easyocr.Reader(['en'])
    all_results = []

    with open(pdf_path, 'rb') as pdf:
        reader = PdfReader(pdf)
        for page_number in range(len(reader.pages)):
            image_path = os.path.join(image_dir, f'page_{page_number + 1}.png')
            result = reader.readtext(image_path)
            for detection in result:
                all_results.append({detection[0]: detection[1]})

    os.remove(pdf_path)

    return all_results
