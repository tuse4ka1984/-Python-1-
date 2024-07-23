import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

def test_fill_form():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome() 

    # Открываем указанную страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполняем форму значениями
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")  # Оставляем пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажимаем кнопку Submit
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    # Проверяем, что поле Zip code подсвечено красным
    assert "danger" in driver.find_element(By.ID, 'zip-code').get_attribute("class")

    # Проверяем, что остальные поля подсвечены зеленым
    assert "success" in driver.find_element(By.ID, 'first-name').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'last-name').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'address').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'e-mail').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'phone').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'city').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'country').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'job-position').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'company').get_attribute("class")
   
  # Закрываем браузер
    driver.quit()
