"""Products inventory page actions."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class ProductsPage(BasePage):
    def wait_until_loaded(self):
        self.wait.until(EC.url_contains("inventory.html"))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='inventory-item-name']")))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='title']")))

    def title(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-test='title']").text.strip()

    def product_names(self):
        return [item.text.strip() for item in self.driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-name']")]

    def product_prices(self):
        return [item.text.strip() for item in self.driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-price']")]

    def product_images(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "img[data-test^='inventory-item-']")

    def sort_by(self, value):
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='product-sort-container']"))
        )
        Select(dropdown).select_by_value(value)
        self.wait.until(
            lambda d: Select(
                d.find_element(By.CSS_SELECTOR, "[data-test='product-sort-container']")
            ).first_selected_option.get_attribute("value")
            == value
        )

    def open_product(self, link_id):
        self.wait.until(EC.element_to_be_clickable((By.ID, link_id))).click()
        self.wait.until(EC.url_contains("inventory-item.html"))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".inventory_details_name")))

    def detail_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".inventory_details_name").text.strip()

    def detail_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-price']").text.strip()

    def detail_description(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-desc']").text.strip()

    def back_to_products(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "back-to-products"))).click()
        self.wait_until_loaded()

    def add_product(self, button_id):
        self.wait.until(EC.element_to_be_clickable((By.ID, button_id))).click()
        remove_button_id = button_id.replace("add-to-cart-", "remove-", 1)
        self.wait.until(EC.visibility_of_element_located((By.ID, remove_button_id)))

    def remove_product(self, button_id):
        self.wait.until(EC.element_to_be_clickable((By.ID, button_id))).click()
