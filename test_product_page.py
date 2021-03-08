import pytest
from pages.product_page import ProductPage
import time

@pytest.mark.parametrize(
    'promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='link with bug')) for i in range(10)]
)
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_alert_with_chosen_product_name()
    product_page.should_be_the_same_name_of_chosen_product()
    product_page.should_be_alert_with_total_price_of_cart()
    product_page.should_be_the_same_price_of_chosen_product()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    time.sleep(1)
    product_page.should_be_disappeared_message()