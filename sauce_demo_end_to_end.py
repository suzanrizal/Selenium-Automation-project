from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import Select  # For dropdown

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.saucedemo.com/"
driver.get(url)
wait = WebDriverWait(driver,10)

username = wait.until(
    EC.element_to_be_clickable((By.ID, "user-name"))
)
username.send_keys("standard_user")
time.sleep(1)

password = wait.until(
    EC.element_to_be_clickable((By.ID, "password"))
)
password.send_keys("secret_sauce")
time.sleep(1)

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(1)
assert "inventory" in driver.current_url, "Login Failed"

dropdown_option = driver.find_element(By.XPATH, "//select[@aria-label='Sort products']")
select = Select(dropdown_option)
select.select_by_value("hilo")
time.sleep(1)

product1_add = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
product1_add.click()
time.sleep(1)
product2_add = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
product2_add.click()
time.sleep(1)

driver.execute_script("window.scrollBy(0,500);")
time.sleep(1)
product3_add = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
product3_add.click()
time.sleep(1)

driver.execute_script("window.scrollTo(0,0);")
time.sleep(1)

cart_button = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
cart_button.click()
time.sleep(1)
assert "cart" in driver.current_url, "Proceed to cart page failed"

driver.execute_script("window.scrollBy(0,500);")
time.sleep(1)

checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()
time.sleep(1)
assert "checkout" in driver.current_url, "Checkout process failed"

first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("sujan")
time.sleep(1)
last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Rijal")
time.sleep(1)
postal_code = driver.find_element(By.ID, "postal-code")
postal_code.send_keys("44600")
time.sleep(1)

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()
time.sleep(1)

driver.execute_script("window.scrollBy(0,500);")
time.sleep(1)

finish_button = driver.find_element(By.ID, "finish")
finish_button.click()
time.sleep(1)
assert "complete" in driver.current_url, "Checkout Failed"

reciept_download = driver.find_element(By.ID, "generate-pdf-order")
reciept_download.click()
time.sleep(2)

driver.quit()