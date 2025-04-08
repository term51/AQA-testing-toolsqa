import os
import random
import allure
from selenium.webdriver import Keys

from generator.generator import generate_person, generate_file, generate_subject
from locators.forms.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    @allure.title('Fill form fields')
    def fill_form_fields(self):
        with allure.step('Generate person data'):
            person = next(generate_person())

        with allure.step('Generate file'):
            file_path = generate_file()

        with allure.step('Fill form fields'):
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person.first_name)

            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person.last_name)

            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person.email)

            self.element_is_visible(self.locators.GENDER_RADIO_BUTTONS).click()

            self.element_is_visible(self.locators.MOBILE_NUMBER_INPUT).send_keys(person.mobile)

            subjects = random.sample(generate_subject(), random.randint(1, 4))
            subjects_field = self.element_is_clickable(self.locators.SUBJECTS_FIELD)
            for subject in subjects:
                subjects_field.send_keys(subject)
                subjects_field.send_keys(Keys.RETURN)

            self.element_is_visible(self.locators.HOBBIES_INPUT).click()

            self.element_is_present(self.locators.FILE_INPUT).send_keys(file_path)

            self.element_is_visible(self.locators.CURRENT_ADDRESS_AREA).send_keys(person.current_address)

            self.element_is_visible(self.locators.STATE_SELECT).click()
            self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)

            self.element_is_visible(self.locators.CITY_SELECT).click()
            self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)

            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

        if file_path and os.path.exists(file_path):
            with allure.step('Remove file'):
                os.remove(file_path)

        return [person.first_name, person.last_name, person.email, person.mobile, person.current_address]

    @allure.title('Get form result')
    def form_result(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        data = [element.text for element in result_list]
        return data
