from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")
    ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    SORT_SELECT = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    @staticmethod
    def _slug(product_name: str) -> str:
        # "Sauce Labs Backpack" -> "sauce-labs-backpack" (matches the button ids on the page)
        return product_name.lower().replace(" ", "-")

    def title(self) -> str:
        return self.text_of(self.TITLE)

    def items_count(self) -> int:
        self.find(self.ITEMS)
        return len(self.find_all(self.ITEMS))

    def add_to_cart(self, product_name):
        self.click((By.ID, f"add-to-cart-{self._slug(product_name)}"))

    def remove_from_cart(self, product_name):
        self.click((By.ID, f"remove-{self._slug(product_name)}"))

    def cart_count(self) -> int:
        badges = self.find_all(self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def sort_by(self, visible_text):
        Select(self.find(self.SORT_SELECT)).select_by_visible_text(visible_text)

    def product_names(self) -> list[str]:
        return [e.text for e in self.find_all(self.ITEM_NAMES)]

    def product_prices(self) -> list[float]:
        return [float(e.text.replace("$", "")) for e in self.find_all(self.ITEM_PRICES)]

    def open_cart(self):
        self.click(self.CART_LINK)

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
