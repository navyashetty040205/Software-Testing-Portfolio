"""Pytest fixtures for SauceDemo browser tests."""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

collect_ignore = ["test_login.py"]


def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Show the Chrome window instead of running headless.",
    )


@pytest.fixture
def driver(request):
    """Open Chrome for one test and always close it afterwards."""
    options = Options()
    if not request.config.getoption("--headed"):
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    try:
        yield browser
    finally:
        browser.quit()
