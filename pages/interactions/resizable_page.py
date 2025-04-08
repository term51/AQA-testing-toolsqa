import allure

from locators.interactions.resizable_page_locators import ResizablePageLocators
from pages.base_page import BasePage


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    @allure.title('Change size of element: {handle_locator}')
    def change_size(self, handle_locator, x, y):
        element = self.element_is_present(handle_locator)
        self.action_drag_and_drop_by_offset(
            element,
            x,
            y
        )

    @allure.title('Change box size with restriction')
    def change_box_size_with_restriction(self, x, y):
        self.change_size(
            self.locators.RESIZABLE_BOX_WITH_RESTRICTION_HANDLE,
            x,
            y,
        )
        size = self.element_is_present(self.locators.RESIZABLE_BOX_WITH_RESTRICTION).size
        return size

    @allure.title('Change box size without restriction')
    def change_box_size_without_restriction(self, x, y):
        self.go_to_element(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE))
        self.change_size(
            self.locators.RESIZABLE_BOX_HANDLE,
            x,
            y
        )
        size = self.element_is_present(self.locators.RESIZABLE_BOX).size
        return size
