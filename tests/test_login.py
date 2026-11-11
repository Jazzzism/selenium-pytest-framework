import pytest

from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_valid_login_opens_inventory(login_page, driver):
    login_page.login("standard_user", "secret_sauce")
    assert InventoryPage(driver).is_loaded()


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("locked_out_user", "secret_sauce", "locked out"),
        ("standard_user", "wrong_password", "do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
    ids=["locked-out-user", "wrong-password", "missing-username", "missing-password"],
)
def test_invalid_login_shows_error(login_page, username, password, expected_error):
    login_page.login(username, password)
    assert expected_error in login_page.error_message()
