from src.database import Base
from sqlalchemy.orm import mapped_column, Mapped

class Users(Base):

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hash_password: Mapped[str] = mapped_column(unique=True, nullable=False)
    

