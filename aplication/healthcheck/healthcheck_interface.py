from abc import ABC, abstractmethod


class HealthcheckInterface(ABC):

    @abstractmethod
    async def get_status():
        pass


class HealthcheckServiceInterface(ABC):

    @abstractmethod
    async def get_status():
        pass


healthcheckInterface = HealthcheckInterface
healthcheckServiceInterface = HealthcheckServiceInterface
