import allure
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestIview:
    @pytest.fixture(scope="function", autouse=True)
    def driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://vuetifyjs.com/en/")
        sleep(2)
        print("开始测试")
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/en/getting-started"
                                                                                   "/installation/']"))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='v-list-group--id-Components' "
                                                  "and contains(., 'Components')]"))).click()
        yield self.driver
        print("结束测试")
        self.driver.quit()

    @allure.feature("Goto_radio_page")
    def test_goto_radio_page(self, driver):
        with allure.step("goto radio page"):
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='v-list-item-title' and contains(.,'Radio "
                                                          "button')]"))).click()

        with allure.step("assert radio page loading"):
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(.,'Radio "
                                                                                      "buttons')]")))
            driver.save_screenshot("./result/radioPage.png")
            allure.attach.file("./result/radioPage.png", attachment_type=allure.attachment_type.PNG)

    @allure.feature("Click_OptionC_radio")
    def test_click_windows_radio(self, driver):
        with allure.step("goto radio page"):
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='v-list-item-title' and contains(.,'Radio "
                                                          "button')]"))).click()

        with allure.step("selecting windows radio"):
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//label[@class='v-label v-label--clickable' and contains("
                                                          "., 'Radio Three')]"))).click()
            sleep(1)
            driver.save_screenshot("./result/windowsRadio.png")
            allure.attach.file("./result/windowsRadio.png", attachment_type=allure.attachment_type.PNG)


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test01.py', '--alluredir=./result/1'])
