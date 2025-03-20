from selenium.webdriver.common.by import By

from locators.radio_button_page_locators import RadioButtonPageLocators
from pages.base_page import BasePage


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_RADIO,
            'impressive': self.locators.IMPRESSIVE_RADIO,
            'no': self.locators.NO_RADIO
        }
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.TEXT_SUCCESS).text

    def get_no_radiobutton(self):
        return self.element_is_visible(self.locators.NO_RADIO).find_element(By.XPATH, "./preceding-sibling::input")
