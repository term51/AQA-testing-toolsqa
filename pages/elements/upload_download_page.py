import base64
import os
import random
import allure

from locators.elements.upload_download_page_locators import UploadDownloadPageLocators
from pages.base_page import BasePage
from utils.files import get_temp_folder_path
from utils.logger import setup_logger

logger = setup_logger(__name__)


class UploadDownloadPage(BasePage):
    locators = UploadDownloadPageLocators()

    @allure.step('Upload file {file_path}')
    def upload_file(self, file_path):
        self.element_is_visible(self.locators.UPLOAD_FILE_INPUT).send_keys(file_path)
        return self.element_is_present(self.locators.FILE_UPLOADED_RESULT).text

    @allure.step('Download file')
    def download_file(self):
        path = None
        try:
            with allure.step('Get file link'):
                link = self.element_is_visible(self.locators.DOWNLOAD_FILE_BUTTON).get_attribute('href')

            try:
                base64_str = link.split(",")[1]  # Извлечение base64-строки из ссылки
            except IndexError:
                raise ValueError("Неверный формат ссылки, base64-данные не найдены.")

            with allure.step('Decode base64 to binary data'):
                link_b = base64.b64decode(base64_str)

            with allure.step('Generate path for temporary file'):
                path = os.path.join(get_temp_folder_path(), f'image_file_{random.randint(1, 999)}.jpg')

            with allure.step('Save file'):
                with open(path, 'wb') as file:
                    file.write(link_b)

            with allure.step('Verify file exists'):
                file_exists = os.path.exists(path)

            return file_exists
        except Exception as e:
            logger.error("Error occurred while downloading file", exc_info=True)
            raise e
        finally:
            if path and os.path.exists(path):
                with allure.step('Remove file'):
                    os.remove(path)
