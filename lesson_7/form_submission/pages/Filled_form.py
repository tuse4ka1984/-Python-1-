from selenium.webdriver.common.by import By


class Fill_form:
     
    def __init__(self, driver):
       self.driver = driver

    def fill_first_name(self):
        return self.driver.find_element(By.ID, "first-name").get_attribute("class")

    def fill_last_name(self):
        return self.driver.find_element(By.ID, "last-name").get_attribute("class")
    
    def fill_address(self):
        return self.driver.find_element(By.ID, "address").get_attribute("class")

    def fill_mail(self):
        return self.driver.find_element(By.ID, "e-mail").get_attribute("class")

    def fill_phone(self):
        return self.driver.find_element(By.ID, "phone").get_attribute("class")

    def fill_zip_code(self):
        return self.driver.find_element(By.ID, "zip-code").get_attribute("class")

    def fill_city(self):
        return self.driver.find_element(By.ID, "city").get_attribute("class")

    def fill_country(self):
        return self.driver.find_element(By.ID, "country").get_attribute("class")

    def fill_job_position(self):
        return self.driver.find_element(By.ID, "job-position").get_attribute("class")

    def fill_company(self):
        return self.driver.find_element(By.ID, "company").get_attribute("class")