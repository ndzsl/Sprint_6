from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_FIELD = (By.CSS_SELECTOR, "input[name='name']")
    SURNAME_FIELD = (By.CSS_SELECTOR, "input[name='surname']")
    ADDRESS_FIELD = (By.CSS_SELECTOR, "input[name='address']")
    STATION_FIELD = (By.CSS_SELECTOR, "input[name='station']")
    PHONE_FIELD = (By.CSS_SELECTOR, "input[name='phone']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "button[type='button'][data-action='next']")
    DATE_FIELD = (By.CSS_SELECTOR, "input[name='date']")
    RENTAL_PERIOD_FIELD = (By.CSS_SELECTOR, "select[name='rental_period']")
    COLOR_FIELD = (By.CSS_SELECTOR, "input[name='color']")
    COMMENT_FIELD = (By.CSS_SELECTOR, "textarea[name='comment']")
    ORDER_BUTTON = (By.CSS_SELECTOR, "button[type='submit'][data-action='order']")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[type='button'][data-action='confirm']")
    ORDER_DONE = (By.CSS_SELECTOR, "div[class*='order_done']")