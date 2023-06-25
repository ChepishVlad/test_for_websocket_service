import json
import uuid

import allure


class Client:
    def __init__(self, ws):
        self.ws = ws

    @allure.step("Отправка запроса на добавление пользоваля")
    def add_user(self, body: dict, _id: str = None):
        data = dict(method="add", id=_id or str(uuid.uuid4()), **body)
        return self.send_request(data=data)

    @allure.step("Отправка запроса на получение пользователей")
    def select_users(self, body: dict, _id: str = None):
        data = dict(method="select", id=_id or str(uuid.uuid4()), **body)
        return self.send_request(data=data)

    @allure.step("Отправка запроса на уделаение опльзователя")
    def delete_user(self, body: dict, _id: str = None):
        data = dict(method="delete", id=_id or str(uuid.uuid4()), **body)
        return self.send_request(data=data)

    @allure.step("Отправка запроса на обновление данных пользователя")
    def update_user(self, body: dict, _id: str = None):
        data = dict(method="update", id=_id or str(uuid.uuid4()), **body)
        return self.send_request(data=data)

    def send_request(self, data: dict):
        print(f"Send request: {data}")
        self.ws.send(json.dumps(data))
        response = json.loads(self.ws.recv())
        print(f"Response is: {response}")
        return response
