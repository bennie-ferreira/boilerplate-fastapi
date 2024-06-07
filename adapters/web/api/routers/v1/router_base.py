from fastapi import APIRouter

from . import router_healthcheck

router_main = APIRouter()

router_main.include_router(router_healthcheck.router, prefix="/health", tags=["health"])
