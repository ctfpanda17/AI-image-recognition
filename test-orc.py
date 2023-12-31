from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

userinput = input("src=")

def transform(userinput):
    transform = userinput.replace("\\","/")
    return transform

src = transform(userinput)
print(src)
print(pytesseract.image_to_string(Image.open(src), lang='eng'))
