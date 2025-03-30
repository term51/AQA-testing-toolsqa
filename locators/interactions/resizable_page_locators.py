from selenium.webdriver.common.by import By


class ResizablePageLocators:
    RESIZABLE_BOX_WITH_RESTRICTION_AREA = (By.CSS_SELECTOR, ".constraint-area")
    RESIZABLE_BOX_WITH_RESTRICTION = (By.CSS_SELECTOR, "#resizableBoxWithRestriction")
    RESIZABLE_BOX_WITH_RESTRICTION_HANDLE = (By.CSS_SELECTOR, "#resizableBoxWithRestriction .react-resizable-handle")

    RESIZABLE_BOX = (By.CSS_SELECTOR, "#resizable")
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, "#resizable .react-resizable-handle")
