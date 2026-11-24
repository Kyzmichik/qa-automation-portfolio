from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.config import DEFAULT_TIMEOUT


class BasePage:
    """Common actions shared by all pages. Uses explicit waits instead of sleep()."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        field = self.find(locator)
        field.clear()
        field.send_keys(text)

    def text_of(self, locator) -> str:
        return self.find(locator).text

    def is_visible(self, locator) -> bool:
        elements = self.find_all(locator)
        return bool(elements) and elements[0].is_displayed()
