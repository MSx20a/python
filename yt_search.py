from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.by import By
from pprint import pprint


options = Options()
options.add_argument("--disable-notifications")

driver = webdriver.Firefox()
driver.maximize_window()
url = "https://www.youtube.com"
driver.get(url)
time.sleep(2)

search = driver.find_element(By.NAME, "search_query").send_keys("機車")
time.sleep(2)
submit = driver.find_element(By.ID, "search-icon-legacy").click()
time.sleep(2)
datas = driver.find_elements(By.CSS_SELECTOR, "#video-title[title][href]")
# print(len(datas))
result = []
for data in datas:
    # print(type(data))
    # print(data)
    resultElement = {}
    title = data.get_attribute("title")
    href = data.get_attribute("href")
    resultElement[title] = href
    result.append(resultElement)
    # break
print(len(result))
pprint(result)
time.sleep(2)
driver.close()
