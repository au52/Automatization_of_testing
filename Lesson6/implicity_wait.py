from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://uitestingplayground.com/ajax')
# Добавляем неявное ожидание, без которого выполнение кода падает в ошибку
# В течении 20 сек драйвер будет пытаться найти элементы, чьи селекторы есть в коде
driver.implicitly_wait(20)
# Даже если элемент найден, ожидание по-прежнему будет 20 сек, раньше не завершится.
# Т.е. неявное ожидание не содержит условия
driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

content = driver.find_element(By.CSS_SELECTOR, '#content')
txt = content.find_element((By.CSS_SELECTOR), 'p.bg-success').text
print(txt)

sleep(5)

