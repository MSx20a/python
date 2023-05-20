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


class TestThird:
    """自動化測試

    Args:
        unittest (_type_): 三方後台登錄頁面測試
    """

    def testCase1(self):
        """登錄頁面-語系切換"""
        load_dotenv()
        driver=browserWebdriver(1)
        url = os.getenv("thirdUrl")
        driver.get(url)
        time.sleep(2)
        try:
            driver.find_element(By.ID, "languageDropdown").click()
            #把下拉式選單combox內所有的語言存進list
            comboBox = driver.find_elements(By.CLASS_NAME, "dropdown-item")
            # 抓取語言清單內的url
            href = driver.find_elements(By.CSS_SELECTOR, "a.dropdown-item[href]")
            # print(len(comboBox))
        except NoSuchElementException:
            pytest.fail("抓取不到元素")
        for i in range(len(comboBox)):
            # 取得超連結的文字
            hope = href[i].text
            comboBox[i].click()
            time.sleep(1)
            # 取得目前語言名稱
            language = driver.find_element(By.ID, "languageDropdown").text
            driver.find_element(By.ID, "languageDropdown").click()
            # 第47~49行為避免selenium.common.exceptions.StaleElementReferenceException
            # 指重新執行click()時會發生跳轉等變化，可能導致element status "過時"，所以須重新定位元素
            comboBox = driver.find_elements(By.CLASS_NAME, "dropdown-item")
            href = driver.find_elements(
                By.CSS_SELECTOR, "a.dropdown-item[href]")
            print(f"期望值(下拉選單的名稱)：{hope}")
            # print(len(hope))
            # print(type(hope))
            print(f"選擇語言後跳轉的值：{language}")
            # print(len(language))
            assert hope[:3] == language[:3], "判斷語言名稱的前三個字"
            # assert hope == language
        driver.close()

    # @pytest.mark.NotChooseGroup
    def testCase2(self):
        """成功打開租戶視窗"""
        load_dotenv()
        driver=browserWebdriver(1)
        url = os.getenv("thirdUrl")
        driver.get(url)
        time.sleep(2)
        driver.find_element(By.ID, "AbpTenantSwitchLink").click()
        time.sleep(1)
        try:
            modalTitle=driver.find_element(By.CSS_SELECTOR, "h5.modal-title").text
            #print(modalTitle)
            hope=driver.find_element(By.CSS_SELECTOR, "h5.modal-title").text
            print(f"{hope}={modalTitle},有定位到元素...視窗開啟成功")
        except NoSuchElementException:
            driver.close()
            pytest.fail("元素不存在")     
        driver.close()
        assert modalTitle==hope,"視窗開啟失敗"

    def testCase3(self):
        """關閉租戶視窗"""
        load_dotenv()
        driver = browserWebdriver(1)
        url = os.getenv("thirdUrl")
        driver.get(url)
        time.sleep(5)
        try:
            driver.find_element(By.ID, "AbpTenantSwitchLink").click()
            time.sleep(3)
            bodyClassCheck = driver.find_element(
                By.CSS_SELECTOR, "body").get_attribute("class")
            # print(bodyClassCheck)
            driver.find_element(By.CSS_SELECTOR,"button.btn-close").click()
            time.sleep(3)
            bodyClass = driver.find_element(
                By.CSS_SELECTOR, "body").get_attribute("class")
            time.sleep(3)
            print(f"點開租戶視窗的class:{bodyClassCheck},關閉租戶視窗的class:{bodyClass}")
            # print(bodyClass)
        except NoSuchElementException:
            driver.close()
            pytest.fail("找不到元素")
        driver.close()
        assert bodyClass != bodyClassCheck, "關閉租戶視窗正常"

    def testCase4(self):
        """租戶欄位是否能輸入文字"""
        pass

    def testCase5(self):
        """未輸入租戶的情形"""
        load_dotenv()
        driver=browserWebdriver(1)
        url = os.getenv("thirdUrl")
        driver.get(url)
        time.sleep(2)
        driver.find_element(
            By.ID, "LoginInput_UserNameOrEmailAddress"
        ).send_keys(os.getenv("thirdUserName"))
        time.sleep(0.5)
        driver.find_element(By.ID, "LoginInput_Password").send_keys(
            os.getenv("thirdPassWord")
        )
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(2)
        warning = driver.find_element(By.CLASS_NAME, "show").text
        # print(warning)
        hope = driver.find_element(By.CLASS_NAME, "show").text
        print(f"未輸入租戶時登入會出現'{warning}'")
        driver.close()
        assert warning == hope, "未輸入租戶"
    
    # @pytest.mark.loginS
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
        driver.find_element(By.ID, "Input_Name").send_keys(os.getenv("thirdGroup"))
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(1)
        driver.find_element(
            By.ID, "LoginInput_UserNameOrEmailAddress"
        ).send_keys(os.getenv("thirdUserName"))
        driver.find_element(By.ID, "LoginInput_Password").send_keys(
            os.getenv("thirdPassWord")
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
        assert elementText == hope, "登錄不正常"
    # def testCase2(self):
    #     """租戶功能測試"""

    # def testCase3(self):
    #     """登錄不成功的情形，未填帳號"""
    #     self.driver.find_element(By.ID, "AbpTenantSwitchLink").click()
    #     time.sleep(0.5)
    #     self.driver.find_element(By.ID, "Input_Name").send_keys("fae")
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


# if __name__ == "__main__":
#     go = TestThird()
#     go.testCase1()
