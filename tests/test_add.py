import allure

from models.user import User


@allure.story("Positive test creating user with add method")
class TestAddPositive:
    @allure.story("Успешное добавление не существующего пользователя")
    def test_success_creation_user(self):
        # создать юзера
        # проверить, что такого пользователя ещё нет в приложении
        user = User(name="Robert", surname="Poulsen", phone="+71111111111", age=41)
        request_id = ""
        # some_magic
        response = dict #here will be response
        assert response["id"] == request_id, ""
        assert response["method"] == "add"
        assert response["status"] == "success"
        # assert select_creater_user here should be check with select was user created or not


@allure.story("Negative tests not creating user with add method")
class TestAddNegative:
    @allure.story("Нельзя повторно добавить существующего юзера")
    def test_cannot_create_existed_user(self):
        pass
