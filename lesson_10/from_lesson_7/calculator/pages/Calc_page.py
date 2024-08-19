from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class CalcPage:
    """
                    Класс для автоматизации взаимодействия с веб-страницей калькулятора.
                    Атрибуты:
                    url (str): URL страницы калькулятора.
    """

    url: str = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver: WebDriver) -> None:
        """
                    Инициализация класса CalcPage.
                    Параметры:
                    driver (WebDriver): Объект WebDriver для управления браузером.
        """
        self.driver = driver

    def open(self) -> None:
        """
                    Открывает страницу калькулятора в браузере.
        """
        self.driver.get(self.url)

    def delay(self, time: str) -> None:
        """
                    Устанавливает задержку для калькулятора.
                    Параметры:
                    time (str): Задержка, которую необходимо установить.
                        Должна быть представлена в виде строки, поскольку
                        поле ввода принимает текст.
        """
        self.driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self.driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(time)

    def sum(self) -> None:
        """
                    Выполняет операцию сложения 7 и 8 в калькуляторе и нажимает кнопку "=".
        """
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    def wait(self, time: int) -> None:
        """
                    Ожидает, пока результат "15" появится на экране калькулятора.
                    Параметры:
                        time (int): Максимальное время ожидания в секундах.
        """
        waiter = WebDriverWait(self.driver, time)
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )