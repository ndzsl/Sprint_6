from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise Exception(f"Не удалось кликнуть на элемент: {locator}")

    def fill_input(self, locator, value):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(value)
        except TimeoutException:
            raise Exception(f"Не удалось заполнить поле: {locator}")

    def get_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            raise Exception(f"Не удалось получить текст элемента: {locator}")

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except TimeoutException:
            raise Exception(f"Не удалось прокрутить к элементу: {locator}")
