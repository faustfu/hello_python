import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import re

BASE_URL = 'https://www.twse.com.tw'
LIST_URL = BASE_URL + \
    '/announcement/announcement?startDate=20200828&endDate=20200831&offset='
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
PAGE_OFFSET = 15


def next_page(page_number: int) -> str:
    offset = PAGE_OFFSET * page_number

    return LIST_URL + str(offset)


# 異步HTTP請求
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


def parser(url, html):
    title = None
    reference_no = None
    paragraphs = None

    item = BeautifulSoup(html, 'html.parser')
    trs = item.article.table.find_all('tr')

    for tr in trs:
        [key, value] = tr.find_all('td')

        key = key.get_text()
        if key == '主　　旨':
            title = value.get_text()
        elif key == '依　　據':
            reference_no = value.get_text()
        elif key == '公告事項':
            paragraphs = value.get_text().split('\r')
        else:
            continue

    return (title, reference_no, paragraphs)


async def download(announcement):
    async with aiohttp.ClientSession() as session:
        url = announcement[0]
        try:
            html = await fetch(session, url)

            (title, reference_no, paragraphs) = parser(url, html)

            announcement.append(title)
            announcement.append(reference_no)
            announcement.append(paragraphs)
        except aiohttp.client_exceptions.ClientConnectorError as e:
            print(url, e)


# 利用asyncio模塊進行異步IO處理
loop = asyncio.get_event_loop()
try:
    page_number = 0

    while True:
        announcements = []

        # 發送HTTP請求
        try:
            req = requests.get(next_page(page_number), headers=HEADERS)
            # 解析網頁
            summary = BeautifulSoup(req.text, 'html.parser')
            trs = summary.article.table.find_all(
                'tr')[1:]  # ignore table header
            for i, tr in enumerate(trs):
                if i > 1:
                    break  # debug

                tds = tr.find_all('td')[0:3]  # ignore dirty title

                [link, timestamp, no] = tds

                link = BASE_URL + link.find('a').get('href')
                timestamp = timestamp.get_text()
                no = no.get_text()

                announcements.append([link, timestamp, no])

            tasks = [asyncio.ensure_future(download(announcement))
                     for announcement in announcements]
            tasks = asyncio.gather(*tasks)
            loop.run_until_complete(tasks)
            # do other tasks
            for announcement in announcements:
                print(announcement)

            if len(announcements) <= 0:
                break
            else:
                page_number += 1
        except ConnectionRefusedError as e:
            print(e)

finally:
    loop.close()
