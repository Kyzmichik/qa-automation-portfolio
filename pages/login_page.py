from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config import UI_BASE_URL


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get(UI_BASE_URL)
        return self

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def error_message(self) -> str:
        return self.text_of(self.ERROR)
