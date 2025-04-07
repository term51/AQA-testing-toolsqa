import allure

from locators.alerts_frame_windows.nested_frames_locators import NestedFramesPageLocators
from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    @allure.title('Check nested frames')
    def check_nested_frames(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text

        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text
