from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from . import BaseModel


class SchoolModel(BaseModel):
    __tablename__ = 'schools'

    # fullname: Mapped[str] = mapped_column(String(100), nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, default='', nullable=False)
    platzi_id: Mapped[str] = mapped_column(String(100), nullable=False)
    route_url: Mapped[str] = mapped_column(String(255), default='', nullable=False)
    about: Mapped[str] = mapped_column(Text, default='', nullable=False)
    badge_url: Mapped[str] = mapped_column(String(255), default='', nullable=False)

    # Relations
    courses: Mapped[List['CourseModel']] = relationship(secondary='school_course_associations', back_populates='schools')

    def __repr__(self) -> str:
        return f'School {self.name} of {self.category} (#{self.id})'
