import random
import time

import allure

from locators.widgets.progress_bar_page_locators import ProgressBarPageLocators
from pages.base_page import BasePage


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    @allure.title('Change progress bar value')
    def change_progress_bar_value(self):
        with allure.step('Get text before change progress bar value'):
            value_before = self.element_is_present(self.locators.PROGRESS_BAR).text

        with allure.step('Start progress bar'):
            self.element_is_clickable(self.locators.START_STOP_BUTTON).click()

        wait_sec = random.randint(1, 3)
        with allure.step('Wait progress bar for {wait_sec} seconds'):
            time.sleep(wait_sec)

        with allure.step('Stop progress bar'):
            self.element_is_clickable(self.locators.START_STOP_BUTTON).click()

        value_after = self.element_is_visible(self.locators.PROGRESS_BAR).text
        return value_before, value_after
