from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn")
    ALERT_WITH_CHOSEN_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alertinner ")
    NAME_OF_PRODUCT_IN_CART = (By.CSS_SELECTOR, "#messages strong")
    NAME_OF_PRODUCT_ADDED_TO_CART = (By.CSS_SELECTOR, "#content_inner h1")
    ALERT_TOTAL_PRICE_IN_CART = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in")
    PRICE_OF_PRODUCT_IN_CART = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in strong")
    PRICE_OF_CHOSEN_PRODUCT = (By.CSS_SELECTOR, "#content_inner .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner ")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    NO_GOODS_IN_BASKET = (By.CSS_SELECTOR, "#id_form-0-quantity")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    NO_GOODS_IN_BASKET = (By.CSS_SELECTOR, "#id_form-0-quantity")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")