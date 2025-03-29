from selenium.webdriver.common.by import By


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_BUTTON = (By.XPATH, "//div[3]/button")

    # Result
    SUCCESS_CLICK_TEXT = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")
    SUCCESS_RIGHT_CLICK_TEXT = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    SUCCESS_DOUBLE_CLICK_TEXT = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
