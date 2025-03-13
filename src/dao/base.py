from src.database import async_session
from sqlalchemy import select, insert


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod 
    async def add(cls, data: dict):
        async with async_session() as session:
            stmt = insert(cls.model).values(**data)
            await session.execute(stmt)
            await session.commit()

