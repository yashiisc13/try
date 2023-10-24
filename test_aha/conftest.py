from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()

    chrome_options.set_capability("browserName", "chrome")
    chrome_options.set_capability("platformName", "mac")

    driver = webdriver.Remote(
        command_executor='http://192.168.1.2:4444',
        options=chrome_options
    )

    return driver


@pytest.fixture
def website():
    website = 'https://www.amazon.in'
    return website


@pytest.fixture
def category():
    category = "Books"
    return category


@pytest.fixture
def text():
    text = "War and Peace"
    return text


@pytest.fixture
def product_link():
    product_link = '//div//span[contains(@class, "a-size-medium a-color-base a-text-normal")]'
    return product_link


@pytest.fixture
def product():
    return '//div//span[contains(@class, "a-truncate-cut")]'


@pytest.fixture
def quantity():
    return '//div//span[contains(@class, "a-dropdown-prompt")]'
