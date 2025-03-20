import random
import time

from generator.generator import generated_person
from locators.web_table_page_locators import WebTablePageLocators
from pages.base_page import BasePage


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self):
        count = random.randint(1, 1)
        person_info = next(generated_person())

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
        print('people_list', people_list)

        data = []
        for item in people_list:
            if item.text.strip() != '':
                data.append(item.text.splitlines())
        print('data', data)
        return data
        # table = self.element_is_visible(self.locators.TABLE)
        # rows = table.find_elements(*self.locators.ROWS)
        # for row in rows:
        #     columns = row.find_elements(*self.locators.COLUMNS)
        #     full_name = columns[0].text
        #     email_from_table = columns[1].text
