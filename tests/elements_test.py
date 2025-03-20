from pages.elements_page import TextBoxPage
import time


def test_text_box(driver):
    page = TextBoxPage(driver, 'https://demoqa.com/text-box')
    page.open()
    full_name, email, current_address, permanent_address = page.fill_all_fields()
    output_full_name, output_email, output_current_address, output_permanent_address = page.check_filled_form()
    time.sleep(3)

    assert full_name == output_full_name, "The full_name doesn't match"
    assert email == output_email, "The email doesn't match"
    assert current_address == output_current_address, "The current_address doesn't match"

    assert permanent_address == output_permanent_address, "The permanent_address doesn't match"
