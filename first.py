
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# Initilize driver
driver=webdriver.Edge()
#delay execution time
# time.sleep(2)
driver.maximize_window()
time.sleep(2)
url = "https://www.saucedemo.com/"

driver.get("url")
time.sleep(2)

# Locators by id

# username=driver.find_element(By.ID, "user-name")
# password=driver.find_element(By.ID, "password")
# login_button=driver.find_element(By.ID, "login-button")

# Locators by Xpath 

username=driver.find_element(By.XPATH, "//*[@id='user-name']")
password=driver.find_element(By.XPATH, "//*[@id='password']")
login_button=driver.find_element(By.XPATH, "//*[@id='login-button']")


# Actions
username.send_keys("standard_user")
time.sleep(2)
password.send_keys("secret_sauce")
time.sleep(2)
if login_button.is_enabled:
    print("Login button enabled")
else:
    print("Not enabled")
login_button.click()
time.sleep(2)

#Print title and current url
print(driver.title)
#print current url
print("The current URL is: ", driver.current_url)

#Close just the window 
driver.close()
#Quit entire webdriver 
driver.quit()

