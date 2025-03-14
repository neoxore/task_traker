from src.database import async_session
from sqlalchemy import delete, select, insert, update


class BaseDAO:
    model = None

    @classmethod
    async def find_all_func(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod 
    async def add_func(cls, data: dict):
        async with async_session() as session:
            stmt = insert(cls.model).values(**data)
            await session.execute(stmt)
            await session.commit()

    @classmethod 
    async def delete_func(cls, obj_id: int):
        async with async_session() as session:
            query = delete(cls.model).where(cls.model.id == obj_id)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update_func(cls, obj_id: int, data: dict):
        async with async_session() as session:
            query = update(cls.model).where(cls.model.id == obj_id).values(**data)
            await session.execute(query)
            await session.commit()



