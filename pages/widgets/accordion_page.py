from typing import Literal

import allure

from locators.widgets.accordion_page_locators import AccordionPageLocators
from pages.base_page import BasePage


class AccordionPage(BasePage):
    locators = AccordionPageLocators()

    @allure.title('Check accordion {section}')
    def check_accordion(self, section: Literal['first', 'second', 'third']):
        accordion = {
            'first': {'title': self.locators.FIRST_SECTION, 'content': self.locators.FIRST_SECTION_CONTENT},
            'second': {'title': self.locators.SECOND_SECTION, 'content': self.locators.SECOND_SECTION_CONTENT},
            'third': {'title': self.locators.THIRD_SECTION, 'content': self.locators.THIRD_SECTION_CONTENT}
        }

        section_title = self.element_is_visible(accordion[section]['title'])
        is_content_shown = self.element_is_present(accordion[section]['content']).is_displayed()
        if not is_content_shown:
            section_title.click()
        section_content = self.element_is_visible(accordion[section]['content']).text
        return section_title.text, len(section_content)
