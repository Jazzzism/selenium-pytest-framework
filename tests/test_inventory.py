import pytest


@pytest.mark.smoke
def test_inventory_shows_six_products(inventory_page):
    assert inventory_page.item_count() == 6


def test_sort_price_low_to_high(inventory_page):
    inventory_page.sort_by("lohi")
    prices = inventory_page.item_prices()
    assert prices == sorted(prices)


def test_sort_name_z_to_a(inventory_page):
    inventory_page.sort_by("za")
    names = inventory_page.item_names()
    assert names == sorted(names, reverse=True)
