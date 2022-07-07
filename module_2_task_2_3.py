from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#num1')
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, '#num2')
    y = y_element.text

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(int(x)+int(y))) # ищем элемент с суммой

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла