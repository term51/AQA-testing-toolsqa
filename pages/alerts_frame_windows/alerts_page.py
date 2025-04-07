import time
from typing import Literal
import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from locators.alerts_frame_windows.alerts_page_locators import AlertsPageLocators
from pages.base_page import BasePage


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.title('Check alert')
    def check_alert(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.get_alert()
        return alert_window.text

    @allure.title('Check alert after 5 seconds')
    def check_after_alert(self):
        time_start = time.time()
        self.element_is_visible(self.locators.ALERT_AFTER_BUTTON).click()
        wait(self.driver, 6).until(EC.alert_is_present())
        time_end = time.time()
        alert_window = self.get_alert()
        return alert_window.text, int(round(time_end - time_start))

    @allure.title('Check confirm alert by {action}')
    def check_confirm_alert(self, action: Literal["accept", "dismiss"]):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        alert_window = self.get_alert()
        if action == 'dismiss':
            alert_window.dismiss()
        else:
            alert_window.accept()

    @allure.title('Get confirm alert result')
    def get_confirm_alert_result(self):
        return self.element_is_present(self.locators.CONFIRM_RESULT).text

    @allure.title('Check prompt alert via text: {text}')
    def check_prompt_alert(self, text: str):
        self.element_is_visible(self.locators.PROMPT_BUTTON).click()
        alert_window = self.get_alert()
        alert_window.send_keys(text)

    @allure.title('Get prompt alert result')
    def get_prompt_alert_result(self):
        return self.element_is_present(self.locators.PROMPT_RESULT).text
