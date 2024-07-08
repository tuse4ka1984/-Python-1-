from selenium import webdriver

from selenium.webdriver.common.by import By

# Инициализация браузера Firefox
driver = webdriver.Firefox()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Добавление небольшой задержки, чтобы модальное окно успело появиться
time.sleep(5)  # Задержка на 5 секунд

# Найти и закрыть модальное окно
close_button = driver.find_element(By.XPATH,"//div[@class='modal-footer']/p")
close_button.click()

# Закрыть браузер
driver.quit()
