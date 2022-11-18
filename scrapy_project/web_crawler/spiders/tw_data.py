from pprint import pprint
from datetime import datetime
from web_crawler.items import WebCrawlerItem
import scrapy
import bs4
import re

class InsideSpider(scrapy.Spider):
    name = "tw_Data"  # 專案名稱
    # allowed_domains = ["www.taiwanstat.com"]  # 目標網站的網站
    start_urls = ["https://www.taiwanstat.com/"]  # 想要爬取的一至多個網頁網址清單

    def parse(self, respone):
        item=WebCrawlerItem()
        # print(respone.text)
        result = []
        loc_t = datetime.now()
        datetime_format = loc_t.strftime("%Y/%m/%d %H:%M:%S")  # 格式化時間
        soup = bs4.BeautifulSoup(respone.text, "lxml")
        contain = soup.select(
            "main.mdl-layout__content > a.image")  # 此網頁的a.image有24個
        #print(len(contain))
        for i in contain:
            if re.match(r"^http", i["href"]):  #正則表達式來篩選需要加上https://www.taiwanstat.com/的url
                url = i["href"]
            else:
                url = f'https://www.taiwanstat.com/{i["href"]}'

            data = {
                "title": i.select_one("h2.mdl-card__title-text").text,
                "url": url,
                "direction": i.select_one("div.mdl-card__supporting-text").text,
                "insert_time": datetime_format
            }
            # result.append(data)

            item["title"] = data["title"]
            item["url"]=data["url"]
            item["direction"]=data["direction"]
            item["insert_time"]=data["insert_time"]
            #print(item)
            yield item
        
        # print(data["url"])
        #pprint(result)
    