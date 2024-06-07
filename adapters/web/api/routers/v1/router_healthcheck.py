from fastapi import APIRouter, status
from aplication.healthcheck.healthcheck_service import HealthcheckService

router = APIRouter()


@router.get("/check", status_code=status.HTTP_200_OK)
async def get_status() -> dict:
    return await HealthcheckService.get_status()
