import random

from selenium.webdriver import Keys

from generator.generator import generate_color
from locators.widgets.autocomplete_page_locators import AutoCompletePageLocators
from pages.base_page import BasePage


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        # Chooses k unique random elements from a population sequence.
        colors = random.sample(generate_color(), random.randint(1, 4))
        input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
        for color in colors:
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_values_before = len(self.elements_are_visible(self.locators.MULTI_VALUES))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_REMOVE_BUTTONS)
        for value in remove_button_list:
            value.click()
            break
        count_values_after = len(self.elements_are_visible(self.locators.MULTI_VALUES))
        return count_values_before, count_values_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUES)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        color = random.choice(generate_color())
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color

    def check_color_in_single(self):
        value = self.element_is_visible(self.locators.SINGLE_VALUE)
        return value.text
