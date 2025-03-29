from selenium.webdriver.common.by import By


class UploadDownloadPageLocators:
    DOWNLOAD_FILE_BUTTON = (By.ID, 'downloadButton')
    UPLOAD_FILE_INPUT = (By.ID, 'uploadFile')

    FILE_UPLOADED_RESULT = (By.ID, 'uploadedFilePath')
