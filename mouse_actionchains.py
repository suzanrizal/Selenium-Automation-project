from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains  # For mouse actions we import actionchains

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.saucedemo.com/"
driver.get(url)


username = driver.find_element (By.ID, "user-name")
username.send_keys("standard_user")
time.sleep(2)
password = driver.find_element (By.ID, "password")
password.send_keys("secret_sauce")
time.sleep(2)
login_button = driver.find_element (By.ID, "login-button")
# login_button.click()
time.sleep(2)

# Action chain 

actions = ActionChains(driver)
actions.move_to_element(login_button).perform()
time.sleep(1)      # Hover to element and click - Multiple actions with action chains
actions.click_and_hold(login_button).perform()
time.sleep(5)
actions.release(login_button).perform()   # Click and hold the element
time.sleep(2)


driver.close()
driver.quit()
