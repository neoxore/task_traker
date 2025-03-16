from src.database import async_session
from sqlalchemy import delete, select, insert, update
from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound, SQLAlchemyError


class BaseDAO:
    model = None

    @classmethod
    async def find_all_func(cls, **filter_by):
        async with async_session() as session:
            try:
                query = select(cls.model).filter_by(**filter_by)
                result = await session.execute(query)
                return result.scalars().all()
            
            except SQLAlchemyError as e:
                print(f'Database error: {e}')
                raise HTTPException(status_code=500, detail='Database query failed')
                

    @classmethod 
    async def add_func(cls, data: dict):
        async with async_session() as session:
            try:
                query = insert(cls.model).values(**data).returning(cls.model)
                await session.execute(query)
                await session.commit()

            except SQLAlchemyError as e:
                print(f'Database error: {e}')
                raise HTTPException(status_code=500, detail='Failed to create task')

    @classmethod 
    async def delete_func(cls, obj_id: int):
        async with async_session() as session:
            try:
                query = delete(cls.model).where(cls.model.id == obj_id)
                result = await session.execute(query)
                if result.rowcount == 0:
                    raise HTTPException(status_code=404, detail='Task not found')
                await session.commit()
            
            except SQLAlchemyError as e:
                print(f'Database error: {e}')
                raise HTTPException(status_code=500, detail='Failed to delete data')
            

    @classmethod
    async def update_func(cls, obj_id: int, data: dict):
        async with async_session() as session:
            try:
                query = update(cls.model).where(cls.model.id == obj_id).values(**data)
                result = await session.execute(query)
                if result.rowcount == 0:
                    raise HTTPException(status_code=404, detail='Task not found')
                await session.commit()
            
            except SQLAlchemyError as e:
                print(f'Database error: {e}')
                raise HTTPException(status_code=500, detail='Failed to update data')


    @classmethod 
    async def find_one_or_none(cls, obj_id: int):
        if not obj_id:
            return None
        
        async with async_session() as session:
            try:
                query = select(cls.model).where(cls.model.id == obj_id)
                result = await session.execute(query)
                obj = result.scalar_one_or_none() 

                if obj is None:
                    raise HTTPException(status_code=404, detail='Task not found')
                return obj
            
            except SQLAlchemyError as e:
                print(f"Database error: {e}") 
            raise HTTPException(status_code=500, detail="Database error")  
            



