from fastapi import APIRouter

from ..v1 import router_ping

router_main = APIRouter()

router_main.include_router(router_ping.router, prefix="/health", tags=["health"])
