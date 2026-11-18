"""Shopping cart page actions."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    def wait_until_loaded(self):
        self.wait.until(EC.url_contains("cart.html"))
        self.wait.until(EC.visibility_of_element_located((By.ID, "checkout")))

    def item_names(self):
        return [item.text.strip() for item in self.driver.find_elements(By.CSS_SELECTOR, ".cart_item .inventory_item_name")]

    def item_prices(self):
        return [item.text.strip() for item in self.driver.find_elements(By.CSS_SELECTOR, ".cart_item .inventory_item_price")]

    def item_quantities(self):
        return [item.text.strip() for item in self.driver.find_elements(By.CSS_SELECTOR, ".cart_quantity")]

    def remove(self, button_id):
        self.wait.until(EC.element_to_be_clickable((By.ID, button_id))).click()

    def continue_shopping(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue-shopping"))).click()
        self.wait.until(EC.url_contains("inventory.html"))

    def checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
        self.wait.until(EC.url_contains("checkout-step-one.html"))
