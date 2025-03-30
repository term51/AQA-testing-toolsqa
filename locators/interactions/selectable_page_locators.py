from selenium.webdriver.common.by import By


class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, '#demo-tab-list')
    LIST_ITEMS = (By.CSS_SELECTOR, '#demo-tabpane-list .list-group-item')
    LIST_ITEMS_ACTIVE = (By.CSS_SELECTOR, '#demo-tabpane-list .list-group-item.active')

    TAB_GRID = (By.CSS_SELECTOR, '#demo-tab-grid')
    GRID_ITEMS = (By.CSS_SELECTOR, '#demo-tabpane-grid .list-group-item')
    GRID_ITEMS_ACTIVE = (By.CSS_SELECTOR, '#demo-tabpane-grid .list-group-item.active')
