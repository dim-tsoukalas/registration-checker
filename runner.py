from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import datetime

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.geolocation" :2}
options.add_experimental_option("prefs",prefs)

# Set up the Chrome driver (change the path to the location of your chromedriver executable)
driver = webdriver.Chrome(options)

driver.get("https://tevis.ekom21.de/stdar/select2?md=4")


button = driver.find_element(By.ID, 'concerns_accordion-223')
button.click()

time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
button = driver.find_element(By.ID, 'button-plus-1916')
button.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

button = driver.find_element(By.ID, 'WeiterButton')
button.click()

time.sleep(1)

button = driver.find_element(By.ID, 'OKButton')
button.click()
time.sleep(1)

while True:
    # Refresh the page
    driver.refresh()

    # Wait for a specific element to load (or a timeout if the page doesn't change)
    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
    element_to_check = wait.until(EC.presence_of_element_located((By.ID, 'suggest_location_accordion')))  # Replace with the element you want to check

    # Get the content of the element
    current_content = element_to_check.text

    now = datetime.datetime.now()

    # Compare the current content with the previous content
    if 'previous_content' in locals() and current_content != previous_content:
        print("----------------------------------------------------------------------------")
        print (now.strftime("%Y-%m-%d %H:%M"))
        print("Page content has changed.")
        print(f"current_content:{current_content}")

        print(f"-previous_content:{previous_content}")
    else:
        print("----------------------------------------------------------------------------")
        print (now.strftime("%Y-%m-%d %H:%M"))
        print("NO change!")
    
    # Update the previous content
    previous_content = current_content

    time.sleep(60)
