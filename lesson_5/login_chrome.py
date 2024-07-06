from selenium import webdriver

# Инициализация браузера Chrome
driver = webdriver.Chrome()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/login")

# Ввести username и пароль, и нажать кнопку Login

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR,".radius").click()

# Закрыть браузер
driver.quit()