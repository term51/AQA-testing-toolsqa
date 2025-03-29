from pages.widgets.accordion_page import AccordionPage


def test_accordion(driver):
    accordion_page = AccordionPage(driver, 'https://demoqa.com/accordian')
    accordion_page.open()
    title, content = accordion_page.check_accordion('first')
