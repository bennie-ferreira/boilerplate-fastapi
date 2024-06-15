import re
from pydantic import BaseModel, field_validator
from aplication.users.user import User as user


class User(BaseModel, user):
    username: str
    email: str
    password: str

    @field_validator("username")
    def validate_username(cls, value):
        if not re.match("^([a-z]|[0-9]|@)+$", value):
            raise ValueError("username format invalid")
        return value
