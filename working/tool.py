from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import pytest
import os
import time


def setup_browser():
    # 判斷使用的是哪種瀏覽器
    if webdriver.Chrome(executable_path=ChromeDriverManager().install()):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        return driver
    elif webdriver.Firefox(executable_path=GeckoDriverManager().install()):
        options = Options()
        options.add_argument("--disable-notifications")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
        driver.maximize_window()
        return driver
    elif webdriver.Edge(executable_path=EdgeChromiumDriverManager().install()):
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options)
        driver.maximize_window()
        return driver


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
        options = Options()
        options.add_argument("--disable-notifications")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
        driver.maximize_window()
        return driver
    elif num == 2:  # Chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        return driver
    elif num == 3:  # Edge
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options)
        driver.maximize_window()
        return driver


def loginBackStage(browser: str, group: str, userName: str, passWord: str):
    """三方後台登錄

    Args:
        browser (str): 輸入使用的瀏覽器friefox,chrome,edge
        group (str): 租戶
        userName (str): 帳號
        passWord (str): 密碼
    """
    load_dotenv()
    if browser == "friefox":
        driver = browserWebdriver(1)
    if browser == "chrome":
        driver = browserWebdriver(2)
    if browser == "edge":
        driver = browserWebdriver(3)
    driver.find_element(By.ID, "AbpTenantSwitchLink").click()
    time.sleep(1)
    driver.find_element(By.ID, "Input_Name").send_keys(group)
    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(1)
    driver.find_element(
        By.ID, "LoginInput_UserNameOrEmailAddress"
    ).send_keys(userName)
    driver.find_element(By.ID, "LoginInput_Password").send_keys(
        passWord
    )
    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(3)

# try:
#     testCase1()
# except NoSuchElementException:
#     pytest.fail("")

# driver=setup_browser();
# driver.get("https://google.com/")
