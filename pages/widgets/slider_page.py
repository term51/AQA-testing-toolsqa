import random

from locators.widgets.slider_page_locators import SliderPageLocators
from pages.base_page import BasePage


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE_INPUT).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)

        value_after = self.element_is_visible(self.locators.SLIDER_VALUE_INPUT).get_attribute('value')
        return value_before, value_after
