import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

pytestmark = pytest.mark.ui


@pytest.fixture
def checkout(driver, inventory) -> CheckoutPage:
    """Precondition: one item in the cart, user is on the checkout form."""
    inventory.add_to_cart("Sauce Labs Backpack")
    inventory.open_cart()
    CartPage(driver).checkout()
    return CheckoutPage(driver)


@pytest.mark.smoke
def test_complete_purchase_end_to_end(checkout):
    checkout.fill_info("Ihor", "Koval", "46001")
    checkout.finish()

    assert checkout.complete_message() == "Thank you for your order!"


@pytest.mark.regression
def test_order_total_equals_subtotal_plus_tax(checkout):
    checkout.fill_info("Ihor", "Koval", "46001")

    assert checkout.total() == pytest.approx(checkout.subtotal() + checkout.tax(), abs=0.01)


@pytest.mark.regression
@pytest.mark.parametrize(
    "first, last, postal, expected_error",
    [
        ("", "Koval", "46001", "First Name is required"),
        ("Ihor", "", "46001", "Last Name is required"),
        ("Ihor", "Koval", "", "Postal Code is required"),
    ],
    ids=["no-first-name", "no-last-name", "no-postal-code"],
)
def test_checkout_form_validation(checkout, first, last, postal, expected_error):
    checkout.fill_info(first, last, postal)

    assert expected_error in checkout.error_message()
