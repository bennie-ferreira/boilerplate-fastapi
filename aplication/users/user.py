import uuid

from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: Optional[uuid.UUID] = None
    username: str = ""
    email: str = ""
    password: str = ""

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.username == other.username

    def __hash__(self):
        return hash(self.username)
