"""Login page actions."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from data import BASE_URL
from pages.base_page import BasePage


class LoginPage(BasePage):
    def open(self):
        self.driver.get(BASE_URL)
        self.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

    def login(self, username, password):
        username_field = self.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        password_field = self.driver.find_element(By.ID, "password")
        username_field.clear()
        password_field.clear()
        if username:
            username_field.send_keys(username)
        if password:
            password_field.send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def error_message(self):
        error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
        return error.text.strip()

    def dismiss_error(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='error-button']"))).click()
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))

    def is_displayed(self):
        return bool(self.driver.find_elements(By.ID, "login-button"))
