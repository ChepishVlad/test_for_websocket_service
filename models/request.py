from dataclasses import dataclass


@dataclass
class Request:
    id: str = None
    method: str = None
    body: dict = None


@dataclass
class Response:
    id: str = None
    method: str = None
    status: str = None
    body: dict = None
