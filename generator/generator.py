import os
import random

from data.data import Person, Date

from faker import Faker

from utils.files import get_temp_folder_path, get_random_time_with_interval

faker_ru = Faker('ru_RU')
faker_en = Faker('en_US')

"""
    Faker.seed() фиксирует случайность для повторяемости данных. 
    Если передать одно и то же значение в seed(), генератор будет выдавать одни и те же результаты при каждом запуске.
"""
Faker.seed()


def generate_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=faker_ru.random_int(min=1, max=99),
        salary=faker_ru.random_int(min=1000, max=10000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )


def generate_file():
    path = os.path.join(get_temp_folder_path(), f'generated_file_{random.randint(1, 999)}.txt')
    file = open(path, 'w+', encoding='utf-8')
    file.write(f'Hello {faker_ru.first_name()}')
    file.close()
    return path


def generate_color():
    colors = [
        "Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Indigo", "Magenta", "Aqua"
    ]
    return colors


def generate_date():
    yield Date(
        year=faker_en.year(),
        day=faker_en.day_of_month(),
        month=faker_en.month_name(),
        time=get_random_time_with_interval(),
    )


def generate_subject():
    subjects = [
        'Hindi', 'English', 'Maths', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Commerce', 'Accounting',
        'Economics', 'Arts', 'Social Studies', 'History', 'Civics'
    ]
    return subjects
