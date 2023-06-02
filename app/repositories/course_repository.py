from .base_repository import BaseRepository
from app.database.models.course_model import CourseModel


class CourseRepository(BaseRepository[CourseModel]):
    def __init__(self) -> None:
        super().__init__()
        self.model = CourseModel
