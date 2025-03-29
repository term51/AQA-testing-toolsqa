from selenium.webdriver.common.by import By


class RadioButtonPageLocators:
    YES_RADIO = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    IMPRESSIVE_RADIO = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    NO_RADIO = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    TEXT_SUCCESS = (By.CLASS_NAME, "text-success")
