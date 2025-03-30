from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
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
        self.go_to_element(self.element_is_present(locator))
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

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def switch_to_new_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

    def get_alert(self):
        return self.driver.switch_to.alert

    def action_drag_and_drop_by_offset(self, element, x, y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x, y)
        action.perform()

    def action_drag_and_drop_to_element(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target)
        action.perform()

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
