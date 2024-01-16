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
            driver.find_element(By.XPATH, "//span[@class='i-layout-menu-side-title' and contains(., 'Radio')]").click()

        with allure.step("assert radio page loading"):
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Radio')]")))
            driver.save_screenshot("./result/radioPage.png")
            allure.attach.file("./result/radioPage.png", attachment_type=allure.attachment_type.PNG)

    @allure.feature("Click_windows_radio")
    def test_click_windows_radio(self, driver):
        with allure.step("goto radio page"):
            driver.find_element(By.XPATH, "//span[@class='i-layout-menu-side-title' and contains(., 'Radio')]").click()

        with allure.step("selecting windows radio"):
            driver.find_element(By.XPATH, "//i[contains(@class, 'ivu-icon-logo-windows')]").click()
            sleep(1)
            driver.save_screenshot("./result/windowsRadio.png")
            allure.attach.file("./result/windowsRadio.png", attachment_type=allure.attachment_type.PNG)


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test01.py', '--alluredir=./result/1'])
