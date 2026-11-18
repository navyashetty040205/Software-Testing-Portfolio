"""Shopping cart module tests."""

from selenium.webdriver.common.by import By

from data import ADD_BACKPACK, ADD_BIKE_LIGHT, ADD_ONESIE, REMOVE_BIKE_LIGHT
from helpers import add_to_cart_and_open, login_as
from pages.cart_page import CartPage
from pages.products_page import ProductsPage


def test_CART001_add_one_product(driver):
    products = login_as(driver)
    products.add_product(ADD_BACKPACK)

    assert products.cart_badge_count() == 1
    assert driver.find_element(By.ID, "remove-sauce-labs-backpack").text == "Remove"


def test_CART002_add_multiple_products(driver):
    cart = add_to_cart_and_open(driver, ADD_BACKPACK, ADD_BIKE_LIGHT)

    assert cart.cart_badge_count() == 2
    assert cart.item_names() == ["Sauce Labs Backpack", "Sauce Labs Bike Light"]


def test_CART003_remove_product(driver):
    cart = add_to_cart_and_open(driver, ADD_BACKPACK, ADD_BIKE_LIGHT)
    cart.remove(REMOVE_BIKE_LIGHT)

    assert cart.item_names() == ["Sauce Labs Backpack"]
    assert cart.cart_badge_count() == 1


def test_CART004_badge_count(driver):
    products = login_as(driver)
    assert products.cart_badge_count() == 0
    products.add_product(ADD_BACKPACK)
    assert products.cart_badge_count() == 1
    products.add_product(ADD_BIKE_LIGHT)
    assert products.cart_badge_count() == 2
    products.remove_product("remove-sauce-labs-backpack")
    assert products.cart_badge_count() == 1


def test_CART005_open_cart(driver):
    cart = add_to_cart_and_open(driver, ADD_ONESIE)

    assert "cart.html" in driver.current_url
    assert cart.item_names() == ["Sauce Labs Onesie"]


def test_CART006_empty_cart(driver):
    products = login_as(driver)
    products.open_cart()
    cart = CartPage(driver)
    cart.wait_until_loaded()

    assert cart.item_names() == []
    assert cart.cart_badge_count() == 0
    assert driver.find_elements(By.ID, "checkout")


def test_CART007_selected_product_details(driver):
    cart = add_to_cart_and_open(driver, ADD_BACKPACK)

    assert cart.item_names() == ["Sauce Labs Backpack"]
    assert cart.item_prices() == ["$29.99"]
    assert cart.item_quantities() == ["1"]


def test_CART008_continue_shopping(driver):
    cart = add_to_cart_and_open(driver, ADD_BACKPACK)
    cart.continue_shopping()
    products = ProductsPage(driver)
    products.wait_until_loaded()

    assert products.title() == "Products"
    assert products.cart_badge_count() == 1


def test_CART009_cart_persists_during_navigation(driver):
    products = login_as(driver)
    products.add_product("add-to-cart-sauce-labs-fleece-jacket")
    products.open_product("item_5_title_link")
    assert products.cart_badge_count() == 1

    products.open_cart()
    cart = CartPage(driver)
    cart.wait_until_loaded()
    assert cart.item_names() == ["Sauce Labs Fleece Jacket"]
    assert cart.item_prices() == ["$49.99"]
