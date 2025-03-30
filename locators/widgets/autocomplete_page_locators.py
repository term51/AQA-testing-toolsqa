from selenium.webdriver.common.by import By


class AutoCompletePageLocators:
    MULTI_CONTAINER = (By.ID, 'autoCompleteMultipleContainer')
    MULTI_INPUT = (By.ID, 'autoCompleteMultipleInput')
    MULTI_VALUES = (By.CSS_SELECTOR, '.auto-complete__multi-value__label')
    MULTI_REMOVE_BUTTONS = (By.CSS_SELECTOR, '.auto-complete__multi-value__remove')

    SINGLE_VALUE = (By.CLASS_NAME, 'auto-complete__single-value')
    SINGLE_INPUT = (By.ID, 'autoCompleteSingleInput')
