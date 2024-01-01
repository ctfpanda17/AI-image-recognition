from PIL import Image
import pytesseract
import cv2
import numpy as np

knn = cv2.ml.KNearest_load('opencv/mnist_knn.xml') 
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

userinput = input("src=")

def transform(userinput):
    transform = userinput.replace("\\","/")
    return transform

src = transform(userinput)
print(src)
print(pytesseract.image_to_string(Image.open(src), lang='eng', 
                                                config='--psm 6 --oem 3 -c '
                                                'tessedit_char_whitelist'
                                                '=0123456789'))
print(pytesseract.image_to_string(Image.open(src)))

#text = str(int(knn.predict(src)))
#fontFace = cv2.FONT_HERSHEY_SIMPLEX     # 印出的文字字體
#fontScale = 2                           # 印出的文字大小
#color = (0,0,255)                       # 印出的文字顏色
#print(cv2.putText(text, fontFace, fontScale, color)) # 印出文字
