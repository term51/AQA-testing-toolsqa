import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from locators.elements.radio_button_page_locators import RadioButtonPageLocators
from pages.base_page import BasePage


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step('Click on the radio button: {choice}')
    def click_on_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_RADIO,
            'impressive': self.locators.IMPRESSIVE_RADIO,
            'no': self.locators.NO_RADIO
        }
        self.element_is_visible(choices[choice]).click()

    @allure.step('Getting the text of the selection result')
    def get_output_result(self):
        try:
            # ждём видимости элемента, если не появился — TimeoutException
            return self.element_is_present(self.locators.TEXT_SUCCESS).text
        except TimeoutException:
            return None

    @allure.step('Getting the no radio element')
    def get_no_radiobutton(self):
        return self.element_is_visible(self.locators.NO_RADIO).find_element(By.XPATH, "./preceding-sibling::input")
