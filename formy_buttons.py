from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://formy-project.herokuapp.com/buttons"
driver.get(url)

wait = WebDriverWait(driver, 10)   #Explicit wait mechanism

# Click on the primary button
primary_button = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Primary']"))
)
primary_button.click()
assert primary_button.is_displayed(), "Primary button is not displayed"
print("Primary button clicked and verified")

# Click on the success button
success_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Success']"))
)
success_button.click()
assert success_button.is_displayed(), "Success button is not clickable"
print("Success button clicked and verified")

# Click on the info button
info_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Info']"))
)
info_button.click()
assert info_button.is_displayed(), "Info button is not displayed"
print("Info button clicked and verified")

#Click on the link button
link = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Link']"))
)
link.click()
assert link.is_displayed(), "Link button is not displayed"
print("Link button clicked and verified")

#Click on the dropdown button
dropdown = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='btnGroupDrop1']"))
)
dropdown.click()
assert dropdown.is_displayed(), "Dropdown button is not displayed"
print("Dropdown button clicked and verified")


# dropdown_1 = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Dropdown link 1']"))
# )
# assert dropdown_1.is_displayed(), "Dropdown link 1 is not displayed"
# dropdown_1.click()
# time.sleep(2)

# dropdown = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//button[@id='btnGroupDrop1']"))
# )
# dropdown.click()
# time.sleep(2)

# dropdown_2 = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Dropdown link 2']"))
# )
# assert dropdown_2.is_displayed(), "Dropdown link 2 is not displayed"
# dropdown_2.click()


driver.close()
driver.quit()


