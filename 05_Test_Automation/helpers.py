"""Small workflows reused by the test modules."""

from pathlib import Path

from data import ADD_BACKPACK, PASSWORD, STANDARD_USER
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def login_as(driver, username=STANDARD_USER, password=PASSWORD):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    products = ProductsPage(driver)
    products.wait_until_loaded()
    return products


def add_to_cart_and_open(driver, *button_ids):
    products = login_as(driver)
    for button_id in button_ids:
        products.add_product(button_id)
    products.open_cart()
    cart = CartPage(driver)
    cart.wait_until_loaded()
    return cart


def start_checkout(driver, button_id=ADD_BACKPACK):
    cart = add_to_cart_and_open(driver, button_id)
    cart.checkout()
    checkout = CheckoutPage(driver)
    checkout.wait_for_information_page()
    return checkout


def save_screenshot(browser, filename):
    """Save a real browser screenshot into the project evidence folder."""
    screenshot_dir = Path(__file__).resolve().parents[1] / "07_Screenshots"
    screenshot_dir.mkdir(exist_ok=True)
    browser.save_screenshot(str(screenshot_dir / filename))
