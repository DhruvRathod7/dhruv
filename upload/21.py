from PIL import Image
from pytesseract import pytesseract
import json

  
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"invc.png"
pytesseract.tesseract_cmd = path_to_tesseract
img = Image.open(image_path)
file = open("invc.txt", "w")
text = pytesseract.image_to_string(img)
file.write(text)

  


with open('invoice.txt', 'r') as document:
    answer = {}
   
    for line in document:
        line = line.split()
        # if line
        if not line:  # empty line?
            continue
        
        answer[line[0]] = line[1:]
    print(answer)
print (type(answer))

with open("invoice.json", 'w') as file:
    file.write((json.dumps(answer, indent=4)))

