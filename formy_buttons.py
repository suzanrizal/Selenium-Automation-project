from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://formy-project.herokuapp.com/buttons"
driver.get(url)

wait = WebDriverWait(driver, 10)

primary_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Primary']"))
)
primary_button.click()


success_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Success']"))
)
success_button.click()

info_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Info']"))
)
info_button.click()

link = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Link']"))
)
link.click()

dropdown = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='btnGroupDrop1']"))
)
dropdown.click()
time.sleep(2)

dropdown_1 = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Dropdown link 1']"))
)
assert dropdown_1.is_displayed(), "Dropdown link 1 is not displayed"
dropdown_1.click()
time.sleep(2)

dropdown = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='btnGroupDrop1']"))
)
dropdown.click()
time.sleep(2)

dropdown_2 = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Dropdown link 2']"))
)
assert dropdown_2.is_displayed(), "Dropdown link 2 is not displayed"
dropdown_2.click()


driver.close()


