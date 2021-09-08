from .pages.main_page import MainPage
from .pages.login_page import LoginPage


link = 'http://selenium1py.pythonanywhere.com/'


def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_login_url_should_contain_login_word(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_login_form_should_present(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_should_be_login_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
