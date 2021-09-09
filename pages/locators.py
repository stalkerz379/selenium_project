from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    SUCCESS_MESSAGE_BLOCK = (By.CSS_SELECTOR, '.alert.alert-success:nth-child(1)')
    DEFERRED_BENEFIT_ORDER = (By.CSS_SELECTOR, '.alert.alert-success:nth-child(2)')
