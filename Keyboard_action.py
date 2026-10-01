from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.keys import Keys    # For keyboard action we import keys 


driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.saucedemo.com/"
driver.get(url)
time.sleep(2)

actions = ActionChains(driver)

username =driver.find_element(By.XPATH, "//*[@id='user-name']")
username.send_keys("standard_user")
time.sleep(1)
username.send_keys(Keys.TAB)
time.sleep(4)
password= driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("secret_sauce")
login_button= driver.find_element(By.XPATH, "//*[@id='login-button']")
password.send_keys(Keys.TAB)
time.sleep(1)

    # Actions
login_button.send_keys(Keys.ENTER)
time.sleep(3)

driver.close()
driver.quit()

# password.send_keys(Keys.TAB)



