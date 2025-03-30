from dataclasses import dataclass

""" 
    @dataclass автоматически создаёт конструктор (__init__), а также методы __repr__, __eq__ и другие.
"""


@dataclass
class Person:
    full_name: str = None
    first_name: str = None
    last_name: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None


@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None
