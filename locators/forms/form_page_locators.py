import random

from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input#firstName')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input#lastName')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input#userEmail')
    GENDER_RADIO_BUTTONS = (By.CSS_SELECTOR, f'label[for="gender-radio-{random.randint(1, 3)}"]')
    MOBILE_NUMBER_INPUT = (By.CSS_SELECTOR, 'input#userNumber')
    DATE_OF_BIRTH_INPUT = (By.CSS_SELECTOR, 'input#dateOfBirthInput')
    SUBJECTS_FIELD = (By.CSS_SELECTOR, 'input#subjectsInput')
    HOBBIES_INPUT = (By.CSS_SELECTOR, f'label[for="hobbies-checkbox-{random.randint(1, 3)}"]')
    FILE_INPUT = (By.CSS_SELECTOR, 'input#uploadPicture')
    CURRENT_ADDRESS_AREA = (By.CSS_SELECTOR, 'textarea#currentAddress')

    STATE_SELECT = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')

    CITY_SELECT = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table results
    RESULT_TABLE = (By.XPATH, "//div[@class='table-responsive']//td[2]")

