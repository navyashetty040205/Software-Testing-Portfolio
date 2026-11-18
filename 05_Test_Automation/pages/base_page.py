"""Shared page actions used by more than one SauceDemo screen."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_menu(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))

    def close_menu(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "react-burger-cross-btn"))).click()
        self.wait.until(
            lambda d: d.find_element(By.CSS_SELECTOR, ".bm-menu-wrap").get_attribute("aria-hidden") == "true"
        )

    def menu_item_text(self, element_id):
        return self.driver.find_element(By.ID, element_id).text.strip()

    def logout(self):
        self.open_menu()
        self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))

    def reset_app_state(self):
        self.open_menu()
        self.wait.until(EC.element_to_be_clickable((By.ID, "reset_sidebar_link"))).click()
        self.wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")) == 0)

    def cart_badge_count(self):
        badges = self.driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")
        if not badges:
            return 0
        return int(badges[0].text)

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='shopping-cart-link']"))).click()
        self.wait.until(EC.url_contains("cart.html"))
