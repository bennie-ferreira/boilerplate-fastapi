from .healthcheck_interface import healthcheckInterface


class Healthcheck(healthcheckInterface):

    async def get_status():
        return {"STATUS": "OK"}


healthcheck = Healthcheck
