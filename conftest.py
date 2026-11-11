import os
import re

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run Chrome with a visible window (default is headless)",
    )


@pytest.fixture
def driver(request):
    options = Options()
    if not request.config.getoption("--headed"):
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )
    # Selenium Manager downloads the matching ChromeDriver automatically.
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver).open()


@pytest.fixture
def inventory_page(driver, login_page):
    login_page.login("standard_user", "secret_sauce")
    page = InventoryPage(driver)
    assert page.is_loaded(), "Login did not reach the inventory page"
    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Save a screenshot whenever a test fails."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        browser = item.funcargs.get("driver")
        if browser:
            os.makedirs("reports/screenshots", exist_ok=True)
            safe_name = re.sub(r"[^\w.-]", "_", item.name)
            browser.save_screenshot(f"reports/screenshots/{safe_name}.png")
