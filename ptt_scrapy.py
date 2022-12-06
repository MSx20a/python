import requests
import datetime
from bs4 import BeautifulSoup
from pprint import pprint
from pymongo_d import insert_doc
# from read_pymongo

ans = []  # 建立一個empty list用來存取爬下來的網頁內容
time_Now = datetime.datetime.now()  # 使用datetime模組抓取當下時間
ptt_Url = "https://ptt.cc"
url = "https://www.ptt.cc/bbs/index.html"
result = requests.get(url)
# 目前得到result的資料類型為requests.models.Response，常用的屬性有
# .text 響應回傳的網頁內容（str）
# .content 響應回傳的內容（binary），一般用来爬取影片
# .status_code 響應狀態碼
# .url 獲取請求地址
# .cookies 獲取返回的cookies訊息
# .cookies.get_dict() 獲取返回的cookies訊息
# .request 獲取請求方式
# print(result.text)
soup = BeautifulSoup(result.text, "lxml")  # 可以將css,html內的element抓取出來,lxml是解析器
# print(soup)
# select=soup.select("div.b-list-container.action-bar-margin.bbs-screen > div > a > div")
# 選擇需要爬的html內容，使用select，print出的資料屬於list
select = soup.select(
    "#main-container > div.b-list-container.action-bar-margin.bbs-screen > div")
# print(select.text)
for i in select:
    # print(i)
    # print()
    data_Ptt = {
        # "url":f'{ptt_Url}{i.select_one("a.board")["href"]}',  #爬取url的另一種做法
        # attrs is Searching by CSS class
        "url": f'{ptt_Url}{i.find("a").attrs["href"]}',
        "name": i.select_one("a > div.board-name").text,
        "nuser": i.select_one("a > div.board-nuser").text,
        "class": i.select_one("a > div.board-class").text,
        "title": i.select_one("a > div.board-title").text,
        # "create_time":time_Now.strftime("%Y/%m/%d %H:%M:%S")
        "create_time": datetime.datetime.now()
    }

    ans.append(
        # 將需要的資料加進list中
        # select,select_one的data type is bs4.element.Tag直接print會把html的element也打印出來；
        # 所以要網頁內容料爬出來需再後面加上.text轉成str
        data_Ptt

    )

    insert_doc(data_Ptt, 'ptt')
    # break
# print(ans)
