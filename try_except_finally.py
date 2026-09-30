from selenium import webdriver
# import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome() 
driver.maximize_window()   
url = "https://www.saucedemo.com/"  
driver.get(url)

wait = WebDriverWait(driver, 10)

username = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
username.send_keys("standard_user")

password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
password.send_keys("secret_sauce")

try:
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

except:
    print("Login button not found")

# script validation

# if driver.current_url == "https://www.saucedemo.com/inventory.html":
#     print("login sucessful")
# else:
#     print("login failed")

# Other method of script validation

# if "inverntory" in driver.current_url:
#     print("Login sucessful")
# else:
#     print("Login failed")

# Standard method for assertion

assert "inventory" in driver.current_url, "login unsucessful"


driver.close()
driver.quit()