import time

from pages.forms.form_page import FormPage


# !! доделать форму
def test_form(driver):
    form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
    form_page.open()
    person = form_page.fill_form_fields()
    result = form_page.form_result()
    print('person', person)
    print('result', result)
    time.sleep(2)
