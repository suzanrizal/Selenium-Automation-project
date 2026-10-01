from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://formy-project.herokuapp.com/"
driver.get(url)

wait = WebDriverWait(driver, 10)   # Use explicit wait mechanism in the real world scenario

auto_complete = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Autocomplete']")
    )
)
auto_complete.click()
time.sleep(2)    # Using time.sleep() for practicing purpose 

address = driver.find_element(By.ID, "autocomplete")       # We can you explicit wait mechanism here as well but we are using time.sleep() for practicing purpose 
address.send_keys("Kathmandu")
time.sleep(2)

street_address = driver.find_element(By.ID, "street_number")
street_address.send_keys("Kalanki")
time.sleep(2)

street_address2 = driver.find_element(By.ID, "route")
street_address2.send_keys("Kalanki")
time.sleep(2)

city = driver.find_element(By.ID, "locality")
city.send_keys("Gantabya tole")
time.sleep(2)

state = driver.find_element(By.ID, "administrative_area_level_1")
state.send_keys("Bagmati")
time.sleep(2)

zip_code = driver.find_element(By.ID, "postal_code")
zip_code.send_keys("44600")
time.sleep(2)

country = driver.find_element(By.ID, "country")
country.send_keys("Nepal")  
time.sleep(2)   

assert address.get_attribute("value") == "kathmandu, Nepal", "Address is not correct"
assert street_address.is_displayed(), "Street address is not displayed"

driver.close()
driver.quit()

                            
                    