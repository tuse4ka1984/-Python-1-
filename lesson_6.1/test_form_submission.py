import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Инициализация веб-драйвера
driver = webdriver.Chrome()

# Откройте указанную страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Заполняем форму значениями
driver.find_element(By.NAME, "first_name").send_keys("Иван")
driver.find_element(By.NAME, "last_name").send_keys("Петров")
driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
driver.find_element(By.NAME, "phone_number").send_keys("+7985899998787")
driver.find_element(By.NAME, "zip_code").send_keys("")  # Оставляем пустым
driver.find_element(By.NAME, "city").send_keys("Москва")
driver.find_element(By.NAME, "country").send_keys("Россия")
driver.find_element(By.NAME, "job_position").send_keys("QA")
driver.find_element(By.NAME, "company").send_keys("SkyPro")

# Нажимаем кнопку Submit
driver.find_element(By.XPATH, "//input[@value='Submit']").click()

# Ждем, пока форма обработается и поля подсветятся
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, "first_name")))

# Проверяем, что поле Zip code подсвечено красным
zip_code_field = driver.find_element(By.NAME, "zip_code")
zip_code_bg_color = zip_code_field.value_of_css_property("background-color")
assert zip_code_bg_color == "rgba(255, 0, 0, 1)", f"Expected Zip code background color to be red, but got {zip_code_bg_color}"

# Проверяем, что остальные поля подсвечены зеленым
fields_to_check = ["first_name", "last_name", "address", "email", "phone_number", "city", "country", "job_position", "company"]
for field_name in fields_to_check:
    field = driver.find_element(By.NAME, field_name)
    bg_color = field.value_of_css_property("background-color")
    assert bg_color == "rgba(0, 255, 0, 1)", f"Expected {field_name} background color to be green, but got {bg_color}"

# Закрываем браузер
driver.quit()
        
if __name__ == "__main__":
    pytest.main()