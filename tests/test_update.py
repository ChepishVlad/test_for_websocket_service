import uuid
from dataclasses import asdict

import allure
import pytest

from utils.models import User


@allure.story("Сценарные тесты для метода update")
class TestUpdatePositive:
    @pytest.mark.skip("[Bug] Не обновляется возраст пользователя")
    @allure.story("Обновление всех полей, кроме телефона существующего пользователя")
    def test_update_existed_user(self, ws, existed_user):
        existed_user.name = "new_name"
        existed_user.surname = "new_surname"
        existed_user.age = existed_user.age + 1
        _id = str(uuid.uuid4())
        update_response = ws.update_user(body=asdict(existed_user), _id=_id)
        assert update_response.get("status") == "success"
        assert update_response.get("id") == _id
        assert update_response.get("method") == "update"
        select = ws.select_users(body=dict(phone=existed_user.phone))
        assert User(**select.get("users")[0]) == existed_user


class TestUpdateNegative:
    @allure.story("Валидация работы ручки без обязательного параметра")
    def test_update_not_existed_user(self, ws, existed_user):
        existed_user.phone = f"{existed_user.phone}2"
        _id = str(uuid.uuid4())
        update_response = ws.update_user(body=asdict(existed_user), _id=_id)
        assert update_response.get("status") == "failure"
        assert update_response.get("id") == _id
        assert update_response.get("method") == "update"
