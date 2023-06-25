from dataclasses import dataclass
from random import randint

from faker import Faker

fake = Faker()


@dataclass
class User:
    name: str = None
    surname: str = None
    age: int = None
    phone: str = None

    @classmethod
    def random_user(cls):
        return cls(
            name=fake.first_name(),
            surname=fake.last_name(),
            phone=fake.basic_phone_number(),
            age=randint(1, 100),
        )
