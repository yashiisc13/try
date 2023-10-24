from test_aha.test_pages import HomePage, ProductListPage, ProductPage, CartPage, Windows


class test_Website(object):
    """"test class"""

    def __init__(self, driver):
        self.driver = driver

    def test_set_up(self, website):
        self.driver.get(website)

    def test_(self, category, text, product_link, product, quantity):
        Windows(self.driver)
        HomePage(self.driver).search_product(category, text)
        ProductListPage(self.driver).choose_product(product_link)
        Windows(self.driver).switch_window()
        ProductPage(self.driver).add_to_cart()
        Windows(self.driver).go_to_original_window()
        HomePage(self.driver).go_to_cart()
        cart_list = CartPage(self.driver).check_cart(product, quantity)
        assert cart_list[0] == "War And Peace"
        assert cart_list[1] == "1"

    def test_quit_driver(self):
        self.driver.quit()
