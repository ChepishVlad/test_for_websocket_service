import json
import logging
import uuid

import allure

from utils.checkers import validate_request

logger = logging.getLogger("handlers")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)


class Client:
    def __init__(self, ws):
        self.ws = ws

    @allure.step("Отправка запроса на добавление пользоваля")
    def add_user(self, body: dict, _id: str = None, exp_status: str = None):
        data = dict(method="add", id=_id or str(uuid.uuid4()), **body)
        return self.send_request(data=data, exp_status=exp_status)

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

    @validate_request
    def send_request(self, data: dict, **kwargs):
        logger.debug(f"Message: {data} was sent")
        self.ws.send(json.dumps(data))
        response = json.loads(self.ws.recv())
        logger.debug(f"Message: {data} was received")
        return response
