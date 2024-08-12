from selenium import webdriver

from pages.Main import MainPage
from pages.Filled_form import Fill_form


def test_form():
    browser = webdriver.Chrome()

    main_page = MainPage(browser)
    main_page.open()
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
    main_page.submit()

    form = Fill_form(browser)

    assert "danger" in form.fill_zip_code()
    assert "success" in form.fill_first_name()
    assert "success" in form.fill_last_name()
    assert "success" in form.fill_address()
    assert "success" in form.fill_mail()
    assert "success" in form.fill_phone()
    assert "success" in form.fill_city()
    assert "success" in form.fill_country()
    assert "success" in form.fill_job_position()
    assert "success" in form.fill_company()
    browser.quit()