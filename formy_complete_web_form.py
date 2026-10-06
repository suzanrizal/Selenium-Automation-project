from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import Select  # For dropdown

driver = webdriver.Chrome()    # Open chrome browser
driver.maximize_window()        # Maximize window
url = "https://formy-project.herokuapp.com/form"   # Stored url in a vasriable
driver.get(url)    # Getting the Url

wait = WebDriverWait(driver,10)       # For explicit wait

first_name = wait.until(
    EC.element_to_be_clickable((By.ID, "first-name"))
) 
first_name.send_keys("Sujan")
# assert first_name.get_attribute("value") == "Sujan" , "First name not entered correctly"
time.sleep(1)

last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Rijal")
# assert last_name.get_attribute("value") == "Rijal", "Last name is not entered correctly"
time.sleep(1)

job_title = driver.find_element(By.ID, "job-title")
job_title.send_keys("Quality Assurance Engineer")
# assert job_title.get_attribute("value") == "Quality Assurance Engineer", "Job title is incorrect"
time.sleep(1)


highest_education = driver.find_element(By.ID, "radio-button-1")
highest_education.click()
# assert highest_education.is_selected(), "Education was not selected"
time.sleep(1)

driver.execute_script("window.scrollBy(0,500);")       # Mouse scroolm action

sex_checkbox = driver.find_element(By.ID, "checkbox-1")
sex_checkbox.click()
# assert sex.is_selected(), "Sex was not selected"
time.sleep(1)

experience_dropdown = driver.find_element(By.ID, "select-menu")
select = Select(experience_dropdown)          # Dropdown 
select.select_by_value("1")
time.sleep(2)

date = driver.find_element(By.ID, "datepicker")
date.send_keys("10/4/2026")                 # Date format
time.sleep(2)

submit_button = driver.find_element(By.XPATH, "//a[@role='button']")
submit_button.click()
assert "thanks" in driver.current_url, "form submition failed"
print("Form submitted sucessfully")
time.sleep(2)

driver.quit()

