import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test data (field id -> value). Edit these as you like.
data = {"userName": "Nora Frank",
        "userEmail": "noraijk@gmail.com",
        "currentAddress": "Kattookaran house church road, Porthissery, Irinjalakuda North 680125",
        "permanentAddress": "Kattookaran house church road, Porthissery, Irinjalakuda North 680125"}

driver = webdriver.Chrome()                        # 1. launch browser
try:
    driver.maximize_window()
    driver.get("https://demoqa.com/text-box")      # 2. open the page

    for field_id, value in data.items():           # 3. fill the form
        driver.find_element(By.ID, field_id).send_keys(value)

    btn = driver.find_element(By.ID, "submit")     # 4. submit (JS click avoids ad overlay)
    driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", btn)

    # 5. verify the displayed output
    output = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "output"))).text
    for field_id, value in data.items():
        print(f"{field_id:17}:", "PASS" if value in output else "FAIL")
    time.sleep(3)                                  # pause so the result is visible
finally:
    driver.quit()                                  # 6. close the browser
