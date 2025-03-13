from typing import Annotated
from fastapi import APIRouter, Depends
from src.task.schemas import Tasks_Schema
from src.task.base import TasksDAO

router = APIRouter(
    prefix='/tasks',
    tags={'Tasks'}
)

@router.get('')
async def get_all_tasks() -> list[Tasks_Schema]:
    return await TasksDAO.find_all()

@router.post('')
async def add_task(
    task: Annotated[Tasks_Schema, Depends()]
):
    await TasksDAO.add(task.model_dump())
    return {'ok': True}