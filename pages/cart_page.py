from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_LIST = (By.CSS_SELECTOR, "[data-test='cart-list']")
    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove']")

    def item_names(self):
        self.wait_present(self.CART_LIST)
        return [e.text for e in self.driver.find_elements(*self.ITEM_NAMES)]

    def remove_first_item(self):
        self.click(self.REMOVE_BUTTONS)
