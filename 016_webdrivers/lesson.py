from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://www.github.com')

# time.sleep(15)

# driver.close()
# driver.quit()

# print(driver.title)

# email = driver.find_element(By.ID)  # если ипортирована By библиотека
email = driver.find_element('id', 'user_email')
# if email.is_enabled():
# if email.is_displayed():
# if email.is_selected():
email.send_keys('helewlo@example.com')
email.send_keys(Keys.ENTER)

def wait_till_clickable(driver, selector_type, selector_value, time):
    try:
        element = WebDriverWait(driver, time).until(
            EC.element_to_be_clickable((selector_type, selector_value))
        )
    except:
        print('ERROR')
        return None
    else:
        return element

cont = wait_till_clickable(driver, By.XPATH, '//*[@id="email-container"]/div[2]/button', 15)
if cont:
    cont.click()


time.sleep(5)
# print(email)



