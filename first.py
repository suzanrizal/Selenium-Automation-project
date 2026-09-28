# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By

from selenium import webdriver
import time
# Initilize driver
driver=webdriver.Edge()
#delay execution time
time.sleep(2)
driver.maximize_window()
time.sleep(2)
url = "https://www.mindrisers.com.np/"

driver.get(url)
time.sleep(2)
#Refresh
driver.refresh()
driver.back()
time.sleep(2)

driver.get("https://www.saucedemo.com/")
time.sleep(2)

#Print title and current url
print(driver.title)
#print current url
print("The current URL is: ", driver.current_url)

#Quit driver and browser
driver.quit()

