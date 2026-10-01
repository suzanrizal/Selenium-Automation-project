from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://formy-project.herokuapp.com/checkbox"
driver.get(url)

wait = WebDriverWait(driver, 5)
try:
    print("starting checkbox 1")
    checkbox_1 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='checkbox-1']"))
    )
    checkbox_1.click()
    assert checkbox_1.is_selected(), "Checkbox 1 is not selected"
    print("checkbox 1 clicked and verified")

except Exception as e:
    print("Checkbox is not displayed", e)

try:
    print("starting checkbox 2")
    checkbox_2 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='checkbox-2']"))
    )
    checkbox_2.click()
    assert checkbox_2.is_selected(), "Checkbox 2 is not selected"
    print("checkbox 2 clicked and verified")

except Exception as e:
    print("Checkbox is not displayed", e)

try:
    print("starting checkbox 3")
    checkbox_3 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='checkbox-3']"))
    )
    checkbox_3.click()
    assert checkbox_3.is_selected(), "Checkbox 3 is not selected"
    print("checkbox 3 clicked and verified")

except Exception as e:
    print("Checkbox is not displayed", e)



driver.close()
driver.quit()
