from dataclasses import asdict

import allure
import pytest

from utils.models import User


@allure.story("Сценарные тесты для метода add")
class TestAddBusinessLogic:
    @allure.story("Успешное добавление не существующего пользователя")
    def test_success_creation_user(self, ws, not_existed_user):
        ws.add_user(body=asdict(not_existed_user))
        select_response = ws.select_users(body=dict(phone=not_existed_user.phone))
        assert User(**select_response.get("users")[0]) == not_existed_user

    @pytest.mark.skip(
        "[Bug #2] При добавлении существующего пользователя - нет поля 'reason' в ответе"
    )
    @allure.story("Нельзя повторно добавить существующего юзера")
    def test_cannot_create_existed_user(self, ws, existed_user):
        add_response = ws.add_user(body=asdict(existed_user), exp_status="failure")
        # TODO согласовать с Сарой или Джо - какой текст причины мы ожидаем
        assert add_response.get("reason") == ""
        users = ws.select_users(body=dict(name=existed_user.name)).get("users")
        assert len(users) == 1, "Должен быть только один пользователь в ответе"
        assert (
            User(**users[0]) == existed_user
        ), "Данные существующего пользователя не должны были изменится"


@allure.story("Негативные тесты проверящюие, что пользоваль не создаётся")
class TestAddValidationFields:
    @allure.story(
        "Провалидировать обязательные поля. Попытка добавить пользователя без одного из полей"
    )
    @pytest.mark.parametrize("field", ["name", "surname", "age", "phone"])
    def test_validate_required_fields(self, ws, field, not_existed_user):
        user = asdict(not_existed_user)
        user.pop(field)
        response = ws.add_user(body=dict(user), exp_status="failure")
        assert f"key '{str(field)}' not found" in response.get("reason")

    @allure.story("Валидация значения поля возраст")
    @pytest.mark.parametrize(
        "age, status",
        [
            pytest.param(
                -1,
                "failure",
                marks=pytest.mark.skip("[Bug #3] age cpuldn't be negative"),
            ),
            pytest.param(0, "failure", marks=pytest.mark.skip("needs to be agreed")),
            pytest.param(1, "success"),
            pytest.param(
                9223372036854775808,
                "failure",
                marks=pytest.mark.skip("needs to be agreed"),
            ),
        ],
    )
    def test_validation_values(self, ws, not_existed_user, age, status):
        user = not_existed_user
        user.age = age
        ws.add_user(body=asdict(not_existed_user), exp_status=status)
        select = ws.select_users(body=dict(phone=not_existed_user.phone))
        assert (
            not select.get("users")
            if status == "failure"
            else User(**select.get("users")[0]) == not_existed_user
        )
