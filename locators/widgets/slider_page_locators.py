from selenium.webdriver.common.by import By


class SliderPageLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR, "input[type='range']")
    SLIDER_INPUT_LABEL = (By.CSS_SELECTOR, ".range-slider__tooltip__label")
    SLIDER_VALUE_INPUT = (By.CSS_SELECTOR, "input#sliderValue")
