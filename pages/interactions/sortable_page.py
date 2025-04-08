import random
from typing import Literal

import allure

from locators.interactions.sortable_page_locators import SortablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    @allure.title('Get list of sortable items {locator}')
    def get_sortable_items(self, locator):
        item_list = self.elements_are_visible(locator)
        return [item.text for item in item_list]

    @allure.title('Shuffle list {locator}')
    def shuffle_list(self, locator):
        two_random_elements = random.sample(self.elements_are_visible(locator), k=2)
        item_from = two_random_elements[0]
        item_to = two_random_elements[1]
        self.action_drag_and_drop_to_element(item_from, item_to)

    @allure.title('Change order of {tab_name}')
    def change_order(self, tab_name: Literal['list', 'grid']):
        tab_locators = {
            'list': {
                'tab': self.locators.TAB_LIST,
                'items': self.locators.LIST_ITEMS,
            },
            'grid': {
                'tab': self.locators.TAB_GRID,
                'items': self.locators.GRID_ITEMS,
            }
        }

        self.element_is_present(tab_locators[tab_name]['tab']).click()
        items_locator = tab_locators[tab_name]['items']
        order_before = self.get_sortable_items(items_locator)
        self.shuffle_list(items_locator)
        order_after = self.get_sortable_items(items_locator)
        return order_before, order_after
