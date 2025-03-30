import os
import random


def get_root_folder_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def get_temp_folder_path():
    temp_path = os.path.join(get_root_folder_path(), "temp")
    if not os.path.exists(temp_path):
        os.makedirs(temp_path)
    return temp_path


def get_random_time_with_interval(interval: int = 15):
    """
     Генерирует список временных меток с шагом interval минут от 00:00 до 23:59.
     :param interval: Интервал в минутах между временными метками (по умолчанию 15)
     :return: Список строк в формате "HH:MM"
     """
    times = [f"{hour:02d}:{minute:02d}"
             for hour in range(24)
             for minute in range(0, 60, interval)]
    return random.choice(times)
