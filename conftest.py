import datetime
import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


# хук, который срабатывает после каждого теста
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # получаем отчёт
    outcome = yield
    rep = outcome.get_result()

    # интересует только фаза исполнения теста (call), а не setup/teardown
    if rep.when == 'call' and rep.failed:
        # пытаемся достать фикстуру driver
        driver = item.funcargs.get('driver')
        if driver:
            png = driver.get_screenshot_as_png()
            now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            allure.attach(
                png,
                name=f'screenshot_{item.name}_{now}',
                attachment_type=allure.attachment_type.PNG
            )

## Автоматическая генерация метаданных для Allure
# @pytest.fixture(autouse=True)
# def allure_metadata(request):
#     file_path = request.fspath  # Получаем полный путь к файлу теста
#     file_name = os.path.basename(file_path).replace('.py', '')
#     suite_name = file_name.replace('_test', '').replace('_', ' ')
#
#     test_name = request.node.name  # Имя теста, например, "test_text_box"
#     feature = test_name.replace('test_', '').replace('_', ' ').title()
#     title = f"Check {feature}"
#     print('suite', suite_name, 'feature', feature, 'title', title)
#
#     with allure.step(f"Running {title}"):
#         allure.dynamic.suite(suite_name)
#         allure.dynamic.feature(feature)
#         allure.dynamic.title(title)
