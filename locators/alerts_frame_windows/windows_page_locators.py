from selenium.webdriver.common.by import By


class WindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button#tabButton")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button#windowButton")

    SAMPLE_PAGE_TEXT = (By.CSS_SELECTOR, "h1#sampleHeading")
