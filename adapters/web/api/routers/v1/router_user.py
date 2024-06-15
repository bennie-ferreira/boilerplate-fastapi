from fastapi import APIRouter, status
from adapters.repositories.users import UserRepository
from adapters.web.api.schemas.user import User


router = APIRouter()


@router.get("/list-users", status_code=status.HTTP_200_OK)
async def list_users():
    return await UserRepository.list_users()


@router.get("/get-user/{id}", status_code=status.HTTP_200_OK)
async def get_user(id: str):
    return await UserRepository.get_user(id=id)


@router.post("/create-user", status_code=status.HTTP_200_OK)
async def create_user(user: User):
    return await UserRepository.create_user(user)


@router.put("/update-user", status_code=status.HTTP_200_OK)
async def update_user(user: User):
    return await UserRepository.edit_user(user)


@router.delete("/delete-user/{id}", status_code=status.HTTP_200_OK)
async def delete_user(id: str):
    return await UserRepository.delete_user(id=id)
