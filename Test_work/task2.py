from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calc_delay():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    driver.find_element(By.CSS_SELECTOR, '#delay').clear()
    driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')

    numeric_keys = driver.find_elements(By.CSS_SELECTOR, 'span.btn-outline-primary')
    oper_keys = driver.find_elements(By.CSS_SELECTOR, 'span.btn-outline-success')
    numeric_keys[0].click()  # 7
    oper_keys[0].click()  # +
    numeric_keys[1].click()  # 8
    driver.find_element(By.CSS_SELECTOR, 'span.btn-outline-warning').click()  # =

    timer = WebDriverWait(driver, 45.1, 0.1)
    assert timer.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15')
    ) == True

    driver.quit()
