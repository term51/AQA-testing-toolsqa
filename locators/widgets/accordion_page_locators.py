from selenium.webdriver.common.by import By


class AccordionPageLocators:
    FIRST_SECTION = (By.CSS_SELECTOR, "div#section1Heading")
    FIRST_SECTION_CONTENT_WRAPPER = (By.CSS_SELECTOR, "div#section1Heading ~ .collapse")
    FIRST_SECTION_CONTENT = (By.CSS_SELECTOR, "div#section1Content p")

    SECOND_SECTION = (By.CSS_SELECTOR, "div#section2Heading")
    SECOND_SECTION_CONTENT_WRAPPER = (By.CSS_SELECTOR, "div#section2Heading ~ .collapse")
    SECOND_SECTION_CONTENT = (By.CSS_SELECTOR, "div#section2Content p")

    THIRD_SECTION = (By.CSS_SELECTOR, "div#section3Heading")
    THIRD_SECTION_CONTENT_WRAPPER = (By.CSS_SELECTOR, "div#section3Heading ~ .collapse")
    THIRD_SECTION_CONTENT = (By.CSS_SELECTOR, "div#section3Content p")
