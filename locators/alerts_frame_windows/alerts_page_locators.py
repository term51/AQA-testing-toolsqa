from selenium.webdriver.common.by import By


class AlertsPageLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR, "button#alertButton")
    ALERT_AFTER_BUTTON = (By.CSS_SELECTOR, "button#timerAlertButton")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "button#confirmButton")
    PROMPT_BUTTON = (By.CSS_SELECTOR, "button#promtButton")

    # result
    CONFIRM_RESULT = (By.ID, "confirmResult")
    PROMPT_RESULT = (By.ID, "promptResult")
