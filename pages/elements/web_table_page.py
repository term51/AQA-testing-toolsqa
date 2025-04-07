import random
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from generator.generator import generate_person
from locators.elements.web_table_page_locators import WebTablePageLocators
from pages.base_page import BasePage


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.step('Add auto generated person')
    def add_new_person(self):
        count = random.randint(1, 1)
        person_info = next(generate_person())

        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        while count != 0:
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1

        return [first_name, last_name, str(age), email, str(salary), department]

    @allure.step('Check new added person')
    def check_new_added_person(self):
        people_list = self.elements_are_visible(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            if item.text.strip() != '':
                data.append(item.text.splitlines())
        return data

    @allure.step('Search some person via: {key_word}')
    def search_some_person(self, key_word):
        input_field = self.element_is_visible(self.locators.SEARCH_INPUT)
        input_field.clear()
        ActionChains(self.driver).move_to_element(input_field).click().send_keys(key_word).perform()
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element_value(self.locators.SEARCH_INPUT, key_word)
        )

    @allure.step('Check search person')
    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(*self.locators.ROW_PARENT)
        return row.text.splitlines()

    # TODO: сделать рандомно выбор значения и его изменение
    @allure.step('Update person info')
    def update_person_info(self):
        person_info = next(generate_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    @allure.step('Delete person')
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('Check no rows found')
    def check_no_rows_found(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step('Select up to some rows')
    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        with  allure.step('Prepare data'):
            for x in count:
                with  allure.step('Get count row select'):
                    count_row_select = self.element_is_visible(self.locators.SELECT_COUNT_ROWS)
                self.go_to_element(count_row_select)
                count_row_select.click()
                with  allure.step(f'Select count row {x}'):
                    self.element_is_visible((By.CSS_SELECTOR, f"option[value='{x}']")).click()
                data.append(self.check_count_rows())

        return data

    @allure.step('Check count rows')
    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.TABLE_ROWS)
        return len(list_rows)
