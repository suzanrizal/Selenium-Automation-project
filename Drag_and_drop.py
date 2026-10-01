from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains   # Mouse cations


driver = webdriver.Chrome()
driver.maximize_window()

url = "https://formy-project.herokuapp.com/dragdrop"
driver.get(url)
time.sleep(2)

# We need 
# Source locator 
# Destination locator

actions = ActionChains(driver)

source = driver.find_element(By.XPATH, "//*[@id='image']/img")
destination = driver.find_element(By.XPATH, "//*[@id='box']")

actions.drag_and_drop(source, destination).perform()
time.sleep(2)


driver.close()
driver.quit()

