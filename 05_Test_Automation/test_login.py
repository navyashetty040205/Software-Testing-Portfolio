import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome
driver = webdriver.Chrome()

try:
    # Open SauceDemo website
    driver.get("https://www.saucedemo.com/")

    # Maximize browser window
    driver.maximize_window()

    # Enter valid username
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    # Enter valid password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click login button
    driver.find_element(By.ID, "login-button").click()

    # Wait until Products page loads
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    # Verify login result
    if "inventory.html" in driver.current_url:
        print("TEST PASSED: Login successful!")
        print("Products page opened successfully.")

        # Keep Chrome open for 5 seconds
        time.sleep(5)

    else:
        print("TEST FAILED: Login unsuccessful.")

except Exception as e:
    print("TEST FAILED:", e)

finally:
    # Close browser after test execution
    driver.quit()
