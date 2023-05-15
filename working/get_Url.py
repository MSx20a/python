from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv


class MyTest:
    """自動化測試

    Args:
        unittest (_type_): _description_
    """

    def __init__(self) -> None:
        # 初始化條件
        # print(self)
        # print(type(self))
        self.options = Options()  # 實例化Options()
        self.env = load_dotenv()
        self.open_Third_Url = self.getUrl()

    def getUrl(self):
        self.options.add_argument("--disable-notifications")
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

    def test_Case1(self):
        """登入成功的情形"""
        self.open_Third_Url.find_element(By.ID, "AbpTenantSwitchLink").click()
        time.sleep(1)
        self.open_Third_Url.find_element(By.ID, "Input_Name").send_keys("demo")
        self.open_Third_Url.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(2)
        self.open_Third_Url.find_element(
            By.ID, "LoginInput_UserNameOrEmailAddress"
        ).send_keys(os.getenv("third_userName"))
        self.open_Third_Url.find_element(By.ID, "LoginInput_Password").send_keys(
            os.getenv("third_passWord")
        )
        self.open_Third_Url.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(5)
        # 因為無法直接定位，所以尋找所有span標籤發現userName在第67項
        elementText = self.open_Third_Url.find_elements(By.CSS_SELECTOR, "span")[
            66
        ].text
        hope = os.getenv("third_userName")
        # Wprint(elementText)
        self.open_Third_Url.close()
        assert elementText == hope, "登錄功能正常"

    def test_Case2(self):
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


go = MyTest()
go.test_Case1()
