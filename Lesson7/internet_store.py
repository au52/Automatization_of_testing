from selenium.webdriver.common.by import By

class InternetStore:

    def __init__(self, driver):
        self.drv = driver
        self.drv.get('https://www.saucedemo.com/')
        self.drv.implicitly_wait(4)
        self.drv.maximize_window()
        self.username = 'standard_user'
        self.password = 'secret_sauce'

    def customer_auth(self):
        self.drv.find_element(By.CSS_SELECTOR, '#user-name').send_keys(self.username)
        self.drv.find_element(By.CSS_SELECTOR, '#password').send_keys(self.password)
        self.drv.find_element(By.CSS_SELECTOR, '#login-button').click()

    def add_to_cart_1(self):
        self.drv.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()

    def add_to_cart_2(self):
        self.drv.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()

    def add_to_cart_3(self):
        self.drv.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def go_to_cart(self):
        self.drv.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    def checkout_click(self):
        self.drv.find_element(By.CSS_SELECTOR, '#checkout').click()

    def customer_first_name_send(self, first_name):
        self.drv.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)

    def customer_last_name_send(self, last_name):
        self.drv.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)

    def custoner_zip_code_send(self, zip_code):
        self.drv.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(zip_code)

    def continue_click(self):
        self.drv.find_element(By.CSS_SELECTOR, '#continue').click()

    def get_total_cost(self):
        return self.drv.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text[7:]







