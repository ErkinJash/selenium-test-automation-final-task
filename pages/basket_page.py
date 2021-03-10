from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):

    def should_not_be_item_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.NO_GOODS_IN_BASKET), \
            "Item in the basket is presented, but should not be"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), \
            "Message about no item in the basket is not presented, but should be"

