import os
import random

from generator.generator import generate_file
from pages.elements.buttons_page import ButtonsPage
from pages.elements.check_box_page import CheckBoxPage
from pages.elements.dynamic_properties_page import DynamicProperties
from pages.elements.links_page import LinksPage
from pages.elements.radio_button_page import RadioButtonPage
from pages.elements.text_box_page import TextBoxPage
from pages.elements.upload_download_page import UploadDownloadPage
from pages.elements.web_table_page import WebTablePage


def test_text_box(driver):
    text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
    text_box_page.open()
    full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
    output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()

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
    assert input_checkbox == output_result, "Checkboxes are not equal"


def test_radio_button(driver):
    radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
    radio_button_page.open()
    radio_button_page.click_on_radio_button('yes')
    output_yes = radio_button_page.get_output_result()

    radio_button_page.click_on_radio_button('impressive')
    output_impressive = radio_button_page.get_output_result()

    radio_button_page.click_on_radio_button('no')
    output_no = radio_button_page.get_output_result()
    no_radiobutton = radio_button_page.get_no_radiobutton()
    assert output_yes == 'Yes', 'Yes have not been selected'
    assert output_impressive == 'Impressive', 'Impressive have not been selected'
    assert output_no != 'No', 'No shouldn\'t be selected'
    assert not no_radiobutton.is_enabled(), 'No should be disabled'


def test_web_table(driver):
    web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
    web_table_page.open()
    new_person = web_table_page.add_new_person()
    table_result = web_table_page.check_new_added_person()
    assert new_person in table_result


def test_web_table_search_person(driver):
    web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
    web_table_page.open()
    key_word = web_table_page.add_new_person()[random.randint(0, 5)]
    web_table_page.search_some_person(key_word)
    table_result = web_table_page.check_search_person()
    assert key_word in table_result, "The person wasn't found in the table"


def test_web_table_update_person_info(driver):
    web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
    web_table_page.open()
    lastname = web_table_page.add_new_person()[1]
    web_table_page.search_some_person(lastname)
    age = web_table_page.update_person_info()
    row = web_table_page.check_search_person()
    assert age in row, "the person card has not been changed"


def test_web_table_delete_person_info(driver):
    web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
    web_table_page.open()
    email = web_table_page.add_new_person()[3]
    web_table_page.search_some_person(email)
    web_table_page.delete_person()
    text = web_table_page.check_no_rows_found()
    assert text == 'No rows found', 'The person has not been deleted'


def test_web_table_change_count_row(driver):
    web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
    web_table_page.open()
    count = web_table_page.select_up_to_some_rows()
    assert count == [5, 10, 20, 25, 50, 100], \
        "The numbers of rows in the table has not been changed or has changed incorrectly"


def test_different_click_on_the_button(driver):
    buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
    buttons_page.open()
    double = buttons_page.click_on_double_click_button()
    right = buttons_page.click_on_right_click_button()
    click = buttons_page.click_on_click_button()

    assert double == 'You have done a double click', "The double click button was not pressed"
    assert right == 'You have done a right click', "The right click button was not pressed"
    assert click == 'You have done a dynamic click', "The dynamic click button was not pressed"


# сделать остальные линки и подумать над логикой текущих(через try except и тд)
def test_link(driver):
    links_page = LinksPage(driver, 'https://demoqa.com/links')
    links_page.open()
    href_link, current_url = links_page.check_new_tab_simple_link()
    assert href_link == current_url, "The link is broken or ulr in incorrect"


def test_broken_link(driver):
    links_page = LinksPage(driver, 'https://demoqa.com/links')
    links_page.open()
    response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
    assert response_code == 400, "The link ....."


def test_upload_file(driver):
    upload_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
    upload_page.open()
    file_path = generate_file()
    result = upload_page.upload_file(file_path)
    os.remove(path=file_path)
    assert os.path.basename(result) == os.path.basename(file_path), "File wasn't uploaded"


def test_download_file(driver):
    download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
    download_page.open()
    is_file_exists = download_page.download_file()
    assert is_file_exists, "File wasn't downloaded"


def test_enable_button(driver):
    dynamic_properties_page = DynamicProperties(driver, 'https://demoqa.com/dynamic-properties')
    dynamic_properties_page.open()
    is_clickable = dynamic_properties_page.check_enable_button()
    assert is_clickable is True, "The button is not clickable"


def test_changed_color_button(driver):
    dynamic_properties_page = DynamicProperties(driver, 'https://demoqa.com/dynamic-properties')
    dynamic_properties_page.open()
    color_before, color_after, time_taken = dynamic_properties_page.check_changed_color()
    assert color_after != color_before, "The color isn't changed"
    assert time_taken <= 5, "Must take 5 seconds"


def test_appear_button(driver):
    dynamic_properties_page = DynamicProperties(driver, 'https://demoqa.com/dynamic-properties')
    dynamic_properties_page.open()
    appear = dynamic_properties_page.check_appear_button()
    assert appear is True
