from fastapi import APIRouter
from src.users.schemas import Users_Schema
from src.users.base import UsersDAO


router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('')
async def get_all_users() -> list[Users_Schema]:
    return await UsersDAO.find_all()