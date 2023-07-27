from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time


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

def checkElement():
    """判斷元素"""
    

def loginBackStage(num: str, group: str, userName: str, passWord: str):
    """三方後台登錄

    Args:
        num (int): 請輸入瀏覽器編號：1.friefox 2.chrome 3.edge
        group (str): 租戶
        userName (str): 帳號
        passWord (str): 密碼
    """

    if num == 1:  # Firefox
        options = Options()
        options.add_argument("--disable-notifications")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
        driver.maximize_window()
        driver.get("https://app-third.mymine.one/?iss=https:%2F%2Fauth-third.mymine.one%2F")
    elif num == 2:  # Chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get("https://app-third.mymine.one/?iss=https:%2F%2Fauth-third.mymine.one%2F")
    elif num == 3:  # Edge
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options)
        driver.maximize_window()
        driver.get("https://app-third.mymine.one/?iss=https:%2F%2Fauth-third.mymine.one%2F")

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

    return driver

# driver = browserWebdriver(1)
# driver.get("http://google.com/")

#目前會卡在登入後沒有等網頁加載完就做跳轉至quick-start頁面，而導致出錯
# driver = loginBackStage(1, "fae", "alvin", "1qaz@WSX")
# # time.sleep(6)
# driver.implicitly_wait(5)
# driver.get("https://app.third.mymine.one/banker/quick-start")
# x = driver.find_element(By.CLASS_NAME, "content-header-title").text
# print(x)
# https://app.third.mymine.one/?iss=https:%2F%2Fauth.third.mymine.one%2F
