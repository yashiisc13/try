from test_aha.test_elements import Base, Window
from test_aha.test_locators import HomePageLocators, ChooseProductLocator, ProductPageLocators, CartPageLocators


class HomePage(Base):
    """home page"""

    def search_product(self, category, text):
        self.select(HomePageLocators.dropdown_list, category)
        self.input(HomePageLocators.search_box, text)
        self.click(HomePageLocators.search_button)

    def go_to_cart(self):
        self.click(HomePageLocators.go_to_cart)


class ProductListPage(Base):
    """class for choosing a product from various options"""

    def choose_product(self, product_link):
        self.click(ChooseProductLocator(product_link).product_chosen)


class ProductPage(Base):
    """class for adding product to cart"""

    def add_to_cart(self):
        self.click(ProductPageLocators.add_to_cart)


class CartPage(Base):
    """cart page class"""

    def check_cart(self, product, quantity):
        return (self.get_text(CartPageLocators(product, quantity).product_chosen),
                self.get_text(CartPageLocators(product, quantity).quantity))


class Windows(Base):
    """class for managing windows"""

    def __init__(self, driver):
        super().__init__(driver)
        self.original_window = self.driver.current_window_handle

    def switch_window(self):
        Window(self.driver).switch()
        for window_handle in self.driver.window_handles:
            if window_handle != self.original_window:
                self.driver.switch_to.window(window_handle)
                break

    def go_to_original_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.original_window)
