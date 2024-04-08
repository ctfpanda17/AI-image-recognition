from PIL import Image
import pytesseract
import cv2
import numpy as np
from gtts import gTTS
import os

#knn = cv2.ml.KNearest_load('mnist_knn.xml') 
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

userinput = input("src=")

def transform(userinput):
    transform = userinput.replace("\\","/")
    return transform

src = transform(userinput)
print(src)

image = cv2.imread(src)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
src = cv2.erode(binary, kernel, iterations=1)
cv2.imwrite('C:/Users/r6129/Downloads/opencv/AI-image-recognition/testjpg/src.jpg', src)
src = 'C:/Users/r6129/Downloads/opencv/AI-image-recognition/testjpg/src.jpg'

print(pytesseract.image_to_string(Image.open(src), lang='eng', 
                                                config='--psm 6 --oem 3 -c '
                                                'tessedit_char_whitelist'
                                                '=0123456789'))
str = pytesseract.image_to_string(Image.open(src))
print(str)
s = gTTS(text=str)
s.save("sample.mp3")
os.system("sample.mp3")
