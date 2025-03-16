from typing import Annotated
from fastapi import APIRouter, Depends, Path
from src.task.schemas import Tasks_Schema, Tasks_SchemaID
from src.task.base import TasksDAO

router = APIRouter(
    prefix='/tasks',
    tags={'Tasks'}
)

@router.get('')
async def get_all_tasks() -> list[Tasks_SchemaID]:
    return await TasksDAO.find_all_func()

@router.get('/{task_id}')
async def get_task_id(task_id: int):
    return await TasksDAO.find_one_or_none(task_id)

@router.post('')
async def add_task(
    task: Annotated[Tasks_Schema, Depends()]
):
    await TasksDAO.add_func(task.model_dump())
    return {'ok': True}

@router.delete('/{task_id}')
async def delete_task(task_id: int):
    await TasksDAO.delete_func(task_id)
    return {'ok': True}

@router.put('/{task_id}')
async def update_task(
    task_id: Annotated[int, Path()],  
    task: Annotated[Tasks_Schema, Depends()] 
):
    await TasksDAO.update_func(task_id, task.model_dump())
    return {'ok': True}