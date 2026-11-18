"""Menu, logout, refresh, and browser history tests."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from data import ADD_BACKPACK, BASE_URL
from helpers import login_as
from pages.cart_page import CartPage
from pages.login_page import LoginPage


def test_NAV001_menu_opens(driver):
    products = login_as(driver)
    products.open_menu()

    assert products.menu_item_text("inventory_sidebar_link") == "All Items"
    assert products.menu_item_text("about_sidebar_link") == "About"
    assert products.menu_item_text("logout_sidebar_link") == "Logout"
    assert products.menu_item_text("reset_sidebar_link") == "Reset App State"


def test_NAV002_menu_closes(driver):
    products = login_as(driver)
    products.open_menu()
    products.close_menu()

    hidden = driver.find_element(By.CSS_SELECTOR, ".bm-menu-wrap").get_attribute("aria-hidden")
    assert hidden == "true"


def test_NAV003_about_link(driver):
    products = login_as(driver)
    products.open_menu()
    products.wait.until(EC.element_to_be_clickable((By.ID, "about_sidebar_link"))).click()
    products.wait.until(EC.url_contains("saucelabs.com"))

    assert "saucelabs.com" in driver.current_url


def test_NAV004_reset_app_state(driver):
    products = login_as(driver)
    products.add_product(ADD_BACKPACK)
    assert products.cart_badge_count() == 1

    products.reset_app_state()
    assert products.cart_badge_count() == 0
    products.open_cart()
    cart = CartPage(driver)
    cart.wait_until_loaded()
    assert cart.item_names() == []


def test_NAV005_refresh_keeps_session_and_cart(driver):
    products = login_as(driver)
    products.add_product(ADD_BACKPACK)
    driver.refresh()
    products.wait_until_loaded()

    assert "inventory.html" in driver.current_url
    assert products.cart_badge_count() == 1
    assert products.title() == "Products"


def test_NAV006_back_from_products(driver):
    login_as(driver)
    driver.back()
    login_page = LoginPage(driver)
    login_page.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))

    assert driver.current_url.rstrip("/") == BASE_URL.rstrip("/")
    assert login_page.is_displayed()


def test_NAV007_forward_returns_to_products(driver):
    products = login_as(driver)
    driver.back()
    LoginPage(driver).wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
    driver.forward()
    products.wait_until_loaded()

    assert "inventory.html" in driver.current_url
    assert len(products.product_names()) == 6


def test_NAV008_inventory_requires_login(driver):
    products = login_as(driver)
    products.logout()
    driver.get(BASE_URL + "inventory.html")
    LoginPage(driver).wait.until(EC.visibility_of_element_located((By.ID, "login-button")))

    assert "inventory.html" not in driver.current_url
