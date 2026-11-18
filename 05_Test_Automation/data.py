"""Shared test data for the SauceDemo automation suite."""

BASE_URL = "https://www.saucedemo.com/"
PASSWORD = "secret_sauce"
STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
PROBLEM_USER = "problem_user"
PERFORMANCE_USER = "performance_glitch_user"

# Stable product order observed on the inventory page.
PRODUCTS_AZ = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)",
]
PRODUCTS_ZA = list(reversed(PRODUCTS_AZ))
PRODUCTS_LOHI = [
    "Sauce Labs Onesie",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Test.allTheThings() T-Shirt (Red)",
    "Sauce Labs Backpack",
    "Sauce Labs Fleece Jacket",
]
PRODUCTS_HILO = [
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Backpack",
    "Sauce Labs Bolt T-Shirt",
    "Test.allTheThings() T-Shirt (Red)",
    "Sauce Labs Bike Light",
    "Sauce Labs Onesie",
]

PRICES = {
    "Sauce Labs Backpack": "$29.99",
    "Sauce Labs Bike Light": "$9.99",
    "Sauce Labs Bolt T-Shirt": "$15.99",
    "Sauce Labs Fleece Jacket": "$49.99",
    "Sauce Labs Onesie": "$7.99",
    "Test.allTheThings() T-Shirt (Red)": "$15.99",
}

ADD_BACKPACK = "add-to-cart-sauce-labs-backpack"
ADD_BIKE_LIGHT = "add-to-cart-sauce-labs-bike-light"
ADD_ONESIE = "add-to-cart-sauce-labs-onesie"
REMOVE_BACKPACK = "remove-sauce-labs-backpack"
REMOVE_BIKE_LIGHT = "remove-sauce-labs-bike-light"

INVALID_CREDENTIALS = "Epic sadface: Username and password do not match any user in this service"
USERNAME_REQUIRED = "Epic sadface: Username is required"
PASSWORD_REQUIRED = "Epic sadface: Password is required"
LOCKED_OUT_MESSAGE = "Epic sadface: Sorry, this user has been locked out."

FIRST_NAME_REQUIRED = "Error: First Name is required"
LAST_NAME_REQUIRED = "Error: Last Name is required"
POSTAL_CODE_REQUIRED = "Error: Postal Code is required"

ORDER_HEADER = "Thank you for your order!"
ORDER_TEXT = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
