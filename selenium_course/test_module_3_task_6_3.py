import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="class")   # class function
def browser():
    print("\nstart browser for test..")
    # browser = webdriver.Chrome()
    browser = webdriver.Firefox()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestStepikPages():
    @pytest.mark.parametrize('link', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
])
    def test_link(self, browser, link):
        answer = math.log(int(time.time()))
        
        browser.get(link)
        browser.implicitly_wait(10)
        textarea = browser.find_element(By.CSS_SELECTOR, "textarea")
        textarea.send_keys(answer)
        button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        button.click()
        final_element = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint')
        final_text = final_element.text

        assert "Correct!" == final_text
        

if __name__ == "__main__":

    pytest.main()

# не забываем оставить пустую строку в конце файла