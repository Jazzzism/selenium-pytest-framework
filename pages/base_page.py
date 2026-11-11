from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    URL = "https://www.saucedemo.com"
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    def find(self, locator):
        """Wait until the element is visible, then return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_present(self, locator):
        """Wait until the element exists in the DOM (even if it has no size)."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def text_of(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        try:
            self.find(locator)
            return True
        except TimeoutException:
            return False
