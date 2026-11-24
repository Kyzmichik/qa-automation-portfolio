import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import LOCKED_OUT_USER, PASSWORD, STANDARD_USER, UI_BASE_URL

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_login_with_valid_credentials(driver):
    LoginPage(driver).open().login(STANDARD_USER, PASSWORD)

    inventory = InventoryPage(driver)
    assert inventory.title() == "Products"
    assert "/inventory.html" in driver.current_url


@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("", PASSWORD, "Username is required"),
        (STANDARD_USER, "", "Password is required"),
        (STANDARD_USER, "wrong_password", "Username and password do not match"),
        (LOCKED_OUT_USER, PASSWORD, "this user has been locked out"),
    ],
    ids=["empty-username", "empty-password", "wrong-password", "locked-out-user"],
)
def test_login_negative(driver, username, password, expected_error):
    login = LoginPage(driver).open()
    login.login(username, password)

    assert expected_error in login.error_message()
    assert "/inventory.html" not in driver.current_url


@pytest.mark.regression
def test_logout_returns_to_login_page(driver, inventory):
    inventory.logout()

    assert LoginPage(driver).is_visible(LoginPage.LOGIN_BUTTON)


@pytest.mark.regression
def test_inventory_is_protected_without_login(driver):
    """Opening the product page directly must not bypass authentication."""
    driver.get(f"{UI_BASE_URL}/inventory.html")

    assert "You can only access '/inventory.html' when you are logged in" in LoginPage(driver).error_message()
