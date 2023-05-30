from sqlalchemy import Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import BaseModel


class SchoolCourseAssociation(BaseModel):
    __tablename__ = 'school_course_associations'
    
    school_id: Mapped[int] = mapped_column(Integer, ForeignKey('schools.id'), primary_key=True)
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey('courses.id'), primary_key=True)