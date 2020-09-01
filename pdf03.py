# coding=UTF-8

from pdfminer.high_level import extract_pages
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal, LTTextLineHorizontal, LTChar
from urllib.request import urlretrieve

import re
import math
import os
import csv
from datetime import date, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

# constants
re_control_characters = re.compile(r'[\n\r\t]')
re_space_start = re.compile(r'^\s{8}')
re_level_1 = re.compile(r'^[一二三四五六七八九十]、')
re_level_2 = re.compile(r'^[123456789].\s+')

item_left_start = 78.024

title_size = 15.96

paragraph_left_start = 81.984
paragraph_size = 14.04

re_control_characters = re.compile(r'[\n\r\t]')
re_space_start = re.compile(r'^\s{8}')
re_level_1 = re.compile(r'^[一二三四五六七八九十]、')
re_level_2 = re.compile(r'^[123456789].\s+')
re_csv_date = re.compile(r'^\d{3}年\d{2}月\d{2}日$')

roc_date_format = '{:03d}年{:02d}月{:02d}日'


def date_to_roc_str(d: date) -> str:
    return roc_date_format.format(d.year-1911, d.month, d.day)


def csv_filter(rows: list, **range) -> list:
    today = date.today()
    yesterday = today - timedelta(days=1)

    start = range.get('start')
    if start is None:
        start = date_to_roc_str(yesterday)

    end = range.get('end')
    if end is None:
        end = date_to_roc_str(today)

    if rows is None or len(rows) < 1:
        return []

    result = []
    for row in rows:
        if row is None or len(row) < 3:
            continue

        if not re_csv_date.match(row[2]):
            continue

        if row[2] < start or row[2] > end:
            continue

        result.append(row)

    return result


def get_pdf_urls(urls: list) -> list:
    result = []

    options = Options()
    options.add_argument('--headless')

    firefox = webdriver.Firefox(options=options)

    for url in urls:
        path = None
        try:
            firefox.get(url)
            element = WebDriverWait(firefox, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'pdf-download')))
            path = element.get_attribute('href')
        finally:
            result.append(path)

    firefox.quit()

    return result


def get_news_url(csv_row: list) -> str:
    if csv_row is None or len(csv_row) < 2:
        return

    return csv_row[1]


def get_first_char_size(line: LTTextLineHorizontal) -> float:
    for character in line:
        if not isinstance(character, LTChar):
            continue

        return character.size


def get_first_line_size(box: LTTextBoxHorizontal) -> float:
    for line in box:
        return get_first_char_size(line)


def get_left_start(line: LTTextLineHorizontal) -> float:
    if line is None or line.bbox is None or line.bbox[0] is None:
        return 0

    return line.bbox[0]


def trim_control_characters(text: str) -> str:
    if text is None:
        return ''

    return re_control_characters.sub('', text).strip()


def is_title(line: LTTextLineHorizontal) -> bool:
    size = get_first_char_size(line)
    if math.isclose(title_size, size):
        return True

    return False


def is_empty(line: LTTextLineHorizontal) -> bool:
    if line is None or trim_control_characters(line.get_text()) == '':
        return True

    return False


def is_content(line: LTTextLineHorizontal) -> bool:
    font_size = get_first_char_size(line)
    if math.isclose(paragraph_size, font_size):
        return True

    text = line.get_text()
    if is_level_1(text) or is_level_2(text):
        return True

    return False


def is_space_start(line: LTTextLineHorizontal) -> bool:
    text = line.get_text()

    return re_space_start.match(text)


def is_level_1(text: str) -> bool:
    return re_level_1.match(text)


def is_level_2(text: str) -> bool:
    return re_level_2.match(text)


def extract_line(line: tuple, paragraph_index: int, paras: list) -> int:
    (left_start, _font_size, text) = line

    if is_level_1(text):
        paragraph_index += 1
        paras.append((1, text))
    elif is_level_2(text):
        paragraph_index += 1
        paras.append((2, text))
    elif math.isclose(paragraph_left_start, left_start) or math.isclose(item_left_start, left_start) or re_space_start.match(text):
        paragraph_index += 1
        paras.append((0, text.lstrip()))
    else:
        if paragraph_index < 0:
            return paragraph_index  # Ignore content before paragraphs

        (level, original_text) = paras[paragraph_index]
        paras[paragraph_index] = (
            level, ''.join([original_text, text.lstrip()]))

    return paragraph_index


