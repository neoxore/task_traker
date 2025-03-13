from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL, 
    echo=False,
    pool_size=5,
    max_overflow=10,
    pool_recycle=1800,
    pool_pre_ping=True
)

async_session = sessionmaker(
    engine,
    class_=AsyncSession, 
    expire_on_commit=False,
    autocommit=False
)

class Base(DeclarativeBase):
    pass
