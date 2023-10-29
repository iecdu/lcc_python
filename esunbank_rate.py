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
trs = tbody.find_all("tr",recursive=False)[1:]  #recursice=False關閉遞迴搜尋

for row in trs:
    tds = row.find_all("td",recursive=False)    #recursice=False關閉遞迴搜尋
    currency = tds[0].text.split()
    currencyIn = tds[0].text.split()[2]
    currencyOut = tds[0].text.split()[3]
    """即期匯率"""
    spotRate = tds[1].text.strip().split()

    #print(len(tds))
    print(currency[0],currency[1])     
    print(currencyIn + ":" + spotRate[0])
    print(currencyOut + ":" + spotRate[1])    
    print(tds[2].text.strip()) 
    print(tds[3].text.strip())
    print()
    # tds[2]、tds[3]包含銀行買入、銀行賣出 兩個數值
    
"""     recursice=False 關閉遞迴搜尋     
        否则tr、td會重複抓到以下子截點 [] [銀行買入] [銀行賣出]

<table class="d-lg-none bankState">
    <tbody>
    <tr>
        <td label=""></td>
        <td label="即期匯率">
            銀行買入
        </td>
        <td label="網銀/App優惠">
            銀行賣出
        </td>
    </tr>
    </tbody>
</table
"""