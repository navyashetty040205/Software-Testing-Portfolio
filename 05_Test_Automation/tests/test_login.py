"""Login module tests. IDs match 02_Test_Case_Design/Test_Cases.md."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from helpers import save_screenshot
from data import (
    INVALID_CREDENTIALS,
    LOCKED_OUT_MESSAGE,
    LOCKED_OUT_USER,
    PASSWORD,
    PASSWORD_REQUIRED,
    PERFORMANCE_USER,
    PROBLEM_USER,
    STANDARD_USER,
    USERNAME_REQUIRED,
)
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_LOGIN001_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)

    products = ProductsPage(driver)
    products.wait_until_loaded()

    assert products.title() == "Products"
    assert len(products.product_names()) == 6


def test_LOGIN002_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("wrong_user", PASSWORD)

    assert login_page.error_message() == INVALID_CREDENTIALS
    assert "inventory.html" not in driver.current_url
    save_screenshot(driver, "05_invalid_login_error.png")


def test_LOGIN003_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(STANDARD_USER, "wrong_password")

    assert login_page.error_message() == INVALID_CREDENTIALS
    assert login_page.is_displayed()


def test_LOGIN004_both_credentials_invalid(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("invalid_user", "invalid_password")

    assert login_page.error_message() == INVALID_CREDENTIALS


def test_LOGIN005_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("", PASSWORD)

    assert login_page.error_message() == USERNAME_REQUIRED


def test_LOGIN006_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(STANDARD_USER, "")

    assert login_page.error_message() == PASSWORD_REQUIRED


def test_LOGIN007_both_fields_empty(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("", "")

    assert login_page.error_message() == USERNAME_REQUIRED


def test_LOGIN008_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(LOCKED_OUT_USER, PASSWORD)

    assert login_page.error_message() == LOCKED_OUT_MESSAGE
    assert "inventory.html" not in driver.current_url


def test_LOGIN009_problem_user_can_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(PROBLEM_USER, PASSWORD)

    products = ProductsPage(driver)
    products.wait_until_loaded()
    assert products.title() == "Products"


def test_LOGIN010_performance_glitch_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(PERFORMANCE_USER, PASSWORD)

    products = ProductsPage(driver)
    products.wait_until_loaded()
    assert products.title() == "Products"
    assert len(products.product_names()) == 6


def test_LOGIN011_error_message_can_be_closed(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("wrong_user", PASSWORD)
    assert login_page.error_message() == INVALID_CREDENTIALS

    login_page.dismiss_error()
    assert driver.find_elements(By.CSS_SELECTOR, "[data-test='error']") == []


def test_LOGIN012_logout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)
    ProductsPage(driver).wait_until_loaded()

    products = ProductsPage(driver)
    products.logout()

    assert login_page.is_displayed()
    driver.get("https://www.saucedemo.com/inventory.html")
    login_page.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
    assert "inventory.html" not in driver.current_url
