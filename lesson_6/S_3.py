from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# Переход на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ожидание загрузки всех картинок
wait = WebDriverWait(driver, 20)
wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done"))

# Получение значения атрибута src у 3-й картинки
third_image = driver.find_element(By.XPATH, "(//img)[4]")
print(third_image.get_attribute("scr"))

# Закрыть браузер
driver.quit()
