from selenium.webdriver.common.by import By


class DraggablePageLocators:
    # Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, '#draggableExample-tab-simple')
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, '#dragBox')

    # Axis Restricted
    AXIS_RESTRICTED_TAB = (By.CSS_SELECTOR, '#draggableExample-tab-axisRestriction')
    AXIS_ONLY_X = (By.CSS_SELECTOR, '#restrictedX')
    AXIS_ONLY_Y = (By.CSS_SELECTOR, '#restrictedY')

    # Container Restricted
    CONTAINER_RESTRICTED_TAB = (By.CSS_SELECTOR, '#draggableExample-tab-containerRestriction')
    CONTAINMENT_WRAPPER_BIG = (By.CSS_SELECTOR, '#containmentWrapper')
    CONTAINMENT_WRAPPER_BIG_TEXT = (By.CSS_SELECTOR, '#containmentWrapper > div')
    CONTAINMENT_WRAPPER_SMALL = (By.CSS_SELECTOR, '#draggableExample-tabpane-containerRestriction .m-3')
    CONTAINMENT_WRAPPER_SMALL_TEXT = (By.CSS_SELECTOR, '#draggableExample-tabpane-containerRestriction .m-3 span')
