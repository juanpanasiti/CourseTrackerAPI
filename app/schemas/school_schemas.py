from pydantic import BaseModel
from typing import List


from .course_schemas import CourseBase


class SchoolBase(BaseModel):
    category: str | None = None
    name: str | None = None
    description: str | None = None
    platzi_id: str | None = None
    route_url: str | None = None
    about: str | None = None
    badge_url: str | None = None

    courses: List[CourseBase] = []

    def is_valid(self) -> bool:
        return (
            (self.category is not None) and
            (self.name is not None) and
            (self.description is not None) and
            (self.platzi_id is not None) and
            (self.route_url is not None) and
            (self.about is not None) and
            (self.badge_url is not None)
        )

class SchoolResponse(BaseModel):
    id: int
    category: str
    description: str
    platzi_id: str
    route_url: str
    badge_url: str
    name: str
