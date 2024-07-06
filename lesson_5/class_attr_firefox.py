from selenium import webdriver

# Инициализация браузера Firefox
driver = webdriver.Firefox()

# Открыть страницу
driver.get("http://uitestingplayground.com/classattr")

# Кликнуть на синюю кнопку
blue_button = driver.find_element(By.XPATH,"//button[contains(@class, 'btn-primary')]")
blue_button.click()

# Закрыть браузер
driver.quit()
