from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window
time.sleep(2)

url = "https://sagar-test-qa.vercel.app/contact.html"
driver.get(url)
time.sleep(2)

test = driver.find_element(By.XPATH, "/html/body/div/article/ul/li[3]/a")
test.click()
time.sleep(2)


