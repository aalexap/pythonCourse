from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
url = 'https://www.youtube.com/@visitestoniaofficial/videos'

# width = driver.get_window_size().get('width')
# height = driver.get_window_size().get('height')

# print(width, height)
# print(driver.get_window_size())
# driver.get(url)
# driver.set_window_size(800, 600)
#
# driver.set_window_position(100, 100)
# position = driver.get_window_position()
#

# position = driver.get_window_position()
# print(position)
# driver.set_window_rect(100, 100, 800, 600)
#
# driver.fullscreen_window()
# time.sleep(3)
# driver.minimize_window()
# time.sleep(3)
# driver.maximize_window()
# time.sleep(3)

driver.get(url)
accept = driver.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span')
accept.click()

# driver.save_screenshot('yt.png')

# element = driver.find_element('xpath', '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer[1]/div')
# element.screenshot('element.png')

# print(driver.current_window_handle)
current_window = driver.current_window_handle
driver.switch_to.new_window('tab')  # 'window'
driver.get('https://github.com')
second_window = driver.current_window_handle

driver.switch_to.window(current_window)
time.sleep(4)
driver.switch_to.window(second_window)

for win in driver.window_handles:
    driver.switch_to.window(win)
    driver.save_screenshot(f'{win}.png')
