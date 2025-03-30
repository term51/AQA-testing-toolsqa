from selenium.webdriver.common.by import By


class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, "button[id='toolTipButton']")
    BUTTON_TEXT = (By.CSS_SELECTOR, "div[id='buttonToolTip'] .tooltip-inner")

    INPUT = (By.CSS_SELECTOR, "input[id='toolTipTextField']")
    INPUT_TEXT = (By.CSS_SELECTOR, "div[id='textFieldToolTip'] .tooltip-inner")

    CONTRARY_LINK = (By.XPATH, "//*[.='Contrary']")
    CONTRARY_LINK_TEXT = (By.CSS_SELECTOR, "div[id='contraryTexToolTip'] .tooltip-inner")

    VERSION_LINK = (By.XPATH, "//*[.='1.10.32']")
    VERSION_LINK_TEXT = (By.CSS_SELECTOR, "div[id='sectionToolTip'] .tooltip-inner")
