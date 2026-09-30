from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
url = "https://sagar-test-qa.vercel.app/"
driver.get(url)
time.sleep(2)

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")

username.send_keys("Sujanrijal")
time.sleep(2)
password.send_keys("Password@123")
time.sleep(2)
login_button.click()
time.sleep(2)

alert = driver.switch_to.alert


driver.close()





