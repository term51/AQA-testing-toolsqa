import random
from selenium.webdriver.common.by import By

from generator.generator import generate_person
from locators.elements.web_table_page_locators import WebTablePageLocators
from pages.base_page import BasePage


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

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

    def check_new_added_person(self):
        people_list = self.elements_are_visible(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            if item.text.strip() != '':
                data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(*self.locators.ROW_PARENT)
        return row.text.splitlines()

    # сделать рандомно выбор значения и его изменение
    def update_person_info(self):
        person_info = next(generate_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_no_rows_found(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_select = self.element_is_visible(self.locators.SELECT_COUNT_ROWS)
            self.go_to_element(count_row_select)
            count_row_select.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{x}']")).click()
            data.append(self.check_no_rows_found())

        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.TABLE_ROWS)
        return len(list_rows)
