import allure

from pages.widgets.accordion_page import AccordionPage
from pages.widgets.autocomplete_page import AutoCompletePage
from pages.widgets.date_picker_page import DatePickerPage
from pages.widgets.menu_page import MenuPage
from pages.widgets.progress_bar_page import ProgressBarPage
from pages.widgets.select_menu_page import SelectMenuPage
from pages.widgets.slider_page import SliderPage
from pages.widgets.tabs_page import TabsPage
from pages.widgets.tool_tips_page import ToolTipsPage


@allure.suite('Widgets')
class Widgets:
    @allure.feature('Accordion')
    class Accordion:
        @allure.title('Check accordion')
        # сделать параметризацию
        def test_accordion(driver):
            accordion_page = AccordionPage(driver, 'https://demoqa.com/accordian')
            accordion_page.open()
            title, content_len = accordion_page.check_accordion('first')
            assert title == 'What is Lorem Ipsum?', "The title is not correct"
            assert content_len > 0, "The content is empty"

            title, content_len = accordion_page.check_accordion('second')
            assert title == 'Where does it come from?', "The title is not correct"
            assert content_len > 0, "The content is empty"

            title, content_len = accordion_page.check_accordion('third')
            assert title == 'Why do we use it?', "The title is not correct"
            assert content_len > 0, "The content is empty"

    @allure.feature('Autocomplete')
    class Autocomplete:
        @allure.title('Checking selected list items')
        def test_fill_multi_autocomplete(driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result, "Colors are not the same"

        @allure.title('Check for removal from the list')
        def test_remove_value_from_multi_autocomplete(driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_values_before, count_values_after = autocomplete_page.remove_value_from_multi()
            assert count_values_before != count_values_after, "Values are not removed"

        @allure.title('Check for removal all items from the list')
        # !! Доделать тест
        def test_remove_all_values_from_multi_autocomplete(driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')

        @allure.title('Check for selected item')
        def test_fill_single_autocomplete(driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result, "Colors are not the same"

    @allure.feature('DatePicker')
    class DatePicker:
        @allure.title('Check selected date')
        def test_change_date(driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, "The date is not changed"

        @allure.title('Check selected date and time')
        def test_change_date_and_time(driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_datetime_before, value_datetime_after = date_picker_page.select_datetime()
            assert value_datetime_before != value_datetime_after, "The datetime is not changed"

    @allure.feature('Slider')
    class Slider:
        @allure.title('Check slider')
        def test_slider(driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            after, before = slider_page.change_slider_value()
            assert after != before, "The value is not changed"

    @allure.feature('ProgressBar')
    class ProgressBar:
        @allure.title('Check progress bar')
        def test_progress_bar(driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            after, before = progress_bar_page.change_progress_bar_value()
            assert after != before, "The value is not changed"

    @allure.feature('Tabs')
    class Tabs:
        @allure.title('Check tabs')
        def test_tabs(driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()

            what_tab, what_content = tabs_page.check_tabs('what')
            assert what_tab == 'What', "The title is not correct"
            assert what_content > 0, "The content is missing"

            origin_tab, origin_content = tabs_page.check_tabs('origin')
            assert origin_tab == 'Origin', "The title is not correct"
            assert origin_content > 0, "The content is missing"

            use_tab, use_content = tabs_page.check_tabs('use')
            assert use_tab == 'Use', "The title is not correct"
            assert use_content > 0, "The content is missing"

            more_result = tabs_page.check_tabs('more')
            assert more_result is False, "The more tab should be disabled"

    @allure.feature('ToolTips')
    class ToolTips:
        @allure.title('Check tooltips')
        def test_tool_tips(driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            text_button, text_field, text_contrary, text_version = tool_tips_page.check_tool_tips()
            assert text_button == 'You hovered over the Button', "The text is not correct"
            assert text_field == 'You hovered over the text field', "The text is not correct"
            assert text_contrary == 'You hovered over the Contrary', "The text is not correct"
            assert text_version == 'You hovered over the 1.10.32', "The text is not correct"

    @allure.feature('Menu')
    class Menu:
        @allure.title('Check menus')
        def test_menu(driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3'], "The menu is not correct"

    @allure.feature('DropDowns')
    class DropDowns:
        # Сделать самостоятельно
        @allure.title('Check dropdowns')
        def test_select_menu(driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()
