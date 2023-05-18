
import pytesseract
from pdf2image import convert_from_path
import glob

pdfs = glob.glob(r"sd.pdf")

for pdf_path in pdfs:
    pages = convert_from_path(pdf_path, 500,poppler_path=r'C:\Program Files\poppler-23.05.0\Library\bin')

    for pageNum,imgBlob in enumerate(pages):
        text = pytesseract.image_to_string(imgBlob,lang='eng')
        print(text)