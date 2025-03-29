from selenium.webdriver.common.by import By


class DynamicPropertiesLocators:
    ENABLE_BUTTON = (By.CSS_SELECTOR, "button#enableAfter")
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button#colorChange")
    VISIBLE_AFTER_BUTTON = (By.CSS_SELECTOR, "button#visibleAfter")
