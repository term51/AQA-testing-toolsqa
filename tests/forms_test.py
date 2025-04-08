
import allure

from pages.forms.form_page import FormPage


@allure.suite('Forms')
class TestForms:
    @allure.feature('Registration Form')
    class TestRegistrationForm:
        @allure.title('Fill form filling')
        def test_form_filling(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person = form_page.fill_form_fields()
            result = form_page.form_result()
            assert person[0] + ' ' + person[1] == result[0], 'Full name isn\'t equal'
            assert person[2] == result[1], 'email isn\'t equal'
            assert person[4] == result[8], 'Address isn\'t equal'
            assert len(result) == 10, 'All field must be filled'
