import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv
from tool import browserWebdriver

load_dotenv()
url = os.getenv("thirdUrl")


def testCase1():
    """登錄頁面-語系切換"""
    print("登錄頁面-語系切換")
    driver = browserWebdriver(1)
    driver.get(url)
    driver.implicitly_wait(15)
    # time.sleep(20)
    try:
        driver.find_element(By.CLASS_NAME, "dropdown-toggle").click()
        # 把下拉式選單combox內所有的語言存進list
        comboBox = driver.find_elements(By.CLASS_NAME, "dropdown-item")
        # 抓取語言清單內的url
        href = driver.find_elements(
            By.CSS_SELECTOR, "a.dropdown-item[href]")
        # print(len(comboBox))
    except NoSuchElementException:
        pytest.fail("Can not find element 'CLASS_NAME'")
    for i in range(len(comboBox)):
        # 取得超連結的文字
        hope = href[i].text
        comboBox[i].click()
        # time.sleep(2)
        # 取得目前語言名稱
        language = driver.find_element(
            By.CLASS_NAME, "dropdown-toggle").text
        driver.find_element(By.CLASS_NAME, "dropdown-toggle").click()
        # 第46~50行為避免selenium.common.exceptions.StaleElementReferenceException
        # 指重新執行click()時會發生跳轉等變化，可能導致element status "過時"，所以須重新定位元素
        comboBox = driver.find_elements(By.CLASS_NAME, "dropdown-item")
        href = driver.find_elements(
            By.CSS_SELECTOR, "a.dropdown-item[href]")
        print(f"期望值(下拉選單的名稱)：{hope}")
        # print(len(hope))
        # print(type(hope))
        print(f"選擇語言後跳轉的值：{language}")
        assert hope[:2] == language[:2], "判斷語言名稱的前三個字"
    #     # assert hope == language
    driver.close()


def testCase2():
    """登錄頁面的帳號密碼測試"""
    print("登錄頁面的帳號密碼測試")
    driver = browserWebdriver(1)
    driver.get(url)
    driver.implicitly_wait(15)
    # time.sleep(20)
    try:
        account = driver.find_element(
            By.ID, "LoginInput_UserNameOrEmailAddress")
        password = driver.find_element(By.ID, "LoginInput_Password")
    except NoSuchElementException:
        pytest.fail("Can not find element 'ID'")
    atCondition = ["", "al", "Belmore"]
    pdCondition = ["123", "1qaz@WSX"]
    for i in atCondition:
        account.send_keys(i)
        if i == "":
            # 測試登入未填帳號的情形
            password.send_keys(pdCondition[1])
            driver.find_element(By.ID, "submitButton").click()
            result = driver.find_element(
                By.ID, "LoginInput_UserNameOrEmailAddress-error").text
            print(f"未輸入帳號的錯誤提示：{result}")
        elif i == "al":
            # 測試輸入不存在的帳號
            password.send_keys(pdCondition[1])
            driver.find_element(By.ID, "submitButton").click()
            # time.sleep(2)
            result = driver.find_element(By.CLASS_NAME, "fade").text
            print(f"輸入不存在帳號的錯誤提示：{result}")
            driver.find_element(By.CLASS_NAME, "btn-primary").click()
            # time.sleep(2)
            account = driver.find_element(
                By.ID, "LoginInput_UserNameOrEmailAddress")
            password = driver.find_element(By.ID, "LoginInput_Password")
        elif i == "Belmore":
            for i in pdCondition:
                password.send_keys(i)
                if i == "123":
                    # 測試輸入錯誤的密碼
                    driver.find_element(By.ID, "submitButton").click()
                    # time.sleep(2)
                    result = driver.find_element(By.CLASS_NAME, "fade").text
                    print(f"輸入錯誤密碼的錯誤提示：{result}")
                    driver.find_element(By.CLASS_NAME, "btn-primary").click()
                    # time.sleep(2)
                    account = driver.find_element(
                        By.ID, "LoginInput_UserNameOrEmailAddress")
                    password = driver.find_element(
                        By.ID, "LoginInput_Password")
                elif i == "1qaz@WSX":
                    # 測試輸入正確的密碼
                    driver.find_element(By.ID, "submitButton").click()
                    # time.sleep(10)
                    result = driver.find_element(
                        By.CLASS_NAME, "lpx-menu-item-text").text
                    print(f"輸入正確密碼成功登錄並獲取userName：{result}")
                    hope=pdCondition(1)
    driver.close()


if __name__ == "__main__":
    # testCase1()
    testCase2()
