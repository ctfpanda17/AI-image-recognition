from PIL import Image
import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

#userinput = input("src=")

def transform(userinput):
    transform = userinput.replace("\\","/")
    return transform

#src = transform(userinput)
image = cv2.imread('C:/Users/r6129/Downloads/opencv/AI-image-recognition/testjpg/shao_p2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
erode = cv2.erode(binary, kernel, iterations=1)
#contours = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#for contour in contours:
#    cv2.drawContours(image, [contour], 0, (0, 0, 255), thickness=2)

cv2.imshow('image',erode)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(src)
#print(pytesseract.image_to_string(Image.open(src), lang='eng', 
#                                               config='--psm 6 --oem 3 -c '
#                                               'tessedit_char_whitelist'
#                                                '=0123456789'))
#str = pytesseract.image_to_string(Image.open(src))
#print(str)