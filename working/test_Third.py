import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv


class TestThird:
    """自動化測試

    Args:
        unittest (_type_): 三方後台登錄頁面測試
    """

    def testCase1(self):
        """語系切換
        """
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
        driver.find_element(By.ID, "languageDropdown").click()
        comboBox = driver.find_elements(By.CLASS_NAME, "dropdown-item")
        href = driver.find_elements(By.CSS_SELECTOR, "a.dropdown-item[href]")
        # print(len(comboBox))
        for i in range(len(comboBox)):
            hope = href[i].text
            comboBox[i].click()
            time.sleep(1)
            language = driver.find_element(By.ID, "languageDropdown").text
            driver.find_element(By.ID, "languageDropdown").click()
            # 第47~49行為避免selenium.common.exceptions.StaleElementReferenceException
            # 指重新執行click()時會發生跳轉等變化，可能導致element status "過時"
            comboBox = driver.find_elements(By.CLASS_NAME, "dropdown-item")
            href = driver.find_elements(
                By.CSS_SELECTOR, "a.dropdown-item[href]")
            # print(len(hope))
            print(f"期望值(下拉選單的名稱)：{hope}")
            # print(len(language))
            print(f"選擇語言後跳轉的值：{language}")
            assert hope[:2] == language[:2], "判斷語言名稱的前三個字"
            #assert hope == language
        driver.close()

    @pytest.mark.loginSusses
    def testCase(self):
        """登入成功的情形"""
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
        driver.find_element(By.ID, "Input_Name").send_keys("fae")
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(1)
        driver.find_element(
            By.ID, "LoginInput_UserNameOrEmailAddress"
        ).send_keys(os.getenv("third_userName"))
        driver.find_element(By.ID, "LoginInput_Password").send_keys(
            os.getenv("third_passWord")
        )
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(5)
        # 因為無法直接定位，所以尋找所有span標籤發現userName在第67項
        elementText = driver.find_elements(By.CSS_SELECTOR, "span")[
            66
        ].text
        hope = os.getenv("third_userName")
        print("此為登錄的自動測試")
        print(f"期望值：{hope}")
        print(f"頁面元素：{elementText}")
        # print(elementText)
        driver.close()
        assert elementText == hope, "登錄正常"

    @pytest.mark.NotChooseGroup
    def testCase3(self):
        """未輸入租戶的情形"""
        pass

    # def testCase3(self):
    #     """登錄不成功的情形，未填帳號"""
    #     self.driver.find_element(By.ID, "AbpTenantSwitchLink").click()
    #     time.sleep(0.5)
    #     self.driver.find_element(By.ID, "Input_Name").send_keys("demo")
    #     self.driver.find_element(By.CLASS_NAME, "btn-primary").click()
    #     time.sleep(2)
    #     self.driver.find_element(By.ID, "LoginInput_Password").send_keys(
    #         os.getenv("third_passWord"))
    #     self.driver.find_element(By.CLASS_NAME, "btn-primary").click()
    #     result = self.driver.find_element(
    #         By.CSS_SELECTOR, "#LoginInput_UserNameOrEmailAddress[data-val-required]").get_attribute("data-val-required")
    #     print(result)
    #     hope = "欄位使用者名稱或郵箱地址不可為空."
    #     self.assertIn(hope, result)

    # def tearDown(self) -> None:
    #     time.sleep(3)
    #     self.driver.close()

    # def testCase1(self):
    #     i = Calculator(6, 8)
    #     result = i.add()
    #     hope = 14
    #     self.assertEqual(result, hope, "加法運算錯誤")


# if __name__ == "__main__":
#     go = TestThird()
#     go.testCase1()
