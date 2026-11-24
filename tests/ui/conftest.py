import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import PASSWORD, STANDARD_USER


@pytest.fixture
def inventory(driver) -> InventoryPage:
    """Precondition for most UI tests: user is logged in and sees the product list."""
    LoginPage(driver).open().login(STANDARD_USER, PASSWORD)
    page = InventoryPage(driver)
    assert page.title() == "Products"
    return page
