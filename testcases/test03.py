import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGoogleSearch:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.google.com.hk")
        print("开始测试")

    def teardown_method(self):
        self.driver.quit()
        print("结束测试")

    def test_get_user_name(self):
        (WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@aria-label='搜索']"))).send_keys("谷歌地图"))
        (WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Google 搜索']"))).click())
        (WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Google地圖']"))).is_displayed())
        self.driver.back()
        (WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='Google']"))).is_displayed())


if __name__ == '__main__':
    pytest.main(['-vs', 'test03.py'])
