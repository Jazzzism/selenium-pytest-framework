from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    ITEM_PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    SORT = (By.CSS_SELECTOR, "[data-test='product-sort-container']")

    def is_loaded(self):
        try:
            return self.text_of(self.TITLE) == "Products"
        except TimeoutException:
            return False

    def item_count(self):
        return len(self.driver.find_elements(*self.ITEMS))

    def item_names(self):
        return [e.text for e in self.driver.find_elements(*self.ITEM_NAMES)]

    def item_prices(self):
        return [
            float(e.text.replace("$", ""))
            for e in self.driver.find_elements(*self.ITEM_PRICES)
        ]

    def sort_by(self, value):
        """value is one of: az, za, lohi, hilo"""
        Select(self.find(self.SORT)).select_by_value(value)

    def add_items(self, count):
        # After a click the button turns into "Remove", so the first
        # remaining "Add to cart" button is always the next product.
        for _ in range(count):
            self.click(self.ADD_BUTTONS)

    def cart_count(self):
        try:
            return int(self.text_of(self.CART_BADGE))
        except TimeoutException:
            return 0

    def open_cart(self):
        self.click(self.CART_LINK)
