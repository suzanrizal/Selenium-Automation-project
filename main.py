from selenium import webdriver
import time 
from selenium.webdriver.common.by import By

driver = "webdriver"
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
url = "https://www.saucedemo.com/"
driver.get(url)
time.sleep(2)

#Locators
username = driver.find_element (By.ID, "user-name")
password = driver.find_element (By.ID, "password")
login_button = driver.find_element (By.ID, "login-button")

#Actions

username.send_keys("standard_user")
time.sleep(2)
password.send_keys("secret_sauce")
time.sleep(2)
login_button.click()

time.sleep(5)
driver.quit()



# /html/body/div/div/div[2]/div[1]/div/div/form/input    #Absolute XPATH

# //*[@id="login-button"]  # Relative XPATH
