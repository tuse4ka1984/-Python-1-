from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация браузера Chrome
driver = webdriver.Chrome()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Ввести текст 1000, очистить поле и ввести текст 999
input_field = driver.find_element(By.XPATH,"//input[@type='number']")
input_field.send_keys("1000")
input_field.clear()
input_field.send_keys("999")

# Закрыть браузер
driver.quit()
