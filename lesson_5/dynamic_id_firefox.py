from selenium import webdriver

# Инициализация браузера Firefox
driver = webdriver.Firefox()

# Открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Кликнуть на синюю кнопку
blue_button = driver.find_element_by_xpath("//button[contains(@class, 'btn-primary')]")
blue_button.click()

# Закрыть браузер
driver.quit()