import allure

from locators.alerts_frame_windows.frames_page_locators import FramesPageLocators
from pages.base_page import BasePage


class FramesPage(BasePage):
    locators = FramesPageLocators()

    # TODO: универсальность добавить
    @allure.title('Check frame {frame_id}')
    def check_frame(self, frame_id: str):
        frame_element = None
        if frame_id == 'frame1':
            frame_element = self.element_is_present(self.locators.IFRAME)

        if frame_id == 'frame2':
            frame_element = self.element_is_present(self.locators.IFRAME_SMALL)

        width = frame_element.get_attribute('width')
        height = frame_element.get_attribute('height')
        self.driver.switch_to.frame(frame_element)
        text = self.element_is_present(self.locators.TITLE_FRAME).text
        self.driver.switch_to.default_content()
        return [text, width, height]
