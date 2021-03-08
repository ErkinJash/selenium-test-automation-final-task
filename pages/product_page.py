from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button does not exist"

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_alert_with_chosen_product_name(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_WITH_CHOSEN_PRODUCT_NAME), \
            "Alert with chosen product name does not exist"

    def should_be_the_same_name_of_chosen_product(self):
        name_of_product_in_cart = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_CART).text
        name_of_product_added_to_cart = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_ADDED_TO_CART).text
        assert  name_of_product_in_cart == name_of_product_added_to_cart, \
            "Name of the added to cart product differs from the name of product which is in the cart"

    def should_be_alert_with_total_price_of_cart(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_TOTAL_PRICE_IN_CART), \
            "Alert with total price of cart does not exist"

    def should_be_the_same_price_of_chosen_product(self):
        price_of_cart = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT_IN_CART).text
        price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_CHOSEN_PRODUCT).text
        assert price_of_cart == price_of_product, \
            "The price of cart differs from price of product"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The message is not disappeared, but should be"


