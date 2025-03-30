
from typing import Literal

from selenium.webdriver.support.ui import WebDriverWait

from locators.interactions.droppable_page_locators import DroppablePageLocators
from pages.base_page import BasePage


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_me = self.element_is_visible(self.locators.SIMPLE_DRAG_ME)
        drop_here = self.element_is_visible(self.locators.SIMPLE_DROP_HERE)
        self.action_drag_and_drop_to_element(drag_me, drop_here)
        return drop_here.text

    def drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        acceptable = self.element_is_visible(self.locators.ACCEPTABLE)
        not_acceptable = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_here = self.element_is_visible(self.locators.ACCEPT_DROP_HERE)

        self.action_drag_and_drop_to_element(not_acceptable, drop_here)
        drop_text_not_acceptable = drop_here.text

        self.action_drag_and_drop_to_element(acceptable, drop_here)
        drop_text_acceptable = drop_here.text
        return drop_text_not_acceptable, drop_text_acceptable

    def drop_prevent_propagation(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()

        drag_me = self.element_is_visible(self.locators.PREVENT_DRAG_ME)
        not_greedy_dropbox_inner = self.element_is_visible(self.locators.NOT_GREEDY_DROPBOX_INNER)
        greedy_dropbox_inner = self.element_is_visible(self.locators.GREEDY_DROPBOX_INNER)

        self.action_drag_and_drop_to_element(drag_me, not_greedy_dropbox_inner)
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_DROPBOX_TEXT).text
        text_not_greedy_box_inner = not_greedy_dropbox_inner.text

        self.action_drag_and_drop_to_element(drag_me, greedy_dropbox_inner)
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_DROPBOX_TEXT).text
        text_greedy_box_inner = greedy_dropbox_inner.text

        return text_not_greedy_box, text_not_greedy_box_inner, text_greedy_box, text_greedy_box_inner

    def drop_revert_draggable(self, revert_box_name: Literal['will', 'not_will']):
        box_locators = {
            'will': self.locators.WILL_REVERT,
            'not_will': self.locators.NOT_REVERT
        }

        self.element_is_visible(self.locators.REVERT_TAB).click()

        revert_box = self.element_is_visible(box_locators[revert_box_name])
        drop_here = self.element_is_visible(self.locators.REVERT_DROP_HERE)

        self.action_drag_and_drop_to_element(revert_box, drop_here)
        revert_before_position = revert_box.location
        WebDriverWait(self.driver, 5).until(lambda d: "ui-draggable-dragging" not in revert_box.get_attribute("class"))

        revert_after_position = revert_box.location
        return revert_before_position, revert_after_position
