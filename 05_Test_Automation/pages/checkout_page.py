"""Checkout information, overview, and confirmation pages."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def wait_for_information_page(self):
        self.wait.until(EC.url_contains("checkout-step-one.html"))
        self.wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

    def fill_information(self, first_name, last_name, postal_code):
        self.wait_for_information_page()
        fields = {
            "first-name": first_name,
            "last-name": last_name,
            "postal-code": postal_code,
        }
        for field_id, value in fields.items():
            field = self.driver.find_element(By.ID, field_id)
            field.clear()
            if value:
                field.send_keys(value)

    def continue_checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    def cancel(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "cancel"))).click()

    def error_message(self):
        error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
        return error.text.strip()

    def wait_for_overview(self):
        self.wait.until(EC.url_contains("checkout-step-two.html"))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='total-label']")))

    def overview_item_names(self):
        return [item.text.strip() for item in self.driver.find_elements(By.CSS_SELECTOR, ".cart_item .inventory_item_name")]

    def overview_prices(self):
        return [item.text.strip() for item in self.driver.find_elements(By.CSS_SELECTOR, ".cart_item .inventory_item_price")]

    def summary_value(self, data_test):
        text = self.driver.find_element(By.CSS_SELECTOR, f"[data-test='{data_test}']").text
        return text.split("$", 1)[1].strip()

    def finish(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
        self.wait.until(EC.url_contains("checkout-complete.html"))

    def confirmation_header(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='complete-header']"))).text.strip()

    def confirmation_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-test='complete-text']").text.strip()

    def confirmation_buttons(self):
        return [button.text.strip() for button in self.driver.find_elements(By.CSS_SELECTOR, "[data-test='checkout-complete-container'] button")]
