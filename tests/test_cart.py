import pytest

from pages.cart_page import CartPage


@pytest.mark.smoke
def test_adding_items_updates_cart_badge(inventory_page):
    inventory_page.add_items(2)
    assert inventory_page.cart_count() == 2


def test_cart_shows_added_item(inventory_page, driver):
    inventory_page.add_items(1)
    expected = inventory_page.item_names()[0]
    inventory_page.open_cart()
    assert CartPage(driver).item_names() == [expected]


def test_removing_item_empties_cart(inventory_page, driver):
    inventory_page.add_items(1)
    inventory_page.open_cart()
    cart = CartPage(driver)
    cart.remove_first_item()
    assert cart.item_names() == []
