from fastapi import FastAPI

from adapters.configurator.config import settings
from adapters.web.api.routers.v1.router_base import router_main


def include_router(_app: FastAPI):
    _app.include_router(router_main, prefix=settings.API_V1_STR)


def start_application():
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
    )
    include_router(_app)
    return _app


app = start_application()
