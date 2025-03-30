import random
from typing import Literal

from locators.interactions.selectable_page_locators import SelectablePageLocators
from pages.base_page import BasePage


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_item(self, locator):
        item_list = self.elements_are_visible(locator)
        random_items = random.sample(item_list, k=random.randint(1, len(item_list)))
        for item in random_items:
            item.click()

    def select_items(self, tab_name: Literal['list', 'grid']):
        selectable = {
            'list': {
                'tab': self.locators.TAB_LIST,
                'items': self.locators.LIST_ITEMS,
                'active': self.locators.LIST_ITEMS_ACTIVE
            },
            'grid': {
                'tab': self.locators.TAB_GRID,
                'items': self.locators.GRID_ITEMS,
                'active': self.locators.GRID_ITEMS_ACTIVE
            }
        }

        self.element_is_present(selectable[tab_name]['tab']).click()
        self.click_selectable_item(selectable[tab_name]['items'])
        result = []
        for item in self.elements_are_visible(selectable[tab_name]['active']):
            result.append(item.text)

        return result
