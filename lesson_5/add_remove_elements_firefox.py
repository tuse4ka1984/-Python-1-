from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация браузера Firefox
driver = webdriver.Firefox()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Кликнуть 5 раз на кнопку Add Element
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_button.click()

# Собрать список кнопок Delete и вывести их количество
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
print(f"Количество кнопок Delete: {len(delete_buttons)}")

# Закрыть браузер
driver.quit()
