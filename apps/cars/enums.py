from enum import Enum


class RegEx(Enum):
    NAME = (
        r'^[a-zA-Z]{5,20}$',
        ['Something went wrong, your name can`t contain numbers or other non-alphabetic symbols'],)

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
