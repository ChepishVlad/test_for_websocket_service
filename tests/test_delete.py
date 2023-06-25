import uuid
import allure


@allure.story("Сценарные тесты для метода delete")
class TestDeletePositive:
    @allure.story("Успешное удаление существующего пользователя")
    def test_delete_existed_user(self, ws, existed_user):
        _id = str(uuid.uuid4())
        delete_response = ws.delete_user(body=dict(phone=existed_user.phone), _id=_id)
        assert delete_response.get("id") == _id
        assert delete_response.get("status") == "success"
        assert delete_response.get("method") == "delete"

        with allure.step(
            "Проверка, что удаленный пользователь больше не находится по запросу"
        ):
            select_response = ws.select_users(body=dict(phone=existed_user.phone))
            assert select_response.get("status") == "failure"
            assert not select_response.get("users")

    @allure.story("Попытка удаления не существующего пользователя")
    def test_try_to_delete_not_existed_user(self, ws, not_existed_user):
        _id = str(uuid.uuid4())
        delete_response = ws.delete_user(
            body=dict(phone=not_existed_user.phone), _id=_id
        )
        assert delete_response.get("status") == "failure"
        assert delete_response.get("id") == _id
        assert delete_response.get("method") == "delete"
        assert not delete_response.get("reason")


class TestValidationRequiredFields:
    @allure.story("Валидация работы ручки без обязательного параметра")
    def test_request_without_phone(self, ws):
        delete_response = ws.delete_user(body=dict())
        assert "key 'phone' not found" in delete_response.get("reason")
        assert delete_response.get("status") == "failure"
