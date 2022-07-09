from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд, каждые 500 мс
    browser.implicitly_wait(5)
    browser.get(link)

    optimal_price = browser.find_element(By.ID, "price")
    # говорим Selenium проверять в течение 12 секунд, когда цена дома уменьшится до $100
    optimal_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1 = browser.find_element(By.ID, "book")
    button1.click()
    
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(y)
    button2 = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button2.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# В модуле expected_conditions есть много других правил, которые позволяют реализовать необходимые ожидания:

# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present

# не забываем оставить пустую строку в конце файла