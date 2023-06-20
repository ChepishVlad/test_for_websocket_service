from dataclasses import dataclass


@dataclass
class User:
    name: str = None
    surname: str = None
    phone: str = None
    age: int = None

