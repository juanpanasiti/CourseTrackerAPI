from app.repositories.course_repository import CourseRepository
from app.database.models.course_model import CourseModel
from app.schemas.course_schemas import CourseResponse, CourseAuthor


class CourseService():
    def __init__(self) -> None:
        self.course_repo = CourseRepository()

    def __model_to_schema(self, course_db: CourseModel) -> CourseResponse:
        author = CourseAuthor(
            id=course_db.author_id,
            fullname=course_db.author.fullname if course_db.author else 'NONAME'
            )
        return CourseResponse(
            level=course_db.level,
            description=course_db.description,
            platzi_id=course_db.platzi_id,
            status=course_db.status,
            score=course_db.score,
            first_class_url=course_db.first_class_url,
            id=course_db.id,
            title=course_db.title,
            platzi_url=course_db.platzi_url,
            is_active=course_db.is_active,
            badge_url=course_db.badge_url,
            backup_url=course_db.backup_url,
            author=author,
        )
    
    def get_all(self, limit:int, offset:int):
        courses_db = self.course_repo.get_all(limit, offset)
        return [self.__model_to_schema(course) for course in courses_db]