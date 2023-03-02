from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
url = 'https://www.youtube.com/@visitestoniaofficial/videos'

driver.get(url)
accept = driver.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span')
accept.click()

videos = driver.find_elements('class name', 'style-scope ytd-rich-grid-row')

vid_list = []
for vid in videos:
    title = vid.find_elements('xpath', './/*[@id="video-title"]').text
    link = vid.find_elements('tag name', 'a').get_attribute('href')
