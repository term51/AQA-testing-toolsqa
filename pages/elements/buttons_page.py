from locators.elements.buttons_page_locators import ButtonsPageLocators
from pages.base_page import BasePage


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_double_click_button(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
        return self.get_resul_text(self.locators.SUCCESS_DOUBLE_CLICK_TEXT)

    def click_on_right_click_button(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        return self.get_resul_text(self.locators.SUCCESS_RIGHT_CLICK_TEXT)

    def click_on_click_button(self):
        self.element_is_visible(self.locators.CLICK_BUTTON).click()
        return self.get_resul_text(self.locators.SUCCESS_CLICK_TEXT)

    def get_resul_text(self, locator):
        return self.element_is_present(locator).text
