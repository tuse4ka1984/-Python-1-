import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_purchase():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome()

    # Открываем сайт магазина
    driver.get("https://www.saucedemo.com/")

    # Авторизуемся как пользователь standard_user
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавляем в корзину товары
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Нажимаем Checkout
    driver.find_element(By.ID, "checkout").click()

    # Заполняем форму своими данными
    driver.find_element(By.ID, "first-name").send_keys("Наталья")
    driver.find_element(By.ID, "last-name").send_keys("Юхно")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    # Прочитываем со страницы итоговую стоимость (Total)
    total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text

    # Проверяем, что итоговая сумма равна $58.29
    assert total_cost == "Total: $58.29", f"Expected total to be $58.29, but got {total_cost}"

    # Закрываем браузер
    driver.quit()
