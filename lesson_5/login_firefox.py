from selenium import webdriver

# Инициализация браузера Firefox
driver = webdriver.Firefox()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/login")

# Ввести username и пароль, и нажать кнопку Login
driver.find_element_by_id("username").send_keys("tomsmith")
driver.find_element_by_id("password").send_keys("SuperSecretPassword!")
driver.find_element_by_css_selector(".radius").click()

# Закрыть браузер
driver.quit()
