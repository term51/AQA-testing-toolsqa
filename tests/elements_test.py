import time

from pages.check_box_page import CheckBoxPage
from pages.radio_button_page import RadioButtonPage
from pages.text_box_page import TextBoxPage
from pages.web_table_page import WebTablePage


# def test_text_box(driver):
#     text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
#     text_box_page.open()
#     full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
#     output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
#     time.sleep(3)
#
#     assert full_name == output_full_name, "The full_name doesn't match"
#     assert email == output_email, "The email doesn't match"
#     assert current_address == output_current_address, "The current_address doesn't match"
#     assert permanent_address == output_permanent_address, "The permanent_address doesn't match"
#
#
# def test_check_box(driver):
#     check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
#     check_box_page.open()
#     check_box_page.open_full_list()
#     check_box_page.click_random_checkbox()
#     input_checkbox = check_box_page.get_checked_checkboxes()
#     output_result = check_box_page.get_output_result()
#     print('input_checkbox', input_checkbox)
#     print('output_result', output_result)
#     time.sleep(4)
#     assert input_checkbox == output_result, "Checkboxes are not equal"
#

# def test_radio_button(driver):
#     radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
#     radio_button_page.open()
#     radio_button_page.click_on_radio_button('yes')
#     output_yes = radio_button_page.get_output_result()
#
#     radio_button_page.click_on_radio_button('impressive')
#     output_impressive = radio_button_page.get_output_result()
#
#     radio_button_page.click_on_radio_button('no')
#     output_no = radio_button_page.get_output_result()
#     no_radiobutton = radio_button_page.get_no_radiobutton()
#     print('no_radiobutton.is_enabled()', no_radiobutton.is_enabled())
#     assert output_yes == 'Yes', 'Yes have not been selected'
#     assert output_impressive == 'Impressive', 'Impressive have not been selected'
#     assert output_no != 'No', 'No shouldn\'t be selected'
#     assert not no_radiobutton.is_enabled(), 'No should be disabled'

def test_web_table(driver):
    web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
    web_table_page.open()
    new_person = web_table_page.add_new_person()
    table_result = web_table_page.check_new_added_person()
    print('new_person', new_person)
    print('table_result', table_result)
    assert new_person in table_result
