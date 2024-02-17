from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.refresh()
driver.get('http://uitestingplayground.com/textinput')
driver.find_element(By.CSS_SELECTOR, '#newButtonName').send_keys('SkyPro')
updButton = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
updButton.click()
print(updButton.text)

driver.quit()

