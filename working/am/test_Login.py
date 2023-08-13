import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv
from tool import browserWebdriver, switchLanguage,loginBackStage

load_dotenv()
url = os.getenv("thirdUrl")


def testCase1():
    """登錄頁面-語系切換"""
    print("登錄頁面-語系切換")
    driver = browserWebdriver(1)
    driver.get(url)
    time.sleep(20)
    try:
        driver.find_element(By.CLASS_NAME, "dropdown-toggle").click()
        # 把下拉式選單combox內所有的語言存進list
        comboBox = driver.find_elements(By.CLASS_NAME, "dropdown-item")
        # 抓取語言清單內的url存進list
        href = driver.find_elements(
            By.CSS_SELECTOR, "a.dropdown-item[href]")
        # print(len(comboBox))
    except NoSuchElementException:
        driver.close()
        pytest.fail("Can not find element 'CLASS_NAME'")
    for i in range(len(comboBox)):
        # 取得超連結的文字
        hope = href[i].text
        comboBox[i].click()
        time.sleep(3)
        # 取得目前語言名稱
        language = driver.find_element(
            By.CLASS_NAME, "dropdown-toggle").text
        driver.find_element(By.CLASS_NAME, "dropdown-toggle").click()
        # 第41~43行為避免selenium.common.exceptions.StaleElementReferenceException
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
    # driver = browserWebdriver(1)
    # driver.get(url)
    driver = switchLanguage()
    time.sleep(3)
    try:

        account = driver.find_element(
            By.ID, "LoginInput_UserNameOrEmailAddress")
        password = driver.find_element(By.ID, "LoginInput_Password")
    except NoSuchElementException:
        driver.close()
        pytest.fail("Can not find element 'ID'")
    # 測試帳號密碼都沒填的情形
    driver.find_element(By.ID, "submitButton").click()
    result = driver.find_element(By.CLASS_NAME, "lpx-login-title").text
    print(f"沒有輸入帳密會留在登入畫面，並抓取其title：{result}")
    assert result == "登入", '"未填帳號密碼"之測試未通過'

    atCondition = ["", "al", "belmore"]
    pdCondition = ["", "123", "1qaz@WSX"]
    for i in atCondition:
        account.send_keys(i)
        if i == "":
            # 測試登入未填帳號的情形
            password.send_keys(pdCondition[2])
            driver.find_element(By.ID, "submitButton").click()
            result = driver.find_element(
                By.ID, "LoginInput_UserNameOrEmailAddress-error").text
            print(f"未輸入帳號的錯誤提示：{result}")
            hope = "欄位使用者名稱或郵箱地址不可為空."
            print(f"期望值：{hope}")
            assert result == hope, '"未填帳號"之情形未通過測試'
        elif i == "al":
            # 測試輸入不存在的帳號
            password.send_keys(pdCondition[2])
            driver.find_element(By.ID, "submitButton").click()
            time.sleep(2)
            result = driver.find_element(By.CLASS_NAME, "fade").text
            print(f"輸入不存在帳號的錯誤提示：{result}")
            hope = "使用者名稱或密碼無效!"
            print(f"期望值：{hope}")
            time.sleep(2)
            # 重新定位元素
            account = driver.find_element(
                By.ID, "LoginInput_UserNameOrEmailAddress")
            password = driver.find_element(By.ID, "LoginInput_Password")
            # 清除輸入框內的值
            account.clear()
            assert result == hope, '"輸入不存在的帳號"之情形未通過測試'
        elif i == "belmore":
            for i in pdCondition:
                password.send_keys(i)
                if i == "":
                    # 測試未輸入密碼
                    driver.find_element(By.ID, "submitButton").click()
                    result = driver.find_element(
                        By.ID, "LoginInput_Password-error").text
                    print(f"未輸入密碼的情形：{result}")
                    hope = "欄位密碼不可為空."
                    print(f"期望值：{hope}")
                    assert result == hope, '"測試未輸入密碼"之情形未通過測試'
                if i == "123":
                    # 測試輸入錯誤的密碼
                    driver.find_element(By.ID, "submitButton").click()
                    time.sleep(2)
                    result = driver.find_element(By.CLASS_NAME, "fade").text
                    print(f"輸入錯誤密碼的錯誤提示：{result}")
                    hope = "使用者名稱或密碼無效!"
                    print(f"期望值：{hope}")
                    time.sleep(2)
                    # 重新定位元素
                    account = driver.find_element(
                        By.ID, "LoginInput_UserNameOrEmailAddress")
                    password = driver.find_element(
                        By.ID, "LoginInput_Password")
                    # 清除密碼欄位內的值
                    password.clear()
                    assert result == hope, '"輸入錯誤的密碼"之情形未通過測試'
                elif i == "1qaz@WSX":
                    # 測試輸入正確的密碼
                    driver.find_element(By.ID, "submitButton").click()
                    time.sleep(10)
                    # class:lpx-menu-item-text，共有抓到66個
                    result = driver.find_elements(
                        By.CLASS_NAME, "lpx-menu-item-text")[48].text
                    print(f"輸入正確密碼成功登錄並獲取userName：{result}")
                    hope = atCondition[2]
                    assert result.lower() == hope.lower(), '"輸入正確的密碼"之情形未通過測試'
    driver.close()

def testCase3():
    "測試首頁和搜尋欄位"
    driver=loginBackStage(2,"belmore","1qaz@WSX")
    homeMessage=driver.find_element(By.TAG_NAME,"h2").text
    print(homeMessage)
    #hidden-in-hover-trigger
    pass

if __name__ == "__main__":
    #pass
    # testCase1()
    # testCase2()
    testCase3()