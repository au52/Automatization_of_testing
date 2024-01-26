from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://the-internet.herokuapp.com/login')
sleep(2)
driver.find_element(By.NAME, 'username').send_keys('tomsmith')
sleep(2)
driver.find_element(By.NAME, 'password').send_keys('SuperSecretPassword!')
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'button.radius').click()
sleep(2)
driver.quit()