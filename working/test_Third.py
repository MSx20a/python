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

    # @pytest.mark.loginSusses
    def test_Case1(self):
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
        driver.find_element(By.ID, "Input_Name").send_keys("demo")
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
        print(f"期望值：{hope}")
        print(f"頁面元素：{elementText}")
        # Wprint(elementText)
        driver.close()
        assert elementText == hope, "登錄不正常"

    # @pytest.mark.NotChooseGroup
    # def test_Case2(self):
    #     """未輸入租戶的情形"""
    #     pass

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


go = TestThird()
go.test_Case1()
# if __name__ == "__main__":
#     go = MyTest()
#     go.test_Case1()
#     pytest.main()
# print(__name__)
# unittest.main()
# 將多個testCase組裝為一個測試套件
# suite = unittest.TestSuite()
# suite.addTest(MyTest("testCase1"))
# suite.addTest(MyTest("testCase3"))
# dirPath = os.path.dirname(__file__)
# logger.debug(f"結果:{dirPath}")
# reportPath = os.path.join(dirPath, "report.html")
# report = open(reportPath, mode="w+", encoding="utf-8")
# 定義報告的格式
# with open(reportPath, mode="w", encoding="utf-8") as f:
#     runner = WinPath(output=f, title="測試報告", description="後臺登錄情形")
#     runner.run(suite)
# runner = HTMLTestRunner(output=report, title="測試報告", description="後臺登錄情形")
# runner.run(suite)
# report.close()
