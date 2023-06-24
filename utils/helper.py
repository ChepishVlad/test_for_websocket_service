import uuid
from random import randint

import allure
from faker import Faker

fake = Faker()


@allure.step("Генерация случайного пользователя")
def generate_user():
    return dict(name=fake.first_name(), surname=fake.last_name(), phone=fake.basic_phone_number(), age=randint(1, 100))


@allure.step("Подготовка тела запроса")
def send_request(method: str, _id:str | None = None, **kwargs):
    request = dict(id=id or uuid.uuid4(), method=method, **kwargs)