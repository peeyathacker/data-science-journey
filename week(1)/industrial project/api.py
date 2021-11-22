from fastapi import FastAPI, Path, HTTPException, Request, Query
from PIL import Image
import pytesseract
import re

app=FastAPI()

@app.get("/")
def home():
    return {'Hii! Welcome to my API':'Invoice expense extractor (image format)'}

@app.get("/extractor/{name}")
def extractor(name: str = Path(...,description='the path/file name of the invoice png')):
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    try:
        raw = pytesseract.image_to_string(Image.open(name)) #to open the png file and convert content to string
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not Found // Enter correct file name")
    temp = re.compile(r'\s+') 
    remove_spaces = re.sub(temp, '', raw) #to remove blank spaces from string
    remove_spaces = remove_spaces.replace(',', '') #to replace comma with blank space
    amounts = re.findall('[-+]?([\d]+\.[\d]]*)',remove_spaces) #regex to extract all amounts from the string
    int_list = [float(i) for i in amounts] #to convert string items in list into float type
    max_amount = max(int_list) #to find maximum from the list of amounts
    return max_amount

