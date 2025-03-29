import os


def get_root_folder_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def get_temp_folder_path():
    temp_path = os.path.join(get_root_folder_path(), "temp")
    if not os.path.exists(temp_path):
        os.makedirs(temp_path)
    return temp_path
