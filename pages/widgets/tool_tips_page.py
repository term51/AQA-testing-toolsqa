import allure

from locators.widgets.tool_tips_page_locators import ToolTipsPageLocators
from pages.base_page import BasePage


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    @allure.title('Get text from tooltip: {tool_tip_locator}')
    def get_text_from_tool_tip(self, hovered_locator, tool_tip_locator):
        element = self.element_is_visible(hovered_locator)
        self.action_move_to_element(element)
        tool_tip = self.element_is_visible(tool_tip_locator)
        return tool_tip.text

    @allure.title('Check tool tips')
    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tip(
            self.locators.BUTTON,
            self.locators.BUTTON_TEXT
        )
        tool_tip_text_field = self.get_text_from_tool_tip(
            self.locators.INPUT,
            self.locators.INPUT_TEXT
        )
        tool_tip_text_contrary = self.get_text_from_tool_tip(
            self.locators.CONTRARY_LINK,
            self.locators.CONTRARY_LINK_TEXT
        )
        tool_tip_text_version = self.get_text_from_tool_tip(
            self.locators.VERSION_LINK,
            self.locators.VERSION_LINK_TEXT
        )

        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_version
