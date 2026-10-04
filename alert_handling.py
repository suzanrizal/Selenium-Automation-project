from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.maximize_window()

url = "https://sagar-test-qa.vercel.app/"
driver.get(url)

username = driver.find_element(By.ID, "username")
username.send_keys("Sujan rijal")
time.sleep(2)
password = driver.find_element(By.ID, "password")
password.send_keys("Password@123")
time.sleep(2)
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(2)

# Handling alert 

alert = driver.switch_to.alert
alert.accept()
time.sleep(2)

driver.close()
driver.quit()
