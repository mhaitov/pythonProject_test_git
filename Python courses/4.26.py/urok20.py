from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_location = 'chromedriver.exe'

driver = webdriver.Chrome(driver_location)

driver.get('https://www.github.com')

# driver.close() # zakryvaet vkladku
# driver.quit() # zakrqvaet brauzer

# print(driver.title)  # Poluchaem zaagolovok

search = driver.find_element_by_name('user_email')
if search.is_enabled() == True:
    search.send_keys('python@example.com')
    search.send_keys(Keys.ENTER)

else:
    print('ERROR')

time.sleep(4)
search.clear()
search.send_keys('javascript@example.com')

# search.send_keys('python@example.com')
# search.send_keys(Keys.ENTER)  # SAME LIKE (search.send_keys(Keys.RETURN))
# #
# search = driver.find_element_by_id('user_login')
# search.send_keys('Marian')





# Check
# print(search.is_selected())
# print(search.is_enabled())
# print(search.is_displayed())


print(driver.page_source)
