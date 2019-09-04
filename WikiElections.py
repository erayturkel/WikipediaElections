# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup as bs

website_url=requests.get("https://en.wikipedia.org/wiki/2000_United_States_House_of_Representatives_elections#Complete_list").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})


for table in My_tables[1:]:
    for row in table.findAll('tr'):
        cells=row.findAll('td')
        for cell in cells:
            print(cell.text)