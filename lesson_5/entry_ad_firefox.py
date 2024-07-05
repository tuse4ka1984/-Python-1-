from selenium import webdriver

# Инициализация браузера Firefox
driver = webdriver.Firefox()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Найти и закрыть модальное окно
close_button = driver.find_element_by_xpath("//div[@class='modal-footer']/p")
close_button.click()

# Закрыть браузер
driver.quit()