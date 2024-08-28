from selenium.webdriver.common.by import By
from base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from generators import generate_name, generate_surname, generate_address, generate_station, generate_phone, generate_rental_period, generate_color, generate_comment

class OrderPage(BasePage):
    def set_data_for_whom_scooter(self):
        self.fill_input(OrderPageLocators.NAME_FIELD, generate_name())
        self.fill_input(OrderPageLocators.SURNAME_FIELD, generate_surname())
        self.fill_input(OrderPageLocators.ADDRESS_FIELD, generate_address())
        self.fill_input(OrderPageLocators.STATION_FIELD, generate_station())
        self.fill_input(OrderPageLocators.PHONE_FIELD, generate_phone())

    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def set_data_about_rent(self, date):
        self.fill_input(OrderPageLocators.DATE_FIELD, date)
        self.fill_input(OrderPageLocators.RENTAL_PERIOD_FIELD, generate_rental_period())
        self.fill_input(OrderPageLocators.COLOR_FIELD, generate_color())
        self.fill_input(OrderPageLocators.COMMENT_FIELD, generate_comment())

    def click_on_order_then_confirm_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    def check_order_is_done(self):
        return self.is_element_present(OrderPageLocators.ORDER_DONE)