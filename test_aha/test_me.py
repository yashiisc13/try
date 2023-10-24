from test_pages import HomePage, ProductListPage, ProductPage, CartPage, Windows
from selenium import webdriver
import pytest


class test_Website(object):
    """"test class"""

    def test_set_up(self):
        chrome_options = webdriver.ChromeOptions()

        chrome_options.set_capability("browserName", "chrome")
        chrome_options.set_capability("platformName", "mac")

        self.driver = webdriver.Remote(
            command_executor='http://192.168.1.2:4444',
            options=chrome_options
        )
        self.driver.get('https://www.amazon.in')

    def test_a(self):
        Windows(self.driver)
        HomePage(self.driver).search_product("Books", "War and Peace")
        ProductListPage(self.driver).choose_product('//div//span[contains(@class, "a-size-medium a-color-base a-text-normal")]')
        Windows(self.driver).switch_window()
        ProductPage(self.driver).add_to_cart()
        Windows(self.driver).go_to_original_window()
        HomePage(self.driver).go_to_cart()
        cart_list = CartPage(self.driver).check_cart('//div//span[contains(@class, "a-truncate-cut")]', '//div//span[contains(@class, "a-dropdown-prompt")]')
        assert cart_list[0] == "War And Peace"
        assert cart_list[1] == "1"

    def test_quit_driver(self):
        self.driver.quit()
