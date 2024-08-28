from selenium.webdriver.common.by import By
from base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def open(self, url):
        self.driver.get(url)

    def click_on_cookie(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON)

    def scroll_page_to_last_question(self):
        self.scroll_to_element(MainPageLocators.LAST_QUESTION)

    def click_to_question_get_answer(self, question_number):
        self.click_element(MainPageLocators.QUESTION_BUTTONS[question_number])
        return self.get_text(MainPageLocators.ANSWERS[question_number])

    def click_on_order_button(self, button):
        self.click_element(button)

    def click_on_logo_yandex(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def click_on_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def get_current_url(self):
        return self.driver.current_url