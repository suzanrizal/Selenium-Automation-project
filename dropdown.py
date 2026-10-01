from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select   # import select for dropdown handeling 


driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.saucedemo.com/"
driver.get(url)

username = driver.find_element (By.ID, "user-name")
username.send_keys("standard_user")
time.sleep(2)
password = driver.find_element (By.ID, "password")
password.send_keys("secret_sauce")
time.sleep(2)
login_button = driver.find_element (By.ID, "login-button")
login_button.click()
time.sleep(2)

# Drop down 

sort_options1 = driver.find_element(By.XPATH, "//select[@aria-label='Sort products']")
select = Select(sort_options1)
select.select_by_visible_text ("Name (Z to A)")
time.sleep(2)

sort_options2 = driver.find_element(By.XPATH, "//select[@aria-label='Sort products']")
select = Select(sort_options2)
select.select_by_value("hilo")
time.sleep(2)


driver.close()
driver.quit()




