import time
import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from locators.elements.dynamic_properties_locators import DynamicPropertiesLocators
from pages.base_page import BasePage


class DynamicProperties(BasePage):
    locators = DynamicPropertiesLocators()

    @allure.step('Click on enable after button')
    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step('Click on color change button')
    def check_changed_color(self):
        start_time = time.time()
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_before = color_button.value_of_css_property('color')
        WebDriverWait(driver=self.driver, timeout=6).until(
            lambda _: color_button.value_of_css_property('color') != color_before
        )

        end_time = time.time()
        color_after = color_button.value_of_css_property('color')
        time_taken = round(end_time - start_time, 2)
        return color_before, color_after, time_taken

    @allure.step('Click on appear button')
    def check_appear_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON)
        except TimeoutException:
            return False
        return True
