import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_location = 'chromedriver.exe'

driver = webdriver.Chrome(driver_location)

driver.get('https://particle-clicker.web.cern.ch/')

click_object = driver.find_element_by_id('detector-events')

actions = ActionChains(driver)
actions.click(click_object)

count = 0
for i in range(50):
    actions.perform()
    count += 1
    print(count)
