import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

green = 'rgba(209, 231, 221, 1)'
red = 'rgba(248, 215, 218, 1)'

@pytest.mark.parametrize('sel, value, res', [('first-name', 'Иван', green),
                                               ('last-name', 'Петров', green),
                                               ('address', 'Ленина, 55-3', green),
                                               ('e-mail', 'test@skypro.com', green),
                                               ('phone', '+7985899998787', green),
                                               ('city', 'Москва', green),
                                               ('country', 'Россия', green),
                                               ('job-position', 'QA', green),
                                               ('company', 'SkyPro', green),
                                               ('zip-code', '', red)])

def test_fild_color(sel, value, res):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    driver.find_element(By.NAME, sel).clear()
    driver.find_element(By.NAME, sel).send_keys(value)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert driver.find_element(By.CSS_SELECTOR, '#'+sel).\
               value_of_css_property('background-color') == res
    driver.quit()

