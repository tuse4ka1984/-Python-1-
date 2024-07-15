from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# Переход на страницу
driver.get("http://uitestingplayground.com/ajax")

# Нажатие на синюю кнопку
button = driver.find_element(By.ID, "ajaxButton")
button.click()

# Ожидание появления зеленой плашки и получение текста
wait = WebDriverWait(driver, 10)
green_label = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success")))
print(green_label.text)

# Закрыть браузер
driver.quit()