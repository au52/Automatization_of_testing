import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_filling import FormFilling
from calc import Calculator
from internet_store import InternetStore

# Задание 1. Автотест на заполнение формы
# --------------------------------------------------------------------------

@pytest.mark.parametrize('selector, value', [('first-name', 'Иван'),
                                               ('last-name', 'Петров'),
                                               ('address', 'Ленина, 55-3'),
                                               ('e-mail', 'test@skypro.com'),
                                               ('phone', '+7985899998787'),
                                               ('city', 'Москва'),
                                               ('country', 'Россия'),
                                               ('job-position', 'QA'),
                                               ('company', 'SkyPro')])

def test_green_fild_color(selector, value):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    form = FormFilling(driver)
    form.send_data(selector, value)
    form.submit_data()
    cell_color = form.get_cell_color(selector)
    driver.quit()
    assert cell_color == form.green

@pytest.mark.parametrize('selector, value', [('zip-code', '')])
def test_red_fild_color(selector, value):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    form = FormFilling(driver)
    form.send_data(selector, value)
    form.submit_data()
    cell_color = form.get_cell_color(selector)
    driver.quit()
    assert cell_color == form.red
# --------------------------------------------------------------------------

# Задание 2. Автотест на калькулятор
# --------------------------------------------------------------------------

def test_calc_delay():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calc = Calculator(driver)
    calc.make_delay(45)
    calc.click_7()
    calc.click_plus()
    calc.click_8()
    calc.click_equally()
    delay_status = calc.delay_check()
    calc.print_result()
    driver.quit()
    assert delay_status == True
# --------------------------------------------------------------------------

# Задание 3. Автотест на интернет-магазин
# --------------------------------------------------------------------------

def test_total_cost():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    store = InternetStore(driver)
    store.customer_auth()
    store.add_to_cart_1()
    store.add_to_cart_2()
    store.add_to_cart_3()
    store.go_to_cart()
    store.checkout_click()
    store.customer_first_name_send('Иван')
    store.customer_last_name_send('Петров')
    store.custoner_zip_code_send('123456')
    store.continue_click()
    total_cost = store.get_total_cost()
    driver.quit()
    assert total_cost == '$58.29'
# --------------------------------------------------------------------------
