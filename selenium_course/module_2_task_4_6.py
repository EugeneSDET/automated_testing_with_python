from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд, каждые 500 мс
    browser.implicitly_wait(5)
    browser.get(link)

    button = browser.find_element(By.ID, "button")
    button.click()
    message = browser.find_element(By.ID, "verify_message")
    
    assert "successful" in message.text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла