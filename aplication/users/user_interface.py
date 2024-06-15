from typing import List

from abc import ABC, abstractmethod
from .user import User


class UserInterface(ABC):

    @abstractmethod
    async def get_user() -> User:
        pass

    @abstractmethod
    async def list_users() -> List[User]:
        pass

    @abstractmethod
    async def create_user() -> User:
        pass

    @abstractmethod
    async def edit_user() -> User:
        pass

    @abstractmethod
    async def create_or_update():
        pass

    @abstractmethod
    async def delete_user() -> User:
        pass


class UserRepositoryInterface(UserInterface): ...


userInterface = UserInterface
userRepositoryInterface = UserRepositoryInterface
