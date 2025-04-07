import allure

from locators.widgets.menu_page_locators import MenuPageLocators
from pages.base_page import BasePage


class MenuPage(BasePage):
    locators = MenuPageLocators()

    @allure.title('Check menu')
    def check_menu(self):
        menu_items = self.elements_are_present(self.locators.MENU_LINKS)
        data = []
        for item in menu_items:
            self.action_move_to_element(item)
            data.append(item.text)

        return data
