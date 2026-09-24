
# Importing webdriver from selenium
from selenium import webdriver
# Importing time, helps to slow down every steps 
import time 
# Importing for finding web elements inside the website
from selenium.webdriver.common.by import By

# Storing webdriver inside a variable and using to opean any browser 
driver = webdriver.Chrome()
time.sleep(2)   # pauses the program for a specified number of seconds.
driver.maximize_window()   # Maximizing the browser
url = "https://www.saucedemo.com/"  # Storing URL into a variable
driver.get(url)     # Using the URL inside the browser
time.sleep(2)

# Locators -- important 
# Among all the selenium locators we can use any
username = driver.find_element (By.ID, "user-name")
password = driver.find_element (By.ID, "password")
login_button = driver.find_element (By.ID, "login-button")

# After locating finally we give Actions to each feild  

username.send_keys("standard_user")
time.sleep(2)
password.send_keys("secret_sauce")
time.sleep(2)
login_button.click()

time.sleep(5)
driver.quit()



# /html/body/div/div/div[2]/div[1]/div/div/form/input    #Absolute XPATH

# //*[@id="login-button"]  # Relative XPATH
