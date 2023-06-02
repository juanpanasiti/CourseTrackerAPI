from pydantic import BaseModel

from app.core.enums.level_enum import LevelEnum
from app.core.enums.status_enum import StatusEnum
from .author_schemas import AuthorBase


class CourseBase(BaseModel):
    title: str | None = None
    description: str = ''
    level: LevelEnum = LevelEnum.UNDEFINED
    platzi_id: int | None = None
    platzi_url: str | None = None
    status: StatusEnum = StatusEnum.TO_CHECK
    is_active: bool = True
    score: int = -1
    badge_url: str | None = None
    first_class_url: str | None = None
    author: AuthorBase = AuthorBase()

    def is_valid(self) -> bool:
        return (
            (self.title is not None) and
            (self.description is not None) and
            (self.level is not None) and
            (self.platzi_id is not None) and
            (self.platzi_url is not None) and
            (self.status is not None) and
            (self.is_active is not None) and
            (self.score is not None)
        )
    
class CourseAuthor(BaseModel):
    id: int
    fullname: str

class CourseResponse(BaseModel):
    title: str
    description: str
    level: str
    status: str
    platzi_id: int
    score: int
    first_class_url: str
    author: CourseAuthor
    id: int
    platzi_url: str
    is_active: bool
    badge_url: str
    backup_url: str

class CourseRequestUpdate(CourseBase):
    title: str | None = None
    description: str | None = None
    level: LevelEnum | None = None
    platzi_id: int | None = None
    platzi_url: str | None = None
    status: StatusEnum | None = None
    is_active: bool | None = None
    score: int | None = None
    badge_url: str | None = None
    first_class_url: str | None = None
    author: AuthorBase | None = None

    def clean_data(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None }