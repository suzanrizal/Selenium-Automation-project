from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://formy-project.herokuapp.com/checkbox"
driver.get(url)

wait = WebDriverWait(driver, 10)

checkbox_1 = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='checkbox-1']"))
)
checkbox_1.click()
time.sleep(1)

checkbox_2 = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='checkbox-2']"))
)
checkbox_2.click()
time.sleep(1)

checkbox_3 = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='checkbox-3']"))
)
checkbox_3.click()
time.sleep(1)
driver.close()
driver.quit()
