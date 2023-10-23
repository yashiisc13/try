import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

def test_Amazon():
    chrome_options = webdriver.ChromeOptions()

    chrome_options.set_capability("browserName", "chrome")
    chrome_options.set_capability("platformName", "mac")

    driver = webdriver.Remote(
        command_executor = 'http://192.168.1.4:4444',
        options = chrome_options
    )

    driver.get('https://www.amazon.in')

    original_window = driver.current_window_handle

    dropdown_list = driver.find_element(By.ID, "searchDropdownBox")
    category = Select(dropdown_list)
    category.select_by_visible_text('Books')

    driver.find_element(By.ID, "twotabsearchtextbox").send_keys("War And Peace")

    driver.find_element(By.ID, "nav-search-submit-button").click()

    driver.implicitly_wait(5)

    product = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div//span[contains(@class, "a-size-medium a-color-base a-text-normal")]')))
    product.click()

    wait(driver, 10).until(EC.number_of_windows_to_be(2))

    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    driver.find_element(By.ID, "add-to-cart-button").click()

    driver.close()
    driver.switch_to.window(original_window)

    driver.find_element(By.ID, "nav-cart-count").click()

    product_check = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div//span[contains(@class, "a-truncate-cut")]')))
    assert product_check.text == 'War And Peace'

    product_check = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div//span[contains(@class, "a-dropdown-prompt")]')))
    assert product_check.text == '1'

    driver.quit()
