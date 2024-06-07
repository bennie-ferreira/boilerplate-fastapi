from fastapi import APIRouter, status

router = APIRouter()


@router.get("/check", status_code=status.HTTP_200_OK)
def get_status() -> dict:
    return {"status": "UP"}
