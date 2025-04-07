import allure

from locators.alerts_frame_windows.modals_page_locators import ModalsPageLocators
from pages.base_page import BasePage


class ModalsPage(BasePage):
    locators = ModalsPageLocators()

    @allure.title('Check modal dialogs')
    def check_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        small_title = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
        small_body = self.element_is_visible(self.locators.SMALL_MODAL_BODY).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()

        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        large_title = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
        large_body = self.element_is_visible(self.locators.LARGE_MODAL_BODY).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        return [small_title, len(small_body)], [large_title, len(large_body)]
