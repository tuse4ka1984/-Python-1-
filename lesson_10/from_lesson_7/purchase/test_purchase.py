import allure
from selenium import webdriver
from pages.purchase_page import Auth, Prod, Cart, Info, Overview

@allure.title("Тест покупки товара")
@allure.description("Тест, проверяющий функциональность покупки товара в интернет-магазине")
@allure.feature("Покупка товара")
@allure.severity(allure.Severity.CRITICAL)
def test_buy():
    browser = webdriver.Chrome()
    
    with allure.step("Открытие страницы авторизации"):
        authPage = Auth(browser)
        authPage.open()
        
    with allure.step("Авторизация пользователя"):
        authPage.authorization("standard_user", "secret_sauce")
        authPage.button()
        
    with allure.step("Добавление товара в корзину"):
        products = Prod(browser)
        products.add_to_cart()
        
    with allure.step("Переход в корзину"):
        products.cart()
        
    with allure.step("Проверка содержимого корзины"):
        cart = Cart(browser)
        cart.check()
        
    with allure.step("Заполнение информации о покупке"):
        info = Info(browser)
        info.first_name("Наталья")
        info.last_name("Юхно")
        info.postal_code("432029")
        info.button_continue()
        
    with allure.step("Проверка результата покупки"):
        res = Overview(browser)
        result = res.result()
        assert result == "Total: $58.29", f"Ожидали 'Total: $58.29', но получили '{result}'"
        
    browser.quit()