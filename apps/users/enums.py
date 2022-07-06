from enum import Enum


class RegEx(Enum):
    PASSWORD = (r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,50}$', [
        'password must contain 1 number(0 - 9)',
        'password must contain 1 uppercase letters',
        'password must contain 1 lowercase letters',
        'password must contain 1 non - alpha numeric number',
        'password is 8 - 16 characters with no space',
    ])
    NAME = (
        r'^[a-zA-Z]{5,20}$',
        ['Something went wrong, your name can`t contain numbers or other non-alphabetic symbols'],
    )
    PHONE = (
        r'(?=.*[0-9]{3}[0-9]{2}[0-9]{3}[0-9]{4,5}$)',
        ['Number can`t contain whitespaces', 'Number can`t contain any other character but digits']
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
