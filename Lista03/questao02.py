from PIL import Image
import pytesseract

## para windows 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_path = './testeocr.png'
output_text_path = 'resultadoocr.txt'

image = Image.open(image_path)
texto_extraido = pytesseract.image_to_string(image)

with open(output_text_path, 'w', encoding='utf-8') as file:
    file.write(texto_extraido)

print("salvo", output_text_path)