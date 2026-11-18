"""Checkout module tests."""

from decimal import Decimal, ROUND_HALF_UP

from selenium.webdriver.common.by import By
from data import (
    ADD_BACKPACK,
    FIRST_NAME_REQUIRED,
    LAST_NAME_REQUIRED,
    ORDER_HEADER,
    ORDER_TEXT,
    POSTAL_CODE_REQUIRED,
)
from helpers import save_screenshot, start_checkout
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage


def money(amount):
    return Decimal(amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def test_CHECKOUT001_navigate_to_checkout(driver):
    checkout = start_checkout(driver)
    assert "checkout-step-one.html" in driver.current_url
    assert driver.find_element(By.CSS_SELECTOR, "[data-test='title']").text == "Checkout: Your Information"


def test_CHECKOUT002_valid_customer_details(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("Navya", "Shetty", "560043")
    checkout.continue_checkout()
    checkout.wait_for_overview()

    assert "checkout-step-two.html" in driver.current_url
    assert checkout.overview_item_names() == ["Sauce Labs Backpack"]


def test_CHECKOUT003_empty_first_name(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("", "Shetty", "560043")
    checkout.continue_checkout()
    assert checkout.error_message() == FIRST_NAME_REQUIRED


def test_CHECKOUT004_empty_last_name(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("Navya", "", "560043")
    checkout.continue_checkout()
    assert checkout.error_message() == LAST_NAME_REQUIRED


def test_CHECKOUT005_empty_postal_code(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("Navya", "Shetty", "")
    checkout.continue_checkout()
    assert checkout.error_message() == POSTAL_CODE_REQUIRED


def test_CHECKOUT006_overview_shows_selected_product(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("Navya", "Shetty", "560043")
    checkout.continue_checkout()
    checkout.wait_for_overview()
    save_screenshot(driver, "06_checkout_overview.png")

    assert checkout.overview_item_names() == ["Sauce Labs Backpack"]
    assert checkout.overview_prices() == ["$29.99"]


def test_CHECKOUT007_product_price_on_overview(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("Navya", "Shetty", "560043")
    checkout.continue_checkout()
    checkout.wait_for_overview()

    assert checkout.summary_value("subtotal-label") == "29.99"


def test_CHECKOUT008_tax_calculation(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("Navya", "Shetty", "560043")
    checkout.continue_checkout()
    checkout.wait_for_overview()

    subtotal = Decimal(checkout.summary_value("subtotal-label"))
    expected_tax = money(subtotal * Decimal("0.08"))
    assert checkout.summary_value("tax-label") == f"{expected_tax:.2f}"


def test_CHECKOUT009_total_amount(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("Navya", "Shetty", "560043")
    checkout.continue_checkout()
    checkout.wait_for_overview()

    subtotal = Decimal(checkout.summary_value("subtotal-label"))
    tax = Decimal(checkout.summary_value("tax-label"))
    expected_total = money(subtotal + tax)
    assert checkout.summary_value("total-label") == f"{expected_total:.2f}"
    assert checkout.summary_value("total-label") == "32.39"


def test_CHECKOUT010_cancel_information_page(driver):
    checkout = start_checkout(driver)
    checkout.cancel()
    cart = CartPage(driver)
    cart.wait_until_loaded()

    assert "cart.html" in driver.current_url
    assert cart.item_names() == ["Sauce Labs Backpack"]


def test_CHECKOUT011_complete_order(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("Navya", "Shetty", "560043")
    checkout.continue_checkout()
    checkout.wait_for_overview()
    checkout.finish()

    assert "checkout-complete.html" in driver.current_url
    assert checkout.confirmation_header() == ORDER_HEADER


def test_CHECKOUT012_order_confirmation(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("Navya", "Shetty", "560043")
    checkout.continue_checkout()
    checkout.wait_for_overview()
    checkout.finish()
    save_screenshot(driver, "07_order_confirmation_automation.png")

    assert checkout.confirmation_header() == ORDER_HEADER
    assert checkout.confirmation_text() == ORDER_TEXT
    assert checkout.confirmation_buttons() == ["Back Home", "Generate PDF order"]


def test_CHECKOUT013_cancel_overview(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("Navya", "Shetty", "560043")
    checkout.continue_checkout()
    checkout.wait_for_overview()
    checkout.cancel()

    products = ProductsPage(driver)
    products.wait_until_loaded()
    assert products.cart_badge_count() == 1
    products.open_cart()
    cart = CartPage(driver)
    cart.wait_until_loaded()
    assert cart.item_names() == ["Sauce Labs Backpack"]


def test_CHECKOUT014_all_customer_fields_empty(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("", "", "")
    checkout.continue_checkout()
    assert checkout.error_message() == FIRST_NAME_REQUIRED


def test_CHECKOUT015_only_first_name(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("Navya", "", "")
    checkout.continue_checkout()
    assert checkout.error_message() == LAST_NAME_REQUIRED


def test_CHECKOUT016_only_last_name(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("", "Shetty", "")
    checkout.continue_checkout()
    assert checkout.error_message() == FIRST_NAME_REQUIRED


def test_CHECKOUT017_only_postal_code(driver):
    checkout = start_checkout(driver)
    checkout.fill_information("", "", "560043")
    checkout.continue_checkout()
    assert checkout.error_message() == FIRST_NAME_REQUIRED


def test_CHECKOUT018_single_character_values_accepted(driver):
    checkout = start_checkout(driver, ADD_BACKPACK)
    checkout.fill_information("A", "B", "1")
    checkout.continue_checkout()
    checkout.wait_for_overview()
    assert "checkout-step-two.html" in driver.current_url
