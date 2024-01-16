import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function", autouse=True)
def driver():
    options = Options()
    options.add_argument("--headless, --start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(1)
    driver.get("https://iviewui.com")
    sleep(0.5)
    print("开始测试")
    driver.find_element(By.XPATH, "//a[@href='/view-ui-plus/']").click()
    # driver.find_element(By.XPATH, "//span[@class='i-layout-header-trigger']").click()
    driver.find_element(By.XPATH, "//span[@class='i-layout-menu-side-title' and contains(., '组件')]").click()
    driver.find_element(By.XPATH,
                        "//span[@class='i-layout-menu-side-title-text' and contains(., '表单')]").click()
    yield driver
    print("结束测试")
    driver.quit()
