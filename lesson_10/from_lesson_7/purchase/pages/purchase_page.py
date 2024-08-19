from selenium.webdriver.common.by import By

class Auth:
    url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        """
                        Инициализация класса Auth.
                        Параметры:
                        driver: Объект WebDriver для управления браузером.

        """
        self.driver = driver

    def open(self) -> None:
        """
                        Открывает страницу авторизации.
                        
        """
        self.driver.get(self.url)

    def authorization(self, login: str, password: str) -> None:
        """
                        Заполняет поля для авторизации.
                        Параметры:
                        login (str): Имя пользователя для входа.
                        password (str): Пароль для входа.

        """
        self.driver.find_element(By.ID, 'user-name').send_keys(login)
        self.driver.find_element(By.ID, 'password').send_keys(password)

    def button(self) -> None:
        """
                        Нажимает кнопку авторизации.
                        
        """
        self.driver.find_element(By.ID, 'login-button').click()


class Cart:

    def __init__(self, driver):
        """
                        Инициализация класса Cart.
                        Параметры:
                        driver: Объект WebDriver для управления браузером.

        """
        self.driver = driver

    def check(self) -> None:
        """
                        Переходит в раздел оформления заказа в корзине.
                        
        """
        self.driver.find_element(By.ID, 'checkout').click()


class Overview:

    def __init__(self, driver):
        """
                        Инициализация класса Overview.
                        Параметры:
                        driver: Объект WebDriver для управления браузером.

        """
        self.driver = driver

    def result(self) -> str:
        """
                        Получает итоговую сумму из общей информации о заказе.
                        Возвращает:
                        str: Текст итоговой суммы.

        """
        return self.driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    

class Prod:

    def __init__(self, driver):
        """
                        Инициализация класса Prod.
                        Параметры:
                        driver: Объект WebDriver для управления браузером.

        """
        self.driver = driver

    def add_to_cart(self) -> None:
        """
                        Добавляет товары в корзину.

        """
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    def cart(self) -> None:
        """
                        Переходит в корзину для просмотра добавленных товаров.
                        
        """
        self.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()


class Info:

    def __init__(self, driver):
        """
                        Инициализация класса Info.
                        Параметры:
                        driver: Объект WebDriver для управления браузером.

        """
        self.driver = driver

    def first_name(self, f_name: str) -> None:
        """
                        Заполняет поле имени.
                        Параметры:
                        f_name (str): Имя для заполнения.
        """
        self.driver.find_element(By.ID, 'first-name').send_keys(f_name)

    def last_name(self, l_name: str) -> None:
        """
                        Заполняет поле фамилии.
                        Параметры:
                        l_name (str): Фамилия для заполнения.

        """
        self.driver.find_element(By.ID, 'last-name').send_keys(l_name)

    def postal_code(self, post_code: str) -> None:
        """
                        Заполняет поле почтового индекса.
                        Параметры:
                        post_code (str): Почтовый индекс для заполнения.

        """
        self.driver.find_element(By.ID, 'postal-code').send_keys(post_code)

    def button_continue(self) -> None:
        """ 
                        Нажимает кнопку продолжения оформления заказа.
                        
        """
        self.driver.find_element(By.ID, 'continue').click()