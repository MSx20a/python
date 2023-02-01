import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url="https://24h.pchome.com.tw/store/DHAK5S"
result=requests.get(url)
result.encoding="utf8"
soup=BeautifulSoup(result.text,"lxml")
print(soup)
#將爬到的網頁整個存下來方便查看與找取元素
with open("myfile.html",mode="w") as f:
    f.write(soup)


# 17-19行是讓瀏覽器在背景執行
ops=webdriver.FirefoxOptions()
ops.headless=True
driver=webdriver.Firefox(options=ops)
#driver=webdriver.Firefox()
x=driver.get("https://24h.pchome.com.tw/store/DHAK5S")
element=driver.find_elements(By.XPATH,"//h5")  #取得網頁的文字檔
# for i in element:
#     print(i.text)

css=driver.find_elements(By.CSS_SELECTOR,"h5.nick > a")
print(type(css))
for i in css:
    print(i.get_attribute("href"))
y=driver.get(css[1].get_attribute("href"))


