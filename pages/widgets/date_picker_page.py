import allure
from selenium.webdriver.support.select import Select

from generator.generator import generate_date
from locators.widgets.data_picker_page_locators import DatePickerPageLocators
from pages.base_page import BasePage


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    @allure.title('Select date')
    def select_date(self):
        date = next(generate_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()

        self._set_date_by_test(self.locators.DATE_SELECT_MONTH, date.month)
        self._set_date_by_test(self.locators.DATE_SELECT_YEAR, date.year)
        self._set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)

        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.title('Set date for: {locator} via value: {value}')
    def _set_date_by_test(self, locator, value):
        select = Select(self.element_is_present(locator))
        select.select_by_visible_text(value)

    @allure.title('Set date: {value} from items: {locator}')
    def _set_date_item_from_list(self, locator, value):
        item_list = self.elements_are_present(locator)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    @allure.title('Select datetime')
    def select_datetime(self):
        date = next(generate_date())
        input_datetime = self.element_is_visible(self.locators.DATETIME_INPUT)
        value_datetime_before = input_datetime.get_attribute('value')
        input_datetime.click()

        self.element_is_visible(self.locators.DATETIME_SELECT_MONTH).click()
        self._set_date_item_from_list(self.locators.DATETIME_SELECT_MONTH_LIST, date.month)

        self.element_is_visible(self.locators.DATETIME_SELECT_YEAR).click()
        self._set_date_item_from_list(self.locators.DATETIME_SELECT_YEAR_LIST, '2020')

        self._set_date_item_from_list(self.locators.DATETIME_SELECT_DAY_LIST, date.day)

        self._set_date_item_from_list(self.locators.DATETIME_SELECT_TIME_LIST, date.time)
        # берем элемент еще раз, т.к. старый input_date не обновляется
        input_datetime = self.element_is_visible(self.locators.DATETIME_INPUT)
        value_datetime_after = input_datetime.get_attribute('value')
        return value_datetime_before, value_datetime_after
