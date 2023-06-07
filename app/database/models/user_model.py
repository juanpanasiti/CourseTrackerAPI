import bcrypt
from sqlalchemy import String
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from . import BaseModel
from app.core.enums.role_enum import RoleEnum


class UserModel(BaseModel):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(String(64), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[str] = mapped_column(Enum(RoleEnum), default=RoleEnum.UNCONFIRMED, nullable=False)

    @property
    def password(self):
        return self.hashed_password
    
    @password.setter
    def password(self, password:str):
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())
        self.hashed_password = hashed_password.decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password.encode('utf-8'))

    def __str__(self) -> str:
        return f'User {self.username} ({self.email})'

    def __repr__(self) -> str:
        return f'User {self.username} ({self.email})'
