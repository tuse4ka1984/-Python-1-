import allure
from selenium import webdriver
from pages.Main import MainPage
from pages.Filled_form import FillForm

@allure.title("Тест формы")
@allure.description("Тестирование заполнения формы и проверки ошибок при отправке.")
@allure.feature("Форма регистрации")
@allure.severity(allure.severity_level.NORMAL)
def test_form():
    with allure.step("Инициализация драйвера Chrome"):
        browser = webdriver.Chrome()

    main_page = MainPage(browser)

    with allure.step("Открытие главной страницы"):
        main_page.open()

    with allure.step("Заполнение формы"):
        main_page.first_name("Иван")
        main_page.last_name("Петров")
        main_page.address("Ленина, 55-3")
        main_page.mail("test@skypro.com")
        main_page.phone("+7985899998787")
        main_page.zip_code("")
        main_page.city("Москва")
        main_page.country("Россия")
        main_page.job_position("QA")
        main_page.company("SkyPro")
    
    with allure.step("Отправка формы"):
        main_page.submit()

    form = FillForm(browser)

    with allure.step("Проверка поля почтового индекса на наличие ошибки"):
        assert "danger" in form.fill_zip_code()

    with allure.step("Проверка успешного заполнения полей формы"):
        assert "success" in form.fill_first_name()
        assert "success" in form.fill_last_name()
        assert "success" in form.fill_address()
        assert "success" in form.fill_mail()
        assert "success" in form.fill_phone()
        assert "success" in form.fill_city()
        assert "success" in form.fill_country()
        assert "success" in form.fill_job_position()
        assert "success" in form.fill_company()

    with allure.step("Закрытие браузера"):
        browser.quit()