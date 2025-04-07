from typing import Literal

import allure

from locators.widgets.tabs_page_locators import TabsPageLocators
from pages.base_page import BasePage


class TabsPage(BasePage):
    locators = TabsPageLocators()

    @allure.title('Check tabs {tab_name}')
    def check_tabs(self, tab_name: Literal['what', 'origin', 'use', 'more']):
        tab_locators = {
            'what': {
                'title': self.locators.WHAT_TAB,
                'content': self.locators.WHAT_TAB_CONTENT
            },
            'origin': {
                'title': self.locators.ORIGIN_TAB,
                'content': self.locators.ORIGIN_TAB_CONTENT
            },
            'use': {
                'title': self.locators.USE_TAB,
                'content': self.locators.USE_TAB_CONTENT
            },
            'more': {
                'title': self.locators.MORE_TAB,
                'content': self.locators.MORE_TAB_CONTENT
            }
        }

        tab = self.element_is_visible(tab_locators[tab_name]['title'])
        if tab.get_attribute('aria-disabled') == 'true':
            return False

        tab.click()
        content = self.element_is_visible(tab_locators[tab_name]['content'])

        return tab.text, len(content.text)
