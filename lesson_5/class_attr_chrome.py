from selenium import webdriver

# Инициализация браузера Chrome
driver = webdriver.Chrome()

# Открыть страницу
driver.get("http://uitestingplayground.com/classattr")

# Кликнуть на синюю кнопку
blue_button = driver.find_element_by_xpath("//button[contains(@class, 'btn-primary')]")
blue_button.click()

# Закрыть браузер
driver.quit()