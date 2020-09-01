from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
for page_layout in extract_pages("ff80808171e8274501741fb4abc90cc5.pdf"):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            for text_line in element:
                for character in text_line:
                    if isinstance(character, LTChar):
                        print('fontname = {a}, size = {b}, text = [{c}]'.format(
                            a=character.fontname, b=character.size, c=character.get_text()))
