import pytest
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.default_timeout = 5
        self.poll_frequency = 1

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=None):
        """
             visibility_of_element_located - Ожидание проверки того, что элемент присутствует в DOM страницы и виден.
             Видимость означает, что элемент не только отображается, но и имеет высоту и ширину больше 0.
         """
        return wait(self.driver, timeout or self.default_timeout, poll_frequency=self.poll_frequency).until(
            EC.visibility_of_element_located(locator)
        )

    def elements_are_visible(self, locator, timeout=None):
        return wait(self.driver, timeout or self.default_timeout, poll_frequency=self.poll_frequency).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def element_is_present(self, locator, timeout=None):
        """
            presence_of_element_located - Ожидание проверки того, что элемент присутствует в DOM страницы.
            Это не обязательно означает, что элемент виден
        """
        return wait(self.driver, timeout or self.default_timeout, poll_frequency=self.poll_frequency).until(
            EC.presence_of_element_located(locator)
        )

    def elements_are_present(self, locator, timeout=None):
        return wait(self.driver, timeout or self.default_timeout, poll_frequency=self.poll_frequency).until(
            EC.presence_of_all_elements_located(locator)
        )

    def element_is_not_visible(self, locator, timeout=None):
        return wait(self.driver, timeout or self.default_timeout, poll_frequency=self.poll_frequency).until(
            EC.invisibility_of_element(locator)
        )

    def element_is_clickable(self, locator, timeout=None):
        return wait(self.driver, timeout or self.default_timeout, poll_frequency=self.poll_frequency).until(
            EC.element_to_be_clickable(locator)
        )

    def go_to_element(self, element):
        """ JS scroll to element """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
