import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv



def getUrl():
    try:
        options = Options()
        options.add_argument("--disable-notifications")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
        driver.maximize_window()
        url = os.getenv("third_url")
        driver.get(url)
        # driver.execute("get",{"url":url})
        time.sleep(1)
    except Exception as e:
        print(f"Error Massange：{str(e)}")
    return driver


# @pytest.mark.__str__
def test_Case1():
    """登入成功的情形"""
    load_dotenv()
    getUrl().find_element(By.ID, "AbpTenantSwitchLink").click()
    time.sleep(0.5)
    getUrl().find_element(By.ID, "Input_Name").send_keys("demo")
    getUrl().find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(2)
    getUrl().find_element(By.ID, "LoginInput_UserNameOrEmailAddress").send_keys(
        os.getenv("third_userName")
    )
    getUrl().find_element(By.ID, "LoginInput_Password").send_keys(
        os.getenv("third_passWord")
    )
    getUrl().find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(5)
    # 因為無法直接定位，所以尋找所有span標籤發現userName在第67項
    elementText = getUrl().find_elements(By.ID, "span")[66].text
    hope = os.getenv("third_userName")
    # Wprint(elementText)
    getUrl().close()
    assert elementText == hope

test_Case1()