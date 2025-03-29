import base64
import os
import random

from locators.elements.upload_download_page_locators import UploadDownloadPageLocators
from pages.base_page import BasePage
from utils.files import get_temp_folder_path


class UploadDownloadPage(BasePage):
    locators = UploadDownloadPageLocators()

    def upload_file(self, file_path):
        self.element_is_visible(self.locators.UPLOAD_FILE_INPUT).send_keys(file_path)
        return self.element_is_present(self.locators.FILE_UPLOADED_RESULT).text

    def download_file(self):
        link = self.element_is_visible(self.locators.DOWNLOAD_FILE_BUTTON).get_attribute('href')
        # обрезка ненужной информации о файле
        base64_str = link.split(",")[1]
        # декодирование из base64 в байты, затем сохранение в файл
        link_b = base64.b64decode(base64_str)
        path = os.path.join(get_temp_folder_path(), f'image_file_{random.randint(1, 999)}.jpg')
        with open(path, 'wb') as file:
            file.write(link_b)
            check_file = os.path.exists(path)
        os.remove(path)
        return check_file
