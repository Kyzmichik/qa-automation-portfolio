from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", help="Show the browser window (default: headless)")


@pytest.fixture
def driver(request):
    """Fresh Chrome browser for every UI test, closed afterwards."""
    options = Options()
    if not request.config.getoption("--headed"):
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Turn off Chrome's password-leak popup, which blocks clicks on saucedemo
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    drv = webdriver.Chrome(options=options)  # Selenium Manager downloads the driver automatically
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Save a screenshot when a UI test fails, so the bug is easy to reproduce."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed and "driver" in item.fixturenames:
        drv = item.funcargs["driver"]
        folder = Path("screenshots")
        folder.mkdir(exist_ok=True)
        drv.save_screenshot(str(folder / f"{item.name}.png"))
