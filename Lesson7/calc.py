from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:

    def __init__(self, driver):
        self.drv = driver
        self.drv.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self.drv.implicitly_wait(4)
        self.drv.maximize_window()

    def make_delay(self, delay):
        self.delay = delay
        self.drv.find_element(By.CSS_SELECTOR, '#delay').clear()
        self.drv.find_element(By.CSS_SELECTOR, '#delay').send_keys(self.delay)

    def click_7(self):
        self.drv.find_elements(By.CSS_SELECTOR, 'span.btn-outline-primary')[0].click()

    def click_plus(self):
        self.drv.find_elements(By.CSS_SELECTOR, 'span.btn-outline-success')[0].click()

    def click_8(self):
        self.drv.find_elements(By.CSS_SELECTOR, 'span.btn-outline-primary')[1].click()

    def click_equally(self):
        self.drv.find_element(By.CSS_SELECTOR, 'span.btn-outline-warning').click()

    def delay_check(self):
        return WebDriverWait(self.drv, self.delay + 1, 0.2).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15')
            )

    def print_result(self):
        print(f"Задержка {self.delay} сек работает, результат: "
              f"{self.drv.find_element(By.CSS_SELECTOR, 'div.screen').text}")