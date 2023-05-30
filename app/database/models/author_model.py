from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from . import BaseModel
from app.database.models import course_model


class AuthorModel(BaseModel):
    __tablename__ = 'authors'

    fullname: Mapped[str] = mapped_column(String(100), nullable=False)
    platzi_id: Mapped[str] = mapped_column(String(100), nullable=False)
    bio: Mapped[str] = mapped_column(String(255), default='', nullable=False)
    about: Mapped[str] = mapped_column(Text, default='', nullable=False)
    photo_url: Mapped[str] = mapped_column(String(255), default='', nullable=False)
    profile_url: Mapped[str] = mapped_column(String(255), default='', nullable=False)

    # Relations
    courses: Mapped[List['course_model.CourseModel']] = relationship(lazy='joined')

    def __repr__(self) -> str:
        return f'{self.fullname} (#{self.id})'
