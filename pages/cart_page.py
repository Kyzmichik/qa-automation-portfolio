from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM_NAMES = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def item_names(self) -> list[str]:
        return [e.text for e in self.find_all(self.CART_ITEM_NAMES)]

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
