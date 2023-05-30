from typing import List

from app.services.course_service import CourseService
from app.schemas.course_schemas import CourseResponse


class CourseController():
    def __init__(self) -> None:
        self.course_service = CourseService()

    def get_all(self, limit:int, offset:int) -> List[CourseResponse]:
        return self.course_service.get_all(limit, offset)