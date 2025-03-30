import random

from locators.interactions.draggable_page_locators import DraggablePageLocators
from pages.base_page import BasePage


class DraggablePage(BasePage):
    locators = DraggablePageLocators()

    def move_element_to_random_position(self, locator):
        self.action_drag_and_drop_by_offset(locator, random.randint(1, 100), random.randint(1, 100))

    def simple_drag_box(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_me = self.element_is_visible(self.locators.SIMPLE_DRAG_ME)
        before_position = drag_me.location
        self.move_element_to_random_position(drag_me)
        after_position = drag_me.location
        return before_position, after_position

    def axis_restricted_draggable(self):
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()
        only_x = self.element_is_visible(self.locators.AXIS_ONLY_X)
        only_y = self.element_is_visible(self.locators.AXIS_ONLY_Y)
        before_only_x_position = only_x.location
        before_only_y_position = only_y.location

        self.move_element_to_random_position(only_x)
        self.move_element_to_random_position(only_y)

        after_only_x_position = only_x.location
        after_only_y_position = only_y.location

        return before_only_x_position, before_only_y_position, after_only_x_position, after_only_y_position
