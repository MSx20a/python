from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
import time
import os
from dotenv import load_dotenv
import re

load_dotenv()
url = os.getenv("thirdUrl")


def browserWebdriver(num: int):
    """開啟瀏覽器

    Args:
        num (int): 請輸入瀏覽器編號
        1.friefox
        2.chrome
        3.edge
    Returns:
        _type_: webdriver
    """
    if num == 1:  # Firefox
        options = Options()  # 用來配置和設置瀏覽器的各種選項和參數
        options.add_argument("--disable-notifications")  # 禁用瀏覽器的通知
        options.add_argument("--headless")  # 在背景執行
        driver = webdriver.Firefox(
            service=FirefoxService(
                GeckoDriverManager().install(), options=options)
        )
        driver.maximize_window()
        return driver
    elif num == 2:  # Chrome
        options = Options()  # 用來配置和設置瀏覽器的各種選項和參數
        options.add_argument("--disable-notifications")  # 禁用瀏覽器的通知
        # options.add_argument("--headless")  # 在背景執行
        # service=ChromeService("/Users/chenyoucheng/Desktop/code/python_code/working/am/chromedriver")
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        return driver
    elif num == 3:  # Edge
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options)
        driver.maximize_window()
        return driver


def checkElement():
    """判斷元素"""


def loginBackStage(num: str, userName: str, passWord: str):
    """三方後台登錄

    Args:
        num (int): 請輸入瀏覽器編號：1.friefox 2.chrome 3.edge
        userName (str): 帳號
        passWord (str): 密碼
    """
    driver = switchLanguage()

    try:
        account = driver.find_element(
            By.ID, "LoginInput_UserNameOrEmailAddress")
        password = driver.find_element(By.ID, "LoginInput_Password")
        login = driver.find_element(By.ID, "submitButton")
    except NoSuchElementException:
        pytest.fail("Can not find element 'ID'")
    account.send_keys(userName)
    password.send_keys(passWord)
    login.click()
    time.sleep(10)
    # result = driver.find_elements(By.CLASS_NAME, "lpx-menu-item-text")
    # for index,i in enumerate(result):
    #     print(f"{index},{i.text}")

    return driver


def switchLanguage():
    driver = browserWebdriver(1)
    driver.get(url)
    time.sleep(15)
    try:
        driver.find_element(By.CLASS_NAME, "dropdown-toggle").click()
        comboBox = driver.find_elements(By.CLASS_NAME, "dropdown-item")
        href = driver.find_elements(By.CSS_SELECTOR, "a.dropdown-item[href]")
    except NoSuchElementException:
        pytest.fail("Can not find element 'CLASS_NAME'")
    for i in range(len(comboBox)):
        if href[i].text == "繁體中文 / ZH":
            comboBox[i].click()
            break

    return driver


def sr():
    myList = ["銀行管理(Admin)", "銀行管理", "銀行卡管理", "銀行卡控制台", "電腦列表", "建單紀錄", "管理"]
    wd = ["銀", "銀行", "行", "管理", "理", "建單", "控制"]
    r = re.compile("管理")  # 設定查找的字串
    result = []
    for i in myList:
        if r.search(i):  # 會搜尋字串並返回成功匹配的
            result.append(i)


if __name__ == "__main__":
    # switchLanguage()
    # loginBackStage(1,"Belmore","1qaz@WSX")
    sr()
    browserWebdriver(2)
