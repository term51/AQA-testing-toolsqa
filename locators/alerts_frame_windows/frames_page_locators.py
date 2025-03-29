from selenium.webdriver.common.by import By


class FramesPageLocators:
    IFRAME = (By.XPATH, "//iframe[@id='frame1']")
    IFRAME_SMALL = (By.XPATH, "//iframe[@id='frame2']")

    TITLE_FRAME = (By.CSS_SELECTOR, "#sampleHeading")
