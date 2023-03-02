from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get('https://gammatest.net/')

# link = driver.find_element('link text', 'Rohkem infot')
link = driver.find_element('partial link text', 'Rohkem')
# link = driver.find_element('tag name', 'a')
# link = driver.find_element('css selector', '.main .container')
# print(link.text)
link.click()
#
# driver.back()
# driver.forward()
# driver.refresh()

link = driver.find_elements('tag name', 'a')
for l in link:
    print(l.get_attribute('href'))
time.sleep(5)