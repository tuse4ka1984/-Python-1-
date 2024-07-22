import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# Открываем страницу калькулятора
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

# Ввод значения в поле delay
driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

# Нажимаем на кнопки калькулятора
driver.find_element(By.XPATH, "//button[text()='7']").click()
driver.find_element(By.XPATH, "//button[text()='+']").click()
driver.find_element(By.XPATH, "//button[text()='8']").click()
driver.find_element(By.XPATH, "//button[text()='=']").click()

# Ждем 45 секунд для получения результата
time.sleep(45)

# Получаем результат из окна вывода
result = driver.find_element(By.CSS_SELECTOR, "#output").text

# Проверяем, что результат равен 15
assert result == "15", f"Expected result to be 15, but got {result}"

# Закрываем браузер
driver.quit()

if __name__ == "__main__":
    pytest.main()