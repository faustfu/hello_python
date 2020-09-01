from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal

for page_layout in extract_pages("ff80808171e8274501741fb4abc90cc5.pdf"):
    for element in page_layout:
        if isinstance(element, LTTextBoxHorizontal):
          print(element)
            # for text_line in element:
            #     print(text_line)
