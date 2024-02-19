import allure
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGoogleSearch:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.google.com.hk")
        self.driver.set_page_load_timeout(1800)
        print("开始测试")

    def teardown_method(self):
        self.driver.quit()
        print("结束测试")

    def test_get_user_name(self):
        sleep(60)
        with allure.step("type 谷歌地图"):
            (WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, "//textarea[@aria-label='搜索']"))).send_keys("谷歌地图"))
            sleep(10)
        with allure.step("click enter"):
            (WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Google 搜索']"))).click())
            sleep(10)
        with allure.step("assert Google地圖 display"):
            (WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[text()='Google地圖']"))).is_displayed())
            sleep(10)
        with allure.step("back to home page"):
            self.driver.back()
            sleep(10)
        with allure.step("assert Google logo display"):
            (WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//img[@alt='Google']"))).is_displayed())


if __name__ == '__main__':
    pytest.main(['-vs', 'test03.py', '--alluredir=./result'])
