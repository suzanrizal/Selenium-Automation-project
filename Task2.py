from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://sagar-test-qa.vercel.app/about.html"
driver.get(url)
time.sleep(2)

full_name = driver.find_element(By.XPATH, "//input[@id='fullname']")
phone = driver.find_element(By.XPATH, "//input[@id='phone']")
email = driver.find_element(By.XPATH, "//input[@id='email']")
hobby = driver.find_element(By.XPATH, "//input[@id='hobby']")
submit = driver.find_element(By.XPATH, "//button[@type='submit']")

full_name.send_keys("Sujan rijal")
time.sleep(2)
phone.send_keys(9840308352)
time.sleep(2)
email.send_keys("rizalsuzan2@gmail.com")
time.sleep(2)
hobby.send_keys("My hobbies include listening to music, watching movies, and exploring new places. I also enjoy learning new things and spending time with my friends and family.")
time.sleep(2)
submit.click()
time.sleep(2)


driver.quit()



