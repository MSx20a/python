from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

# 第8、9、12為載入環境變數
load_dotenv()

# 第8~9行是用來取消網頁中的彈出視窗
options = Options()
options.add_argument("--disable-notifications")

"""
此selenium版本為4.9.0，使用webdriver_manager及第2~3行來解決
OSError: [WinError 216] 此版本的 %1 與您執行的 Windows 版本不相容。請檢查電腦的系統資訊，然後連絡軟體發行者。
"""
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()  # 設定開啟的網頁視窗要最大化
url = "https://leetcode.com/accounts/login/"
driver.get(url)
time.sleep(5)

try:
    userName = os.getenv("leetCode_UserName")
    passWord = os.getenv("leetCode_passWoed")
    print(userName)
    # search = driver.find_element(By.ID, "search").send_keys("news")  #youtube search id
    userNameInput = driver.find_element(
        By.ID, 'id_login').send_keys(userName)
    passwordInput = driver.find_element(
        By.ID, "id_password").send_keys(passWord)
    time.sleep(1)
    signIn = driver.find_element(
        By.ID, "signin_btn").send_keys(Keys.ENTER)
except Exception as e:
    print(e)

time.sleep(5)
driver.get("https://leetcode.com/problemset/all/")
time.sleep(2)
driver.save_screenshot("result")  # 網頁截圖
target = driver.find_element(By.CSS_SELECTOR, ".top-1\/2 > div:nth-child(1)")
result = target.text.split("\n")
print(f"總刷題數：{result}")
driver.close()
