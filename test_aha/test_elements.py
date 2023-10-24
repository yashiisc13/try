from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class Base(object):
    """base class with element interactions as methods"""

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return Wait(self.driver, 10).until(ec.presence_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def input(self, locator, text):
        self.find_element(locator).send_keys(text)

    def select(self, locator, category):
        Select(self.find_element(locator)).select_by_visible_text(category)

    def get_text(self, locator):
        return self.find_element(locator).text


class Window(object):
    """class for exception condition for switching windows"""

    def __init__(self, driver):
        self.driver = driver

    def switch(self):
        Wait(self.driver, 10).until(ec.number_of_windows_to_be(2))
