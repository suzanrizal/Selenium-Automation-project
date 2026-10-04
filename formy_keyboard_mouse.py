from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://formy-project.herokuapp.com/keypress"

driver.get(url)
actions = ActionChains(driver)

# With Enter key
# name = driver.find_element(By.ID, "name")
# name.send_keys("Sujan rijal")
# time.sleep(2)
# name.send_keys(Keys.ENTER)
# time.sleep(2)

# # TAB
# name = driver.find_element(By.ID, "name")
# name.send_keys("Sujan rijal")
# time.sleep(2)
# name.send_keys(Keys.TAB)
# time.sleep(2)

# Mouse action
name = driver.find_element(By.ID , "name")
actions.move_to_element(name).perform()
time.sleep(2)
actions.click().perform()
time.sleep(2)
actions.send_keys("Sujan rijal").perform()
time.sleep(2)






