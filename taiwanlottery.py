"""
    台灣彩卷
"""
import requests
from bs4 import BeautifulSoup

url = "https://www.taiwanlottery.com.tw/index_new.aspx"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }

data = requests.get(url,headers = header).text 
soup = BeautifulSoup(data,"html.parser")

Bingo = soup.find("div",class_="contents_box01")

Bingo_date = Bingo.find("span",class_="font_black15")
print("Bingo Bingo\n{}".format(Bingo_date.text))

Bingo_title = Bingo.find("div",class_="contents_mine_tx04")
print(Bingo_title.text)

Bingo_number = Bingo.find_all("div",class_="ball_tx ball_yellow")
#print(Bingo_number)
Bingo_number1 = Bingo_number[:10]
Bingo_number2 = Bingo_number[10:]
for item in Bingo_number1:
    print(item.text,end=" ")
print()
for item in Bingo_number2:
    print(item.text,end=" ")
print()

sepcial = Bingo.find_all("div",class_="contents_mine_tx08")
s1=[]
for item in sepcial[0]:
    s1.append(item.text.strip())
print("{}{:3}{}".format(s1[0],s1[2],s1[4]))

s2=[]
for item in sepcial[1]:
    s2.append(item.text.strip())
print("{}{:5}{}".format(s2[0],s2[2],s2[4]))
s3=[]
for item in sepcial[2]:
    s3.append(item.text.strip())
print("{}{:5}{}".format(s3[0],s3[2],s3[4]))
print("--------------------------------------------")

WinWin = soup.find_all("div",class_="contents_box06")

WinWin_date = WinWin[0].find("span",class_="font_black15")
#   使用find_all，WinWin後面要加索引[0]才不會錯誤
print("雙贏彩\n{}".format(WinWin_date.text))

title = WinWin[0].find("div",class_="contents_mine_tx04")
#print(title.text)
WinWin_title=[]
for item in title:
    WinWin_title.append(item)
print(WinWin_title[0],end=" ")

number = WinWin[0].find_all("div",class_="ball_tx ball_blue")
WinWin_numbers1 = number[:12]
WinWin_numbers2 = number[12:]
for n in WinWin_numbers1:
    print(n.text,end=" ")
print()
print(WinWin_title[2],end=" ")
for n in WinWin_numbers2:
    print(n.text,end=" ")
print()
print("--------------------------------------------")
#   威力彩及大樂透共用class，使用find_all 解決
fourin1 = soup.find_all("div",class_="contents_box02")
#print(fourin1[2])

Power_date = fourin1[0].find("span",class_="font_black15")
print("威力彩\n{}".format(Power_date.text))

title = fourin1[0].find("div",class_="contents_mine_tx04")
#print(title)
Power_title=[]
for item in title:
    Power_title.append(item)
print(Power_title[0],end=" ")

number = fourin1[0].find_all("div",class_="ball_tx ball_green")
#print(number)
Power_number1 = number[:6]
Power_number2 = number[6:]
for item in Power_number1:
    print(item.text,end=" ")
print()
print(Power_title[2],end=" ")
for item in Power_number2:
    print(item.text,end=" ")
print()
sepcial = fourin1[0].find("div",class_="ball_red")
print("{:6}{}".format(Power_title[4],sepcial.text),end=" ")
print()
print("--------------------------------------------")

Bighappy_date = fourin1[2].find("span",class_="font_black15")
print("大樂透\n{}".format(Bighappy_date.text))

title = fourin1[2].find("div",class_="contents_mine_tx04")
Bighappy_title=[]
for item in title:
    Bighappy_title.append(item)
print(Bighappy_title[0].text,end=" ")

number = fourin1[2].find_all("div",class_="ball_tx ball_yellow")
Bighappy_number1 = number[:6]
Bighappy_number2 = number[6:]
for item in Bighappy_number1:
    print(item.text,end=" ")
print()
print(Bighappy_title[2],end=" ")
for item in Bighappy_number2:
    print(item.text,end=" ")
print()
special = fourin1[2].find("div",class_="ball_red")
print("{:6}{}".format(Bighappy_title[4],special.text))
print("--------------------------------------------")

FTN = soup.find("div",class_="contents_box03")

FTN_date = FTN.find("span",class_="font_black15")
print("今彩539\n{}".format(FTN_date.text))

title = FTN.find("div",class_="contents_mine_tx04")
FTN_title=[]
for item in title:
    FTN_title.append(item)
print(FTN_title[0].text,end=" ")

number = FTN.find_all("div",class_="ball_tx ball_lemon")
FTN_number1 = number[:5]
FTN_number2 = number[5:]
for item in FTN_number1:    
    print(item.text,end=" ")
print()
print(FTN_title[2].text,end=" ")
for item in FTN_number2:
    print(item.text,end=" ")
print()
print("--------------------------------------------")
#   三星彩及四星彩共用class，使用find_all 解決
Star = soup.find_all("div",class_="contents_box04")

Tstar_date = Star[0].find("span",class_="font_black15")
print("三星彩\n{}".format(Tstar_date.text))

Tstar_title = Star[0].find("div",class_="contents_mine_tx04")
print(Tstar_title.text,end=" ")

Tstar_number = Star[0].find_all("div",class_="ball_tx ball_purple")

for item in Tstar_number:
    print(item.text,end=" ")
print()
print("--------------------------------------------")

Fstar_date = Star[1].find("span",class_="font_black15")
print("四星彩\n{}".format(Fstar_date.text))

Fstar_title = Star[1].find("div",class_="contents_mine_tx04")
print(Fstar_title.text,end=" ")

Fstar_number = Star[1].find_all("div",class_="ball_tx ball_purple")
for item in Fstar_number:
    print(item.text,end=" ")
print()


"""
print("===== 左右摆放 =====")

Star = soup.find_all("div",class_="contents_box04")

Tstar_date = Star[0].find("span",class_="font_black15")
Fstar_date = Star[1].find("span",class_="font_black15")
print("三星彩                     四星彩")
print("{:25}{}".format(Tstar_date.text,Fstar_date.text))

Tstar_title = Star[0].find("div",class_="contents_mine_tx04")
print(Tstar_title.text,end=" ")

Tstar_number = Star[0].find_all("div",class_="ball_tx ball_purple")
number=[]
for item in Tstar_number:
    print(item.text,end=" ")
print("",end="            ")
Fstar_title = Star[1].find("div",class_="contents_mine_tx04")
print(Fstar_title.text,end=" ")

Fstar_number = Star[1].find_all("div",class_="ball_tx ball_purple")
for item in Fstar_number:
    print(item.text,end=" ")
print()
"""



