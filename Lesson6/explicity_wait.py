from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://uitestingplayground.com/progressbar')

driver.find_element(By.CSS_SELECTOR, '#startButton').click()
# Устанавливаем макс время ожидания 40 сек
# По умолчанию третий аргумент WebDriverWait частота проверки условия
# равен 0.5 сек, изменим на 0.1
waiter = WebDriverWait(driver, 40, 0.1)
# waiter может ждать пока какое-либо событие произойдёт,
# либо не произойдёт. Формат написания имеет значение,
# если waiter.until расположить в одну строку - не работает!
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#progressBar'), '75%')
)

driver.find_element(By.CSS_SELECTOR, '#stopButton').click()

sleep(3)