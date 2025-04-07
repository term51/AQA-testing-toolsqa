import allure
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
        with allure.step(f"Open the page: {self.url}"):
            self.driver.get(self.url)

    @allure.step("Wait for element to be visible: {locator}")
    def element_is_visible(self, locator, timeout=None):
        self.go_to_element(self.element_is_present(locator))
        # with allure.step(f"Wait for element to be visible: {locator}"):
        return wait(self.driver, timeout or self.default_timeout, poll_frequency=self.poll_frequency).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Wait for elements to be visible: {locator}")
    def elements_are_visible(self, locator, timeout=None):
        return wait(self.driver, timeout or self.default_timeout, poll_frequency=self.poll_frequency).until(
            EC.visibility_of_all_elements_located(locator)
        )

    @allure.step("Wait for element to be present in DOM: {locator}")
    def element_is_present(self, locator, timeout=None):
        """
            presence_of_element_located - Ожидание проверки того, что элемент присутствует в DOM страницы.
            Это не обязательно означает, что элемент виден
        """
        return wait(self.driver, timeout or self.default_timeout, poll_frequency=self.poll_frequency).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Wait for elements to be present in DOM: {locator}')
    def elements_are_present(self, locator, timeout=None):
        return wait(self.driver, timeout or self.default_timeout, poll_frequency=self.poll_frequency).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step('Wait for element to become invisible: {locator}')
    def element_is_not_visible(self, locator, timeout=None):
        return wait(self.driver, timeout or self.default_timeout, poll_frequency=self.poll_frequency).until(
            EC.invisibility_of_element(locator)
        )

    @allure.step('Wait for element to be clickable: {locator}')
    def element_is_clickable(self, locator, timeout=None):
        return wait(self.driver, timeout or self.default_timeout, poll_frequency=self.poll_frequency).until(
            EC.element_to_be_clickable(locator)
        )

    def go_to_element(self, element):
        with allure.step(f"Scroll to element: {element.tag_name}.{element.get_attribute("class")}"):
            """ JS scroll to element """
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        with allure.step(f"Double click on element: {element.tag_name}.{element.get_attribute("class")}"):
            ActionChains(self.driver).double_click(element).perform()

    def action_right_click(self, element):
        with allure.step(f"Right click on element: {element.tag_name}.{element.get_attribute("class")}"):
            ActionChains(self.driver).context_click(element).perform()

    @allure.step('Switch to new browser tab')
    def switch_to_new_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

    @allure.step('Get browser alert')
    def get_alert(self):
        return self.driver.switch_to.alert

    def action_drag_and_drop_by_offset(self, element, x, y):
        with allure.step(
                f"Drag and drop element: {element.tag_name}.{element.get_attribute("class")} by offset (x={x}, y={y})'"
        ):
            ActionChains(self.driver).drag_and_drop_by_offset(element, x, y).perform()

    def action_drag_and_drop_to_element(self, source, target):
        with allure.step(
                f"Drag and drop element: {source.tag_name}.{source.get_attribute("class")} "
                f"to target: {target.tag_name}.{target.get_attribute('class')}"
        ):
            ActionChains(self.driver).drag_and_drop(source, target).perform()

    def action_move_to_element(self, element):
        with allure.step(f"Move mouse to element: {element.tag_name}.{element.get_attribute("class")}"):
            ActionChains(self.driver).move_to_element(element).perform()
