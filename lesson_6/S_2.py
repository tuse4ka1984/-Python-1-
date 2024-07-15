from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# Переход на сайт
driver.get("http://uitestingplayground.com/textinput")

# Указание текста в поле ввода
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

# Нажатие на синюю кнопку
button = driver.find_element(By.ID, "updatingButton")
button.click()

# Получение текста кнопки и вывод в консоль
print(button.text)

# Закрыть браузер
driver.quit()