from selenium.webdriver.common.by import By


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT = (By.XPATH, "//input[@id='age']")
    SALARY_INPUT = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT = (By.XPATH, "//input[@id='department']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")

    # tables
    FULL_PEOPLE_LIST = (By.XPATH, "//div[@class='rt-tbody']//div[@role='row']")
