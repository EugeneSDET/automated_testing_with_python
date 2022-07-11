import unittest

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By

        link = "http://suninjuly.github.io/registration1.html"
 
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Eugene")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Bliznakov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("Smolensk67@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # проверка успешной регистрации
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_registration2(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By

        link = "http://suninjuly.github.io/registration2.html"
 
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Eugene")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Bliznakov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("Smolensk67@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # проверка успешной регистрации
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()

# не забываем оставить пустую строку в конце файла