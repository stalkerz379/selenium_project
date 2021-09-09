from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def product_page(self):
        self.add_to_cart_button_press()
        self.solve_quiz_and_get_code()
        self.should_be_message_added_to_cart()
        self.should_be_message_cart_satisfies_order()


    def add_to_cart_button_press(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart.click()

    def should_be_message_added_to_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message_block = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_BLOCK)
        product_name_text = product_name.text       # get the name of the product
        message_block_text = message_block.text     # get the text of the cart block
        print(product_name_text)
        assert product_name_text in message_block_text, f'{product_name} not in {message_block_text}'

    def should_be_message_cart_satisfies_order(self):
        message_satisfy_order = self.browser.find_element(*ProductPageLocators.DEFERRED_BENEFIT_ORDER)
        message_satisfy_order_text = message_satisfy_order.text
        assert 'Deferred benefit offer' in message_satisfy_order_text, f'Deferred benefit order not in {message_satisfy_order_text}'
