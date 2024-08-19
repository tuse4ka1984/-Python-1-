from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class FillForm:

    def __init__(self, driver: WebDriver) -> None:
        """
                    Инициализация класса FillForm.
                    Параметры:  
                    driver (WebDriver): Объект WebDriver для управления браузером.

        """
        self.driver = driver

    def fill_first_name(self) -> str:
        """
                    Получает класс элемента поля имени.
                    Возвращает:
                    str: Класс поля имени.

        """
        return self.driver.find_element(By.ID, "first-name").get_attribute("class")

    def fill_last_name(self) -> str:
        """
                    Получает класс элемента поля фамилии.
                    Возвращает:
                    str: Класс поля фамилии.

        """
        return self.driver.find_element(By.ID, "last-name").get_attribute("class")

    def fill_address(self) -> str:
        """
                    Получает класс элемента поля адреса.
                    Возвращает:
                    str: Класс поля адреса.

        """
        return self.driver.find_element(By.ID, "address").get_attribute("class")

    def fill_mail(self) -> str:
        """
                    Получает класс элемента поля электронной почты.
                    Возвращает:
                    str: Класс поля электронной почты.

        """
        return self.driver.find_element(By.ID, "e-mail").get_attribute("class")

    def fill_phone(self) -> str:
        """
                    Получает класс элемента поля телефона.
                    Возвращает:
                    str: Класс поля телефона.

        """
        return self.driver.find_element(By.ID, "phone").get_attribute("class")

    def fill_zip_code(self) -> str:
        """
                    Получает класс элемента поля почтового индекса.
                    Возвращает:
                    str: Класс поля почтового индекса.

        """
        return self.driver.find_element(By.ID, "zip-code").get_attribute("class")

    def fill_city(self) -> str:
        """
                    Получает класс элемента поля города.
                    Возвращает:
                    str: Класс поля города.

        """
        return self.driver.find_element(By.ID, "city").get_attribute("class")

    def fill_country(self) -> str:
        """
                    Получает класс элемента поля страны.
                    Возвращает:
                    str: Класс поля страны.

        """
        return self.driver.find_element(By.ID, "country").get_attribute("class")

    def fill_job_position(self) -> str:
        """
                    Получает класс элемента поля должности.
                    Возвращает:
                    str: Класс поля должности.

        """
        return self.driver.find_element(By.ID, "job-position").get_attribute("class")

    def fill_company(self) -> str:
        """
                    Получает класс элемента поля компании.
                    Возвращает:
                    str: Класс поля компании.

        """
        return self.driver.find_element(By.ID, "company").get_attribute("class")