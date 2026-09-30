from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
url = "https://sagar-test-qa.vercel.app/"
driver.get(url)

# Explicit wait mechanism
wait = WebDriverWait(driver,10)
# time.sleep(2)

username = wait.until(EC.element_to_be_clickable((By.ID, "username")))
username.send_keys("Sujanrijal")
# time.sleep(2)

password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
password.send_keys("Password@123")
# time.sleep(2)

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']")))
login_button.click()
time.sleep(1)

alert = driver.switch_to.alert

alert.accept()
time.sleep(2)


driver.close()





