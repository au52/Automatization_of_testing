import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

first_name = driver.find_element(By.NAME, 'first-name')
last_name = driver.find_element(By.NAME, 'last-name')
address = driver.find_element(By.NAME, 'address')
email = driver.find_element(By.NAME, 'e-mail')
phone = driver.find_element(By.NAME, 'phone')
city = driver.find_element(By.NAME, 'city')
country = driver.find_element(By.NAME, 'country')
job = driver.find_element(By.NAME, 'job-position')
company = driver.find_element(By.NAME, 'company')

first_name.send_keys('Иван')
last_name.send_keys('Петров')
address.send_keys('Ленина, 55-3')
email.send_keys('test@skypro.com')
phone.send_keys('+7985899998787')
city.send_keys('Москва')
country.send_keys('Россия')
job.send_keys('QA')
company.send_keys('SkyPro')

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


sleep(15)
driver.quit()