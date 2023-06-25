from dataclasses import asdict

import pytest
from websockets.sync.client import connect
from utils.client import Client
from utils.models import User


@pytest.fixture(scope="module")
def ws():
    with connect("ws://127.0.0.1:4000") as websocket:
        client = Client(ws=websocket)
        yield client


@pytest.fixture(scope="function")
def not_existed_user(ws):
    existed = True
    user = User()
    while existed:
        random_user = User().random_user()
        response = ws.select_users(body=dict(phone=random_user.phone))
        if response.get("status") == "failure" and not response.get("users"):
            user = random_user
            existed = False
    return user


@pytest.fixture(scope="function")
def existed_user(ws):
    # TODO Перепелить фикстуру так, чтобы она возвраащала список пользователей по дефолту одного, но можно было
    #  законфигурить из теста на несколько
    user = User().random_user()
    select = ws.select_users(body=dict(phone=user.phone))
    if select.get("status") == "failure" and not select.get("users"):
        ws.add_user(body=asdict(user))
    yield user
    ws.delete_user(body=dict(phone=user.phone))
