from pytesseract import pytesseract
from PIL import Image
from glob import glob

path_to_pytesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

images = glob(r'LOST MARY\Screenshot*.png')


for image in images:
    img = Image.open(image)
    pytesseract.tesseract_cmd = path_to_pytesseract
    text = pytesseract.image_to_string(img)
    text = text.splitlines()
    product = text[0].replace(',', '')
    sku = text[2].replace('(', '')
    with open('LOST-MARY.txt', 'a') as f:
        f.write(f'PRODUCT: {product} - SKU {sku}\n\n')
