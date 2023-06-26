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
from tool import browserWebdriver

group = os.getenv("thirdGroup")
user = os.getenv("thirdUserName")
passWord = os.getenv("thirdPassWord")


def testCase4():
    """租戶視窗是否能輸入"""
    load_dotenv()
    driver = browserWebdriver(1)
    # driver.implicitly_wait(3)
    url = os.getenv("thirdUrl")
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.ID, "AbpTenantSwitchLink").click()
    time.sleep(3)
    try:
        hope = os.getenv("thirdGroup")
        driver.find_element(By.ID, "Input_Name").send_keys(hope)
        time.sleep(0.5)
        # 取得租戶輸入的值
        groupInput = driver.find_element(
            By.ID, "Input_Name").get_attribute("value")
        # print(groupInput)
        print(f"輸入租戶的值:{hope},取得輸入後的值:{groupInput}")
        # print(bodyClass2)
    except NoSuchElementException:
        driver.close()
        pytest.fail("找不到元素")
    driver.close()
    assert hope == groupInput, "關閉租戶視窗正常"

# def testCase1():
#     """語系切換"""
#     load_dotenv()
#     options = Options()
#     options.add_argument("--disable-notifications")
#     try:
#         driver = webdriver.Firefox(
#             service=FirefoxService(GeckoDriverManager().install())
#         )
#         driver.maximize_window()
#         url = os.getenv("thirdUrl")
#         driver.get(url)
#         time.sleep(2)
#     except Exception as e:
#         print(f"Error Massange：{str(e)}")
#     # print(len(comboBox))
#     try:
#         driver.find_element(By.ID, "languageDropdown").click()
#         comboBox = driver.find_elements(
#             By.CLASS_NAME, "dropdown-item")  # 抓取語言清單
#         href = driver.find_elements(
#             By.CSS_SELECTOR, "a.dropdown-item[href]")  # 抓取語言清單內的url
#         # print(len(comboBox))
#     except NoSuchElementException:
#         driver.close()
#         pytest.fail("元素不存在")
#     for i in range(len(comboBox)):

#         hope = href[i].text  # 取得超連結的文字
#         comboBox[i].click()
#         time.sleep(1)
#         language = driver.find_element(
#             By.ID, "languageDropdown").text  # 取得目前語言名稱
#         driver.find_element(By.ID, "languageDropdown").click()
#         # 第47~49行為避免selenium.common.exceptions.StaleElementReferenceException
#         # 指重新執行click()時會發生跳轉等變化，可能導致element status "過時"，所以須重新定位元素
#         comboBox = driver.find_elements(By.CLASS_NAME, "dropdown-item")
#         href = driver.find_elements(
#             By.CSS_SELECTOR, "a.dropdown-item[href]")
#         print(f"期望值(下拉選單的名稱)：{hope}")
#         # print(len(hope))
#         # print(type(hope))
#         print(f"選擇語言後跳轉的值：{language}")
#         # print(len(language))
#         assert hope[:3] == language[:3], "判斷語言名稱的前三個字"
#     driver.close()


@pytest.mark.parametrize("x, y, expected", [(2, 3, 5), (5, 7, 12)])
def test_addition(x, y, expected):
    assert x + y == expected


testCase4()
