from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_BUTTON = (By.CSS_SELECTOR, "button[class*='cookie']")
    LAST_QUESTION = (By.CSS_SELECTOR, "section[class*='questions']")
    QUESTION_BUTTONS = [ (By.CSS_SELECTOR, f"button[data-question='{i}']") for i in range(8) ]
    ANSWERS = [ (By.CSS_SELECTOR, f"div[data-answer='{i}']") for i in range(8) ]
    ORDER_BUTTON_IN_HEADER = (By.CSS_SELECTOR, "button[class*='order_header']")
    ORDER_BUTTON_IN_FOOTER = (By.CSS_SELECTOR, "button[class*='order_footer']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "a[href*='yandex.ru']")
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a[href='/']")

