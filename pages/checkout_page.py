import re

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    SUBTOTAL = (By.CSS_SELECTOR, ".summary_subtotal_label")
    TAX = (By.CSS_SELECTOR, ".summary_tax_label")
    TOTAL = (By.CSS_SELECTOR, ".summary_total_label")
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")

    def fill_info(self, first, last, postal):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE)

    def error_message(self) -> str:
        return self.text_of(self.ERROR)

    def _amount(self, locator) -> float:
        # "Item total: $29.99" -> 29.99
        return float(re.search(r"\$([\d.]+)", self.text_of(locator)).group(1))

    def subtotal(self) -> float:
        return self._amount(self.SUBTOTAL)

    def tax(self) -> float:
        return self._amount(self.TAX)

    def total(self) -> float:
        return self._amount(self.TOTAL)

    def finish(self):
        self.click(self.FINISH)

    def complete_message(self) -> str:
        return self.text_of(self.COMPLETE_HEADER)
