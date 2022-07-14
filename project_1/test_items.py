# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_basket_button_exists(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"), 'basket button not found'

# не забываем оставить пустую строку в конце файла