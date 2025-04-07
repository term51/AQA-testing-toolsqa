import random
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

    @allure.title('Change list order')
    def change_list_order(self):
        self.element_is_present(self.locators.TAB_LIST).click()
        items_locator = self.locators.LIST_ITEMS
        order_before = self.get_sortable_items(items_locator)
        self.shuffle_list(items_locator)
        order_after = self.get_sortable_items(items_locator)
        return order_before, order_after

    @allure.title('Change grid order')
    def change_grid_order(self):
        self.element_is_present(self.locators.TAB_GRID).click()
        items_locator = self.locators.GRID_ITEMS
        order_before = self.get_sortable_items(items_locator)
        self.shuffle_list(items_locator)
        order_after = self.get_sortable_items(items_locator)
        return order_before, order_after
