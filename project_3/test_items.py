import time

from selenium.webdriver.common.by import By


def button_is_present(browser):
    try:
        browser.implicitly_wait(10)
        browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
        time.sleep(5)
        return True
    except:
        return False


def test_cart_button_exist(browser):
    assert button_is_present(browser) == True, "Button is not found"

