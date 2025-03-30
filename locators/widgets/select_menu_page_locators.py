from selenium.webdriver.common.by import By


class SelectMenuPageLocators:
    SELECT_VALUE_DROPDOWN = (By.ID, 'withOptGroup')

    SELECT_ONE_DROPDOWN = (By.ID, 'selectOne')

    OLD_STYLE_SELECT = (By.ID, 'oldSelectMenu')

    MULTI_SELECT_DROPDOWN = (By.CSS_SELECTOR, '.css-2b097c-container:not([id])')

    STANDARD_MULTI_SELECT = (By.ID, 'cars')
