# Handeling diffrent windows or tabs

from selenium import webdriver
import time 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://formy-project.herokuapp.com/switch-window"
driver.get(url)
time.sleep(2)

switch_button = driver.find_element(By.ID, "new-tab-button")
switch_button.click()
time.sleep(2)

# print window handle
windows = driver.window_handles
print(windows)
# print("Driver is in this window: ", driver.current_window_handle)
driver.switch_to.window(windows[0])       # Switching between the windows from the list 
time.sleep(2)
print(driver.current_window_handle)


driver.quit()
