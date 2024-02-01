import allure
import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestIview:

    @allure.feature("Goto_radio_page")
    def test_goto_radio_page(self, driver):
        with allure.step("goto radio page"):
            WebDriverWait(driver, 3000).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='v-list-item-title' and contains(.,'Radio button')]"))).click()

        with allure.step("assert radio page loading"):
            WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(.,'Radio buttons')]")))
            driver.save_screenshot("./result/radioPage.png")
            allure.attach.file("./result/radioPage.png", attachment_type=allure.attachment_type.PNG)

    @allure.feature("Click_OptionC_radio")
    def test_click_windows_radio(self, driver):
        with allure.step("goto radio page"):
            WebDriverWait(driver, 3000).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='v-list-item-title' and contains(.,'Radio button')]"))).click()

        with allure.step("selecting windows radio"):
            WebDriverWait(driver, 3000).until(
                EC.presence_of_element_located((By.XPATH, "//label[@class='v-label v-label--clickable' and contains(., 'Radio Three')]"))).click()
            sleep(1)
            driver.save_screenshot("./result/windowsRadio.png")
            allure.attach.file("./result/windowsRadio.png", attachment_type=allure.attachment_type.PNG)


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test01.py', '--alluredir=./result/1'])
