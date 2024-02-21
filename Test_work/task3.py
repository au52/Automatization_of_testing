from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_total_cost():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://www.saucedemo.com/')

    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Ivan')
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Petrov')
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('123456')

    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    total_cost = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text[7:]
    driver.quit()

    assert total_cost == '$58.29'