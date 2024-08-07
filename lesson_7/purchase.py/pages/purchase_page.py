from selenium.webdriver.common.by import By


class Auth:
    url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def authorization(self, login, password):
        self.driver.find_element(By.ID, 'user-name').send_keys(login)
        self.driver.find_element(By.ID, 'password').send_keys(password)

    def button(self):
        self.driver.find_element(By.ID, 'login-button').click()


class Cart:

    def __init__(self, driver):
        self.driver = driver

    def check(self):
        self.driver.find_element(By.ID, 'checkout').click()


class Overview:

    def __init__(self, driver):
        self.driver = driver

    def result(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    

class Prod:

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    def cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()


class Info:

    def __init__(self, driver):
        self.driver = driver

    def first_name(self, f_name):
        self.driver.find_element(By.ID, 'first-name').send_keys(f_name)

    def last_name(self, l_name):
        self.driver.find_element(By.ID, 'last-name').send_keys(l_name)

    def postal_code(self, post_code):
        self.driver.find_element(By.ID, 'postal-code').send_keys(post_code)

    def button_continue(self):
        self.driver.find_element(By.ID, 'continue').click()