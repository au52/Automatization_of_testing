from selenium.webdriver.common.by import By

class FormFilling:

    def __init__(self, driver):
        self.drv = driver
        self.drv.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self.drv.implicitly_wait(4)
        self.drv.maximize_window()
        self.green = 'rgba(209, 231, 221, 1)'
        self.red = 'rgba(248, 215, 218, 1)'

    def send_data(self, selector, value):
        self.drv.find_element(By.NAME, selector).clear()
        self.drv.find_element(By.NAME, selector).send_keys(value)

    def submit_data(self):
        self.drv.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def get_cell_color(self, selector):
        return self.drv.find_element(By.CSS_SELECTOR, '#'+selector).\
               value_of_css_property('background-color')







