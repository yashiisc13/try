from selenium.webdriver.common.by import By


class HomePageLocators(object):
    """A class for locators on home page"""

    dropdown_list = (By.ID, "searchDropdownBox")
    search_box = (By.ID, "twotabsearchtextbox")
    search_button = (By.ID, "nav-search-submit-button")
    go_to_cart = (By.ID, "nav-cart-count")


class ChooseProductLocator(object):
    """A class for locator for choosing product"""

    def __init__(self, product_chosen):
        self.product_chosen = (By.XPATH, product_chosen)


class ProductPageLocators(object):
    """A class for locators on product page"""

    add_to_cart = (By.ID, "add-to-cart-button")


class CartPageLocators(object):
    """A class for locators on cart page"""

    def __init__(self, product_chosen, quantity):
        self.product_chosen = (By.XPATH, product_chosen)
        self.quantity = (By.XPATH, quantity)
