import pytest

from pages.cart_page import CartPage

pytestmark = pytest.mark.ui

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


@pytest.mark.smoke
def test_add_item_updates_cart_badge(inventory):
    inventory.add_to_cart(BACKPACK)

    assert inventory.cart_count() == 1


@pytest.mark.regression
def test_remove_item_clears_cart_badge(inventory):
    inventory.add_to_cart(BACKPACK)
    inventory.remove_from_cart(BACKPACK)

    assert inventory.cart_count() == 0


@pytest.mark.regression
def test_cart_contains_selected_items(driver, inventory):
    inventory.add_to_cart(BACKPACK)
    inventory.add_to_cart(BIKE_LIGHT)
    inventory.open_cart()

    assert sorted(CartPage(driver).item_names()) == sorted([BACKPACK, BIKE_LIGHT])


@pytest.mark.regression
def test_product_list_shows_six_items(inventory):
    assert inventory.items_count() == 6


@pytest.mark.regression
@pytest.mark.parametrize(
    "option, reverse",
    [("Price (low to high)", False), ("Price (high to low)", True)],
)
def test_sort_by_price(inventory, option, reverse):
    inventory.sort_by(option)

    prices = inventory.product_prices()
    assert prices == sorted(prices, reverse=reverse)


@pytest.mark.regression
def test_sort_by_name_z_to_a(inventory):
    inventory.sort_by("Name (Z to A)")

    names = inventory.product_names()
    assert names == sorted(names, reverse=True)
