
from pages.login import loginpage
from pages.inventory import inventorypage
from pages.cart import cartpage
from pages.checkout import checkoutpage


def test_end_to_end(driver):

    # Step 1: Login
    login = loginpage(driver)
    login.open_url("https://www.saucedemo.com/")
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    # Step 2: Inventory page
    inventory = inventorypage(driver)
    inventory.sort_products()
    inventory.add_fleece_jacket()
    inventory.add_backpack()
    inventory.add_onesie()

    # Verify that 3 products were added
    assert inventory.get_cart_count() == "3"

    # Step 3: Cart page
    inventory.open_cart()

    cart = cartpage(driver)
    assert cart.get_cart_items_count() == 3
    cart.click_checkout()

    # Step 4: Checkout page
    checkout = checkoutpage(driver)
    checkout.enter_first_name("Suzan")
    checkout.enter_last_name("Rizal")
    checkout.enter_postal_code("44600")
    checkout.click_continue()

    # Step 5: Finish the order
    checkout.click_finish()

    # Verify successful order
    assert checkout.get_success_message() == "Thank you for your order!"

