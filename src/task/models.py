from sqlalchemy.orm import mapped_column, Mapped
from src.database import Base
from sqlalchemy import ForeignKey

class Tasks(Base):

    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    author: Mapped[str] = mapped_column(ForeignKey('users.id'), nullable=True)

