from .healthcheck import healthcheck
from .healthcheck_interface import healthcheckServiceInterface


class HealthcheckService(healthcheckServiceInterface):

    async def get_status():
        return await healthcheck.get_status()
