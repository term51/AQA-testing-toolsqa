from locators.alerts_frame_windows.windows_page_locators import WindowsPageLocators
from pages.base_page import BasePage


class WindowsPage(BasePage):
    locators = WindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.switch_to_new_tab()
        return self.element_is_present(self.locators.SAMPLE_PAGE_TEXT).text

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.switch_to_new_tab()
        return self.element_is_present(self.locators.SAMPLE_PAGE_TEXT).text
