import os

from selenium.webdriver import Keys

from generator.generator import generate_person, generate_file
from locators.forms.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    # ! сделать нормальную проверку всех полей
    def fill_form_fields(self):
        person = next(generate_person())
        file_path = generate_file()

        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER_RADIO_BUTTONS).click()
        self.element_is_visible(self.locators.MOBILE_NUMBER_INPUT).send_keys(person.mobile)
        # сделать список из bundle файла на серваке и брать рандомно предмет
        self.element_is_visible(self.locators.SUBJECTS_FIELD).send_keys('Math')
        self.element_is_visible(self.locators.SUBJECTS_FIELD).send_keys(Keys.RETURN)

        self.element_is_visible(self.locators.HOBBIES_INPUT).click()

        self.element_is_present(self.locators.FILE_INPUT).send_keys(file_path)
        os.remove(file_path)

        self.element_is_visible(self.locators.CURRENT_ADDRESS_AREA).send_keys(person.current_address)

        self.element_is_visible(self.locators.STATE_SELECT).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)

        self.element_is_visible(self.locators.CITY_SELECT).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

        return [person.first_name, person.last_name, person.email, person.mobile, person.current_address]

    def form_result(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        data = [element.text for element in result_list]
        return data
