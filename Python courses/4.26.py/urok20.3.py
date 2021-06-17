import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_location = 'chromedriver.exe'

driver = webdriver.Chrome(driver_location)

driver.get('https://gammatest.net/')

link = driver.find_element_by_link_text('Rohkem infot')
# # link = driver.find_element_by_partial_link_text('Rohkem i')   # polovina teksta
# # print(link.text)
# link = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/p[2]/a')
link.click()

element = driver.find_elements_by_tag_name('td')
for cell in element:
    print(cell.text)
#
# time.sleep(5)
# driver.back()
#
# time.sleep(5)
# driver.forward()

link = driver.find_element_by_link_text('На русском')
link.click()


element = driver.find_elements_by_tag_name('td')
for cell in element:
    print(cell.text)