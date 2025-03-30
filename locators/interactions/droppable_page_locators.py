from selenium.webdriver.common.by import By


class DroppablePageLocators:
    # Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-simple')
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, '#draggable')
    SIMPLE_DROP_HERE = (By.CSS_SELECTOR, '.simple-drop-container #droppable')

    # Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-accept')
    ACCEPTABLE = (By.CSS_SELECTOR, '#acceptable')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, '#notAcceptable')
    ACCEPT_DROP_HERE = (By.CSS_SELECTOR, '.accept-drop-container #droppable')

    # Prevent Propogation
    PREVENT_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-preventPropogation')
    PREVENT_DRAG_ME = (By.CSS_SELECTOR, '#dragBox')

    NOT_GREEDY_DROPBOX_TEXT = (By.CSS_SELECTOR, '#notGreedyDropBox > p')
    NOT_GREEDY_DROPBOX_INNER = (By.CSS_SELECTOR, '#notGreedyInnerDropBox')

    GREEDY_DROPBOX_TEXT = (By.CSS_SELECTOR, '#greedyDropBox > p')
    GREEDY_DROPBOX_INNER = (By.CSS_SELECTOR, '#greedyDropBoxInner')

    # Revert Draggable
    REVERT_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-revertable')
    WILL_REVERT = (By.CSS_SELECTOR, '#revertable')
    NOT_REVERT = (By.CSS_SELECTOR, '#notRevertable')
    REVERT_DROP_HERE = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')
