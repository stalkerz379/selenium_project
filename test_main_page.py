from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        login_link = browser.find_element_by_css_selector("#login_link")
        login_link.click()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page_valid()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


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


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.basket_should_not_have_items()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_product_page()
    page.go_to_basket()
    page.basket_should_not_have_items()
    page.text_basket_page_is_empty()


@pytest.mark.skip(reason='Not used now, need to be updated')
def test_empty_text(browser):
    languages = {"ar": "?????? ???????????? ??????????",
                 "ca": "La seva cistella est?? buida.",
                 "cs": "V???? ko????k je pr??zdn??.",
                 "da": "Din indk??bskurv er tom.",
                 "de": "Ihr Warenkorb ist leer.",
                 "en": "Your basket is empty.",
                 "el": "???? ???????????? ?????? ?????????? ??????????.",
                 "es": "Tu carrito esta vac??o.",
                 "fi": "Korisi on tyhj??",
                 "fr": "Votre panier est vide.",
                 "it": "Il tuo carrello ?? vuoto.",
                 "ko": "??????????????? ???????????????.",
                 "nl": "Je winkelmand is leeg",
                 "pl": "Tw??j koszyk jest pusty.",
                 "pt": "O carrinho est?? vazio.",
                 "pt-br": "Sua cesta est?? vazia.",
                 "ro": "Cosul tau este gol.",
                 "ru": "???????? ?????????????? ??????????",
                 "sk": "V???? ko????k je pr??zdny",
                 "uk": "?????? ?????????? ????????????.",
                 "zh-cn": "Your basket is empty."}
    link = 'https://selenium1py.pythonanywhere.com/catalogue/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_product_page()
    page.go_to_basket()
    page.check_empty_basket_text(languages)
