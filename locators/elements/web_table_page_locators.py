from selenium.webdriver.common.by import By


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT = (By.XPATH, "//input[@id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    # tables
    FULL_PEOPLE_LIST = (By.XPATH, "//div[@class='rt-tbody']//div[@role='row']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = (By.XPATH, ".//ancestor::div[@role='row']")
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    TABLE_ROWS = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SELECT_COUNT_ROWS = (By.CSS_SELECTOR, "select[aria-label='rows per page']")

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
