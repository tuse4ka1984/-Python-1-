from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class MainPage:
    url: str = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def __init__(self, driver: WebDriver) -> None:
        """
                    Инициализация класса MainPage.
                    Параметры:
                    driver (WebDriver): Объект WebDriver для управления браузером.

        """
        self.driver = driver      

    def open(self) -> None:
        """
                    Открывает главную страницу.
        
        """
        self.driver.get(self.url)

    def first_name(self, first_name: str) -> None:
        """
                    Заполняет поле имени.
                    Параметры:
                    first_name (str): Имя для заполнения поля.

        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(first_name)

    def last_name(self, last_name: str) -> None:
        """
                    Заполняет поле фамилии.
                    Параметры:
                    last_name (str): Фамилия для заполнения поля.

        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)

    def address(self, address: str) -> None:
        """         
                    Заполняет поле адреса.
                    Параметры:
                    address (str): Адрес для заполнения поля.

        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(address)

    def mail(self, mail: str) -> None:
        """ 
                    Заполняет поле электронной почты.
                    Параметры:
                    mail (str): Электронная почта для заполнения поля.

        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(mail)

    def phone(self, phone: str) -> None:
        """
                    Заполняет поле телефона.
                    Параметры:
                    phone (str): Телефон для заполнения поля.

        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)

    def zip_code(self, z_code: str) -> None:
        """
                    Заполняет поле почтового индекса
                    Параметры:
                    z_code (str): Почтовый индекс для заполнения поля.

        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys(z_code)

    def city(self, city: str) -> None:
        """
                    Заполняет поле города.
                    Параметры:
                    city (str): Город для заполнения поля.
            
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)

    def country(self, country: str) -> None:
        """
                    Заполняет поле страны.
                    Параметры:
                    country (str): Страна для заполнения поля.

        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)

    def job_position(self, job: str) -> None:
        """
                    Заполняет поле должности.
                    Параметры:
                    job (str): Должность для заполнения поля.

        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job)

    def company(self, company: str) -> None:
        """         
                    Заполняет поле компании.
                    Параметры:
                    company (str): Компания для заполнения поля.

        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)

    def submit(self) -> None:
        """
                    Нажимает на кнопку 'Submit' для отправки формы.
                    
        """
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()