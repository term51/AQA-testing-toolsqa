from selenium.webdriver.common.by import By


class ProgressBarPageLocators:
    PROGRESS_BAR = (By.XPATH, "//div[@id='progressBar']/div")
    START_STOP_BUTTON = (By.CSS_SELECTOR, "#startStopButton")
