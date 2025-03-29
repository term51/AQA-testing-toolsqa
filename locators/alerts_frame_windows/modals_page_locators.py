from selenium.webdriver.common.by import By


class ModalsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "#showSmallModal")
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "#closeSmallModal")
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-sm']")
    SMALL_MODAL_BODY = (By.CSS_SELECTOR, "div[class='modal-body']")

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "#showLargeModal")
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "#closeLargeModal")
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")
    LARGE_MODAL_BODY = (By.CSS_SELECTOR, "div[class='modal-body'] p")
