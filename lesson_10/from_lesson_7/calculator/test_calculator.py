import allure
from selenium import webdriver

from calculator.pages.Calc_page import CalcPage
from calculator.pages.Calc_res import Res

@allure.title("Тест калькулятора")
@allure.description("Этот тест проверяет функциональность калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator():
    with allure.step("Инициализация веб-драйвера"):
        browser = webdriver.Chrome()

    calc_page = CalcPage(browser)

    with allure.step("Открытие страницы калькулятора"):
        calc_page.open()

    with allure.step("Установка задержки в калькуляторе"):
        calc_page.delay(45)

    with allure.step("Выполнение операции сложения 7 и 8"):
        calc_page.sum()

    with allure.step("Ожидание результата"):
        calc_page.wait(60)

    result = Res(browser)

    with allure.step("Получение результата с экрана калькулятора"):
        result_value = result.res()

    with allure.step("Проверка, что результат равен 15"):
        assert result_value == "15"

    with allure.step("Закрытие веб-драйвера"):
        browser.quit()