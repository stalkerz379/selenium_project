from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def product_page(self):
        self.add_to_cart_button_press()
        self.should_be_message_added_to_cart()
        self.should_be_message_cart_satisfies_order()
        self.price_should_be_equal_to()

    def add_to_cart_button_press(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart.click()
        self.solve_quiz_and_get_code()

    def get_product_price_and_name(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name, product_price

    def should_be_message_added_to_cart(self):
        product_name, product_price = self.get_product_price_and_name()
        message_block = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_BLOCK).text
        assert product_name == message_block, f'{product_name} not equal to {message_block}'

    def should_be_message_cart_satisfies_order(self):
        message_satisfy_order = self.browser.find_element(*ProductPageLocators.DEFERRED_BENEFIT_ORDER).text
        assert 'Deferred benefit offer' == message_satisfy_order, f'Deferred benefit order not equal to {message_satisfy_order}'

    def price_should_be_equal_to(self):
        product_name, product_price = self.get_product_price_and_name()
        block_with_product_price = self.browser.find_element(*ProductPageLocators.BLOCK_WITH_PRICE).text
        assert product_price == block_with_product_price, f'{product_price} is not equal to {block_with_product_price}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_BLOCK), \
            'Success message is presented, but should be not'

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_BLOCK), \
            "Element has not disappeared, but should disappear"
