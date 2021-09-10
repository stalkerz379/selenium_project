from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import ProductPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def basket_should_not_have_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty, but expected to be empty"

    def go_to_product_page(self):
        product_item = self.browser.find_element(*ProductPageLocators.PRODUCT_ITEM)
        product_item.click()

    def text_basket_page_is_empty(self):
        basket_items_text = self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS_TEXT)
        number_of_basket_items = self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS)
        assert len(basket_items_text) == 1, f'Basket is not empty, in the basket there are {len(number_of_basket_items)}'

    def check_empty_basket_text(self, languages):
        basket_empty_text = self.browser.find_element(*BasketPageLocators.BASKET_ITEMS_TEXT).text
        assert basket_empty_text in languages, f'Empty basket text is not equal to {basket_empty_text}'
