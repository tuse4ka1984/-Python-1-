from selenium import webdriver

from pages.purchase_page import Auth
from pages.purchase_page import Prod
from pages.purchase_page import Cart
from pages.purchase_page import Info
from pages.purchase_page import Overview


def test_buy():
    browser = webdriver.Chrome()

    authPage = Auth(browser)
    authPage.open()
    authPage.authorization("standard_user", "secret_sauce")
    authPage.button()

    products = Prod(browser)
    products.add_to_cart()
    products.cart()

    cart = Cart(browser)
    cart.check()

    info = Info(browser)
    info.first_name("Елена")
    info.last_name("Хайбулкина")
    info.postal_code("432029")
    info.button_continue()

    res = Overview(browser)
    res.result()

    assert res.result() == "Total: $58.29"
    browser.quit()