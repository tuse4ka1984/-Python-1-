import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calculator():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome()

    # Откройте страницу калькулятора
    driver.implicitly_wait(120)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Ввод значения в поле delay
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")
    
    # Нажимаем на кнопки калькулятора
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидание результата
    wait = WebDriverWait(driver, 60)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='screen']"), "15"))

    # Проверка результата
    assert "15" in driver.find_element(By.XPATH, "//div[@class='screen']").text