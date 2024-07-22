from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# 1. Открываем сайт магазина
driver.get("https://www.saucedemo.com/")

# 2. Авторизуемся как пользователь standard_user
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()


# 3. Добавляем в корзину товары
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

# 4. Переходим в корзину
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# 5. Нажимаем Checkout
driver.find_element(By.ID, "checkout").click()

# 6. Заполняем форму своими данными
driver.find_element(By.ID, "first-name").send_keys("Наталья")  # Имя
driver.find_element(By.ID, "last-name").send_keys("Юхно")  # Фамилия
driver.find_element(By.ID, "postal-code").send_keys("12345")  # Почтовый индекс
driver.find_element(By.XPATH, "//input[@value='Continue']").click()

# 7. Прочитаем со страницы итоговую стоимость (Total)
total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text

# 8. Закрываем браузер
driver.quit()

# 9. Проверяем, что итоговая сумма равна $58.29
assert total_cost == "Total: $58.29", f"Expected total to be $58.29, but got {total_cost}"