from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, 'There are no word "login" in the current url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD__REGISTRATION_FIELD)
        password_field_confirm = self.browser.find_element(*LoginPageLocators.PASSWORD__REGISTRATION_FIELD_CONFRIM)
        registration_submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_field_confirm.send_keys(password)
        registration_submit_button.click()
