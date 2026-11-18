"""Products module tests."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from data import (
    PASSWORD,
    PRICES,
    PROBLEM_USER,
    PRODUCTS_AZ,
    PRODUCTS_HILO,
    PRODUCTS_LOHI,
    PRODUCTS_ZA,
)
from helpers import login_as, save_screenshot
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_PROD001_products_page_loads(driver):
    products = login_as(driver)
    assert products.title() == "Products"
    assert "inventory.html" in driver.current_url
    assert len(products.product_names()) == 6


def test_PROD002_names_and_prices_displayed(driver):
    products = login_as(driver)
    names = products.product_names()
    prices = products.product_prices()

    assert names == PRODUCTS_AZ
    assert prices == [PRICES[name] for name in names]


def test_PROD003_standard_user_images(driver):
    products = login_as(driver)
    products.wait.until(
        lambda d: "sauce-backpack"
        in (d.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-sauce-labs-backpack-img']").get_attribute("src") or "")
    )
    images = products.product_images()
    assert len(images) == 6
    for image in images:
        source = image.get_attribute("src") or ""
        alt_text = image.get_attribute("alt") or ""
        assert alt_text in PRODUCTS_AZ
        assert source.startswith("https://www.saucedemo.com/")
        assert "sl-404" not in source


def test_PROD004_sort_name_ascending(driver):
    products = login_as(driver)
    products.sort_by("az")
    assert products.product_names() == PRODUCTS_AZ


def test_PROD005_sort_name_descending(driver):
    products = login_as(driver)
    products.sort_by("za")
    assert products.product_names() == PRODUCTS_ZA


def test_PROD006_sort_price_ascending(driver):
    products = login_as(driver)
    products.sort_by("lohi")
    assert products.product_names() == PRODUCTS_LOHI
    amounts = [float(price.replace("$", "")) for price in products.product_prices()]
    assert amounts == sorted(amounts)


def test_PROD007_sort_price_descending(driver):
    products = login_as(driver)
    products.sort_by("hilo")
    assert products.product_names() == PRODUCTS_HILO
    amounts = [float(price.replace("$", "")) for price in products.product_prices()]
    assert amounts == sorted(amounts, reverse=True)


def test_PROD008_product_details(driver):
    products = login_as(driver)
    products.open_product("item_4_title_link")

    assert "inventory-item.html?id=4" in driver.current_url
    assert products.detail_name() == "Sauce Labs Backpack"
    assert products.detail_price() == "$29.99"
    assert "laptop" in products.detail_description().lower()


def test_PROD009_back_to_products(driver):
    products = login_as(driver)
    products.open_product("item_4_title_link")
    products.back_to_products()

    assert "inventory.html" in driver.current_url
    assert products.title() == "Products"
    assert len(products.product_names()) == 6


def test_PROD010_problem_user_images(driver):
    """Expected result is a correct product image for each product.

    problem_user currently shows the same missing-image placeholder for every
    product. This test records that defect instead of treating it as a pass.
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(PROBLEM_USER, PASSWORD)
    products = ProductsPage(driver)
    products.wait_until_loaded()

    images = products.product_images()
    broken = []
    for image in images:
        source = image.get_attribute("src") or ""
        if "sl-404" in source:
            broken.append(f"{image.get_attribute('alt')}: {source}")

    save_screenshot(driver, "08_problem_user_images.png")
    assert broken == [], "Product images should match the product. Broken images: " + "; ".join(broken)
