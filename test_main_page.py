link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_existence_of_online_shoping_cart (browser):
    browser.implicitly_wait(5)
    browser.get(link)
    assert browser.find_element_by_css_selector(
        "#add_to_basket_form .btn"
    ), "Кнопка добавления товара в корзину не нацдена"