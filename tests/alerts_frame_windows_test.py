import allure
import pytest

from pages.alerts_frame_windows.alerts_page import AlertsPage
from pages.alerts_frame_windows.frames_page import FramesPage
from pages.alerts_frame_windows.modals_page import ModalsPage
from pages.alerts_frame_windows.nested_frames_page import NestedFramesPage
from pages.alerts_frame_windows.windows_page import WindowsPage


@allure.suite('Alerts Frame Windows')
class TestAlertsFrameWindows:
    @allure.feature('Browser windows')
    class TestBrowserWindows:

        @allure.title('Check new tab')
        def test_new_tab(self, driver):
            windows_page = WindowsPage(driver, 'https://demoqa.com/browser-windows')
            windows_page.open()
            new_tab_text = windows_page.check_opened_new_tab()
            assert new_tab_text == "This is a sample page", "The new tab wasn't opened"

        @allure.title('Check new window')
        def test_new_window(self, driver):
            windows_page = WindowsPage(driver, 'https://demoqa.com/browser-windows')
            windows_page.open()
            new_window_text = windows_page.check_opened_new_window()
            assert new_window_text == "This is a sample page", "The new window wasn't opened"

    @allure.feature('Alerts')
    class TestAlerts:
        @allure.title('Check new window')
        def test_appear_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_alert()
            assert alert_text == "You clicked a button", "The alert wasn't opened"

        @allure.title('Check simple alert')
        def test_appear_alert_after_5_seconds(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text, time_taken = alerts_page.check_after_alert()
            assert alert_text == "This alert appeared after 5 seconds", "The alert wasn't opened"
            assert time_taken == 5, "The alert wasn't opened for 5 seconds"

        @allure.title('Check confirm alert')
        def test_confirm_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alerts_page.check_confirm_alert("accept")
            resul_text = alerts_page.get_confirm_alert_result()
            assert resul_text == "You selected Ok", "Ok is not selected"

            alerts_page.check_confirm_alert("dismiss")
            resul_text = alerts_page.get_confirm_alert_result()
            assert resul_text == "You selected Cancel", "Cancel is not selected"

        @allure.title('Check prompt alert')
        def test_prompt_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text = 'some text'
            alerts_page.check_prompt_alert(text)
            resul_text = alerts_page.get_prompt_alert_result()
            assert text in resul_text, "Text not sent"

    @allure.feature('Frames')
    class TestFrames:
        @pytest.mark.parametrize('frame_name, expected_result_frame', [
            ('frame1', ['This is a sample page', '500px', '350px']),
            ('frame2', ['This is a sample page', '100px', '100px'])
        ])
        @allure.title('Check frame {frame_name}')
        def test_frames(self, driver, frame_name, expected_result_frame):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            result_frame = frames_page.check_frame(frame_name)
            assert result_frame == expected_result_frame, f"Frame {frame_name} is not correct"

    @allure.feature('Nested frames')
    class TestNestedFrames:
        @allure.title('Check nested frames')
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frames_page.open()
            parent_text, child_text = nested_frames_page.check_nested_frames()
            assert parent_text == 'Parent frame', "Parent frame does not exist"
            assert child_text == 'Child Iframe', "Child Iframe does not exist"

    @allure.feature('Modals')
    class TestModals:
        @allure.title('Check open modals')
        def test_modals(self, driver):
            modals_page = ModalsPage(driver, 'https://demoqa.com/modal-dialogs')
            modals_page.open()
            small, large = modals_page.check_modal_dialogs()
            assert small[1] < large[1], "Small modal is not smaller than large modal"
            assert small[0] == 'Small Modal', "Small modal title is not correct"
            assert large[0] == 'Large Modal', "Large modal title is not correct"
