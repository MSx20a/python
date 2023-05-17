import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv
#from tool import openFriefoxBrowser

# 會有每執行一行就會開啟瀏覽器一次的bug


def testCase():
    """未輸入租戶的情形"""
    return
    load_dotenv()
    openFriefoxBrowser().find_element(By.ID, "AbpTenantSwitchLink").click()
    time.sleep(1)
    openFriefoxBrowser().find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(1)
    openFriefoxBrowser().find_element(
        By.ID, "LoginInput_UserNameOrEmailAddress"
    ).send_keys(os.getenv("third_userName"))
    openFriefoxBrowser().find_element(By.ID, "LoginInput_Password").send_keys(
        os.getenv("third_passWord")
    )
    openFriefoxBrowser().find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(5)
    warning = openFriefoxBrowser().find_element(By.CLASS_NAME, "show").text
    print(warning)


def testCase2():
    """成功打開租戶視窗"""
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
    driver.find_element(By.ID, "AbpTenantSwitchLink").click()
    time.sleep(1)
    try:
        modalTitle=driver.find_element(By.CSS_SELECTOR, "h5.m").text
        print(modalTitle)
        hope=driver.find_element(By.CSS_SELECTOR, "h5.modal-title").text
        print(hope)
    except NoSuchElementException:
        driver.close()
        pytest.fail("元素不存在")     
    assert modalTitle is not None,"元素不存在"
    driver.close()
    assert modalTitle==hope,"視窗開啟失敗"

@pytest.mark.parametrize("x, y, expected", [(2, 3, 5), (5, 7, 12)])
def test_addition(x, y, expected):
    assert x + y == expected

testCase2()