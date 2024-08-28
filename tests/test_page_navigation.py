import allure
from data import Urls
from locators.main_page_locators import MainPageLocators

class TestPageNavigation:
    @allure.title('Проверяем редирект на страницу Дзена в новом окне, при клике на лого "Яндекс" в шапке')
    def test_click_on_logo_yandex_redirect_to_dzen(self, main_page):
        main_page.get_url(Urls.MAIN_PAGE_URL)
        main_page.click_on_logo_yandex()
        main_page.search_find_button()
        assert main_page.get_current_url() == Urls.DZEN_URL

    @allure.title('Проверяем возвращение на главную страницу Самоката, при нажатии на лого "Самокат"')
    def test_click_on_scooter_logo_and_open_home_page(self, main_page, order_page):
        main_page.get_url(Urls.MAIN_PAGE_URL)
        main_page.click_on_order_button(MainPageLocators.ORDER_BUTTON_IN_HEADER)
        order_page.set_data_for_whom_scooter()
        order_page.click_next_button()
        order_page.set_data_about_rent('27.08.2024')
        order_page.click_on_order_then_confirm_button()
        assert order_page.check_order_is_done()
        main_page.click_on_scooter_logo()
        assert main_page.get_current_url() == Urls.MAIN_PAGE_URL