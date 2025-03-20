from pages.elements_page import TextBoxPage, CheckBoxPage
import time


def test_text_box(driver):
    text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
    text_box_page.open()
    full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
    output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
    time.sleep(3)

    assert full_name == output_full_name, "The full_name doesn't match"
    assert email == output_email, "The email doesn't match"
    assert current_address == output_current_address, "The current_address doesn't match"
    assert permanent_address == output_permanent_address, "The permanent_address doesn't match"


def test_check_box(driver):
    check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
    check_box_page.open()
    check_box_page.open_full_list()
    check_box_page.click_random_checkbox()
    input_checkbox = check_box_page.get_checked_checkboxes()
    output_result = check_box_page.get_output_result()
    print('input_checkbox', input_checkbox)
    print('output_result', output_result)
    time.sleep(4)
    assert input_checkbox == output_result, "Checkboxes are not equal"
