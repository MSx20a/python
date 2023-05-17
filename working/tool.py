from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

def openFriefoxBrowser():
    """開啟火狐瀏覽器"""
    load_dotenv()
    options = Options()
    options.add_argument("--disable-notifications")
    try:
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
        driver.maximize_window()
        url = os.getenv("third_url")
        driver.get(url)
        time.sleep(2)
    except Exception as e:
        print(f"Error Massange：{str(e)}")
    return driver
def loginSuccess():
    """成功登錄三方後台"""
    pass
