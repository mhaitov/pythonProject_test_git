from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_location = 'chromedriver.exe'

driver = webdriver.Chrome(driver_location)

driver.get('https://www.github.com')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/main/div/div[1]/div[1]/div[1]/div/div/div[1]/h1'))
    )
    print(element.text)
except:
    driver.quit()
