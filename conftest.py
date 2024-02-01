import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function", autouse=True)
def driver():
    options = Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://vuetifyjs.com/en/")
    sleep(2)
    print("开始测试")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/en/getting-started"
                                                                          "/installation/']"))).click()
    driver.find_element(By.XPATH, "//div[@id='v-list-group--id-Components']").click()
    yield driver
    print("结束测试")
    driver.quit()
