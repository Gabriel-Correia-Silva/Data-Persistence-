import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
import pdfplumber

def extract_html(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    return {
        "Title": soup.title.string if soup.title else "No title found",
        "Headers": [header.get_text() for header in soup.find_all(['h1', 'h2', 'h3'])],
        "Links": [link['href'] for link in soup.find_all('a', href=True)]
    }

def extract_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return {"Content": "".join(page.extract_text() or "" for page in pdf.pages).strip()}

def extract_image(image_path):
    return {"Text": pytesseract.image_to_string(Image.open(image_path)).strip()}

def extract_data(file_path):
    if file_path.startswith("http"):
        return "HTML", extract_html(file_path)
    if file_path.endswith(".pdf"):
        return "PDF", extract_pdf(file_path)
    if file_path.lower().endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp")):
        return "Image", extract_image(file_path)
    raise ValueError("Unsupported file type")

def display_extracted_data(file_path):
    file_type, data = extract_data(file_path)
    print(f"\n=== {file_type} Data ===")
    for key, value in data.items():
        print(f"{key}: {value[:500]}")

file_paths = ["https://example.com", "documento.pdf", "imagem_exemplo.png"]
for path in file_paths:
    display_extracted_data(path)
