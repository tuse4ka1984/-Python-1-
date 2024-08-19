from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class Res:
    """Класс для получения результатов с экрана калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """
                Инициализация класса Res.
                Параметры:
                driver (WebDriver): Объект WebDriver для управления браузером.
        """
        self.driver = driver

    def res(self) -> str:
        """
                Получает текст с экрана калькулятора.
                Возвращает:
                str: Текст, отображаемый на экране калькулятора.
        """
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text