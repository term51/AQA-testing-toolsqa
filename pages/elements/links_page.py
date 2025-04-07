import allure
import requests

from locators.elements.links_page_locators import LinksPageLocators
from pages.base_page import BasePage
from utils.logger import setup_logger

logger = setup_logger(__name__)


class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step('Check simple link and switching on the new tab')
    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')

        try:
            with allure.step(f'Request link {link_href}'):
                response = requests.get(link_href, timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logger.error(f"Link check failed: {e}", exc_info=True)
            raise

        with allure.step(f'Click on link {self.locators.SIMPLE_LINK}'):
            simple_link.click()

        with allure.step(f'Switch to new tab'):
            self.switch_to_new_tab()

        return link_href, self.driver.current_url

    @allure.step('Check broken link')
    def check_status_code_of_link(self, url):
        try:
            with allure.step(f'Request link {url}'):
                response = requests.get(url, timeout=5)

            return response.status_code
        except requests.exceptions.RequestException as e:
            logger.error(f"Broken link exception: {e}", exc_info=True)
            return str(e)
