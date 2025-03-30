from selenium.webdriver.common.by import By


class DatePickerPageLocators:
    DATE_INPUT = (By.ID, 'datePickerMonthYearInput')
    DATE_SELECT_MONTH = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    DATE_SELECT_YEAR = (By.XPATH, "//select[@class='react-datepicker__year-select']")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, ".react-datepicker__day")

    DATETIME_INPUT = (By.ID, 'dateAndTimePickerInput')
    DATETIME_SELECT_MONTH = (By.CSS_SELECTOR, ".react-datepicker__month-read-view")
    DATETIME_SELECT_MONTH_LIST = (By.CSS_SELECTOR, ".react-datepicker__month-option")
    DATETIME_SELECT_YEAR = (By.CSS_SELECTOR, ".react-datepicker__year-read-view")
    DATETIME_SELECT_YEAR_LIST = (By.CSS_SELECTOR, ".react-datepicker__year-option")
    DATETIME_SELECT_DAY_LIST = (By.CSS_SELECTOR, ".react-datepicker__day")
    DATETIME_SELECT_TIME_LIST = (By.CSS_SELECTOR, ".react-datepicker__time-list-item")
