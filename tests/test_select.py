import uuid
from copy import deepcopy
from dataclasses import asdict

import allure
import pytest
from faker import Faker

from utils.models import User


@allure.story("Сценарные тесты для метода select")
class TestSelectPositive:
    @allure.story("Поиск пользователя по номеру телефона")
    @pytest.mark.skip("[Bug #1]")
    def test_select_existed_user_by_phone(self, ws, existed_user):
        # создать пользователя, но не добавлять в систему
        # выполнить запрос
        # провалидировать ответ (должен возвращаться только один пользователь
        _id = str(uuid.uuid4())
        select_response = ws.select_users(body=dict(phone=existed_user.phone), _id=_id)
        assert select_response.get("status") == "success"
        assert select_response.get("id") == id
        assert select_response.get("method") == "select"
        assert User(**select_response.get("users")[0]) == existed_user

    @pytest.mark.parametrize("field", ["surname"])
    @pytest.mark.skip("[Bug #1], [Bug #4]")
    def test_select_user_by_name_or_surname(self, ws, field):
        # TODO по хорошему вынести создания пользователей в фикстуру (точнее подправить существующую, чтобы она выдавала список пользователей
        users = [
            User(
                name="Name",
                surname="Surname",
                phone=Faker().basic_phone_number(),
                age=50,
            )
            for _ in range(2)
        ]
        [ws.add_user(body=asdict(user)) for user in users]
        _id = str(uuid.uuid4())
        request = (
            dict(name=users[0].name)
            if field == "name"
            else dict(surname=users[0].surname)
        )
        select_response = ws.select_users(body=request, _id=_id)
        assert select_response.get("status") == "success"
        assert select_response.get("id") == _id
        assert select_response.get("method") == "select"
        assert sorted(users, key=lambda x: x.phone) == sorted(
            [User(**user) for user in select_response.get("users")],
            key=lambda x: x.phone,
        )


class TestValidationRequiredFields:
    def test_request_without(self, ws):
        select_response = ws.delete_user(body=dict())
        assert "key 'phone' not found" in select_response.get("reason")
        assert select_response.get("status") == "failure"
