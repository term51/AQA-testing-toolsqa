import datetime
import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


"""
TODO: 
+ сделать группировку тестов с помощью классов и обернуть всё в allure декораторы
- сделать параметризацию
- сделать задачи в комментах
+- сделать шаги для функций в page
- решить вопрос с запуском функций через Play
- исправить упавшие тесты
- доделать тесты
"""


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


# хук, который срабатывает после каждого теста
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Только если тест упал на этапе выполнения (call)
    if rep.when == 'call' and rep.failed:
        # === ЛОГИ ===
        caplog = item.funcargs.get("caplog", None)
        if caplog and caplog.text:
            allure.attach(
                caplog.text,
                name="Captured Logs",
                attachment_type=allure.attachment_type.TEXT
            )

        # === СКРИНШОТ ===
        driver = item.funcargs.get('driver', None)
        if driver:
            try:
                png = driver.get_screenshot_as_png()
                now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                allure.attach(
                    png,
                    name=f'screenshot_{item.name}_{now}',
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                # Опционально: логируем сбой при снятии скрина (если драйвер умер)
                print(f"[WARN] Failed to capture screenshot: {e}")

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
