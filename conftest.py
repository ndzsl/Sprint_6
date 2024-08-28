import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Urls

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open(Urls.MAIN_PAGE_URL)
    return page

@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    page.open(Urls.ORDER_PAGE_URL)
    return page