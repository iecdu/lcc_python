# -*- coding: utf-8 -*-
"""
    esunbank_rate 解析
"""

import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

url = "https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates"

esunbank = requests.get(url,headers=header).text

soup = BeautifulSoup(esunbank,"html.parser")

table = soup.find(id="exchangeRate")

tbody = table.find("tbody")
trs = tbody.find_all("tr")

for row in trs:
    tds = row.find_all("td",recursive=False) #recursice=False關閉遞迴搜尋
    if len(tds) == 4:
        print(tds[0].text.split()[0],tds[0].text.split()[1],)
        print(tds[1].text)
        print(tds[2].text)
        print(tds[3].text)
        print()
        
"""
recursice=False關閉遞迴搜尋
只抓下一層的子節點
"""

"""
row = table.find("div",class_="row")
m = row.text.split()
print(m[2],m[1])
"""
            
        
        
        