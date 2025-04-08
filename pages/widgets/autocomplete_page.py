import random
import time

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generate_color
from locators.widgets.autocomplete_page_locators import AutoCompletePageLocators
from pages.base_page import BasePage


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    @allure.title('Fill multi input ')
    def fill_input_multi(self):
        colors = random.sample(generate_color(), random.randint(3, 5))
        input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
        for color in colors:
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    @allure.title('Remove value from multi input')
    def remove_value_from_multi(self):
        count_values_before = len(self.elements_are_visible(self.locators.MULTI_VALUES))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_REMOVE_BUTTONS)
        for value in remove_button_list:
            value.click()
            break
        count_values_after = len(self.elements_are_visible(self.locators.MULTI_VALUES))
        return count_values_before, count_values_after

    @allure.title('Remove all values from multi input')
    def remove_all_values_from_multi(self):
        remove_all_button = self.element_is_visible(self.locators.MULTI_REMOVE_ALL_BUTTONS)
        remove_all_button.click()
        try:
            count_values = len(self.elements_are_visible(self.locators.MULTI_VALUES))
            return count_values
        except TimeoutException:
            return 0

    @allure.title('Check color in multi input')
    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUES)
        colors = []
        for color in color_list:
            time.sleep(1)
            colors.append(color.text)
        return colors

    @allure.title('Fill single input')
    def fill_input_single(self):
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        color = random.choice(generate_color())
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color

    @allure.title('Check color in single input')
    def check_color_in_single(self):
        value = self.element_is_visible(self.locators.SINGLE_VALUE)
        return value.text
