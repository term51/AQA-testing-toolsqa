import os
import random

from data.data import Person

from faker import Faker

from utils.files import get_temp_folder_path

faker_ru = Faker('ru_RU')

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
