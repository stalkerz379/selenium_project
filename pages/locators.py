from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_ITEMS_TEXT = (By.CSS_SELECTOR, '#content_inner p')


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_REGISTRATION_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD__REGISTRATION_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD__REGISTRATION_FIELD_CONFRIM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary[value='Register']")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    SUCCESS_MESSAGE_BLOCK = (By.CSS_SELECTOR, '.alert.alert-success:nth-child(1) strong')
    DEFERRED_BENEFIT_ORDER = (By.CSS_SELECTOR, '.alert.alert-success:nth-child(2) strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main p[class="price_color"]')
    BLOCK_WITH_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_ITEM = (By.CSS_SELECTOR, 'li:nth-child(1) .product_pod .image_container')