def get_page_lines(page: PDFPage) -> list:
    result = []

    for box in page:
        if not isinstance(box, LTTextBoxHorizontal):
            continue

        for line in box:
            if not isinstance(line, LTTextLineHorizontal) or is_empty(line) or not is_content(line):
                continue

            result.append((get_left_start(line), get_first_char_size(
                line), line.get_text().rstrip()))

    return result


def get_title(page: PDFPage) -> str:
    title = []

    for element in page:
        if not isinstance(element, LTTextBoxHorizontal):
            continue

        for line in element:
            if not is_title(line):
                continue

            title.append(trim_control_characters(line.get_text()))

    return ''.join(title)


def parse_pdf(pdf_path) -> list:
    paras = []
    paragraph_index = -1

    page_number = 1
    for page in extract_pages(pdf_path):
        if page_number == 1:
            title = get_title(page)
            print('title)', title)

        for line in get_page_lines(page):
            paragraph_index = extract_line(line, paragraph_index, paras)

        page_number += 1

    return paras


# csv_uri = 'https://www.twse.com.tw/news/newsList?response=csv&keyword=&startYear=&endYear=&lang=zh'
# csv_path, _headers = urlretrieve(csv_uri)
csv_path = 'tmpf8j66t5t'


with open(csv_path, encoding='MS950') as csvfile:
    # csv_rows = csv_filter(list(csv.reader(csvfile)))

    # pdf_urls = get_pdf_urls(map(get_news_url, csv_rows))

    # csv_rows = zip(csv_rows, pdf_urls)
    csv_rows = [
        # (['109年民生消費線上主題式業績發表會圓滿結束', 'https://www.twse.com.tw/zh/news/newsDetail/ff80808171e8274501742a40929b0d1c', '109年08月26日'], 'https://www.twse.com.tw/staticFiles/news/news/tsecnews/ff80808171e8274501742a40928a0d1b.pdf'),
        # (['「集雅社股份有限公司」國內第一次有擔保轉換公司債採競價拍賣方式辦理承銷，於今(8/26)日順利完成', 'https://www.twse.com.tw/zh/news/newsDetail/ff80808171e827450174298ab8b80d0a',
        #     '109年08月26日'], 'https://www.twse.com.tw/staticFiles/news/news/tsecnews/ff80808171e8274501742d6f9b440d23.pdf'),
        (['盤中零股交易系列報導八  委託請留意交易單位', 'https://www.twse.com.tw/zh/news/newsDetail/ff80808171e82745017428bf0a670cf6',
          '109年08月26日'], 'https://www.twse.com.tw/staticFiles/news/news/tsecnews/ff80808171e82745017428bf09700cf5.pdf')
    ]

    for (info, pdf_url) in csv_rows:
        # pdf_url = 'https://www.twse.com.tw/staticFiles/news/news/tsecnews/ff80808171e8274501741fb4abc90cc5.pdf'
        # pdf_path, _headers = urlretrieve(pdf_url)

        # pdf_path = '/var/folders/v3/nz4nx80s31g36p_vb18sffs80000gn/T/tmp3hz67b1q'
        # pdf_path = 'ff80808171e8274501741fb4abc90cc5.pdf'  # table
        # pdf_path = 'ff80808171e82745017424e542830ce1.pdf'  # item
        # pdf_path = 'ff80808171e8274501741fbe652b0cc9.pdf'  # text
        # pdf_path = 'ff80808171e8274501741e97ae4b0ca9.pdf'  # list 1
        # pdf_path = 'ff80808171e8274501741053ddb40c93.pdf'  # list 2
        # pdf_path = 'ff80808171e827450174105133b00c8f.pdf'  # recursive 1
        # pdf_path = 'ff80808171e82745017405d701860c5c.pdf'  # recursive 2
        # pdf_path = 'ff80808171e827450173fb78e3d30bfa.pdf' # recursive 3
        # pdf_path = 'ff80808171e827450173dd01d5d10ae2.pdf' # recursive 4
        pdf_path = 'ff80808171e827450173db77690f0ab9.pdf'  # recursive 5
        
        paras = parse_pdf(pdf_path)
        for paragraph in paras:
            print(paragraph)

