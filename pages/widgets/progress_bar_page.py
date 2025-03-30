import random
import time

from locators.widgets.progress_bar_page_locators import ProgressBarPageLocators
from pages.base_page import BasePage


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR).text
        self.element_is_clickable(self.locators.START_STOP_BUTTON).click()
        time.sleep(random.randint(1, 3))
        self.element_is_clickable(self.locators.START_STOP_BUTTON).click()
        value_after = self.element_is_visible(self.locators.PROGRESS_BAR).text
        return value_before, value_after
