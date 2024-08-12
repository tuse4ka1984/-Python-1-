from selenium import webdriver

from pages.Calc_page import CalcPage
from pages.Calc_res import Res


def test_calculator():
    browser = webdriver.Chrome()

    calc_page = CalcPage(browser)
    calc_page.open()
    calc_page.delay(45)
    calc_page.sum()
    calc_page.wait(60)

    result = Res(browser)
    result.res()

    assert result.res() == "15"
    browser.quit()