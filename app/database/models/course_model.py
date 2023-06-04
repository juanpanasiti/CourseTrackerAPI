from sqlalchemy import Integer, String, Boolean, Text, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from . import BaseModel
from app.core.enums.level_enum import LevelEnum
from app.core.enums.status_enum import StatusEnum
from app.database.models import author_model
from app.database.models import school_model


class CourseModel(BaseModel):
    __tablename__ = 'courses'

    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, default='', nullable=False)
    level: Mapped[str] = mapped_column(Enum(LevelEnum), default=LevelEnum.UNDEFINED, nullable=False)
    platzi_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    platzi_url: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(Enum(StatusEnum),default=StatusEnum.TO_CHECK, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean,default=True, nullable=False)
    score: Mapped[int] = mapped_column(Integer, default=-1, nullable=False)
    badge_url: Mapped[str] = mapped_column(String(255), default='', nullable=False)
    first_class_url: Mapped[str] = mapped_column(String(255), default='', nullable=False)

    backup_url: Mapped[str] = mapped_column(String(255), default='', server_default='', nullable=False)

    # FKs
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey('authors.id'))

    # Relations
    author: Mapped['author_model.AuthorModel'] = relationship(lazy='joined', back_populates='courses')
    schools: Mapped[List['school_model.SchoolModel']] = relationship(secondary='school_course_associations', back_populates='courses')


    def __repr__(self) -> str:
        return f'Course {self.title} [{self.platzi_id}] (#{self.id})'