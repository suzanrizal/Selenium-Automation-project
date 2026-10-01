# Curious

from selenium import webdriver
import time 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.facebook.com/"
driver.get(url)
time.sleep(2)

email_or_phone_number = driver.find_element(By.NAME, "email")
email_or_phone_number.send_keys("9840308352")
time.sleep(2)

password = driver.find_element(By.NAME, "pass")
password.send_keys("FakePassword@123")
time.sleep(2)

login_button = driver.find_element(By.XPATH, "//span[@class='x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft'][normalize-space()='Log in']")
login_button.click()
time.sleep(10)

driver.close()
driver.quit()



