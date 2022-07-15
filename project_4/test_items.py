import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_add_to_basket_button(browser: webdriver.Chrome):
    print("start test")
    browser.get(link)
    time.sleep(5)
    browser.implicitly_wait(10)
    try:
        button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        print(f"button text = {button.text}")
    except NoSuchElementException:
        assert False, 'button has not find'
    print("finish test1")
