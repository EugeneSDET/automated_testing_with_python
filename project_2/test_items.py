from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary"), "нет кнопки добавления товара в корзину" 

