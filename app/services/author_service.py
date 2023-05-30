from typing import List

from app.repositories.author_repository import AuthorRepository
from app.database.models.author_model import AuthorModel
from app.schemas.author_schemas import AuthorResponse


class AuthorService():
    def __init__(self) -> None:
        self.author_repo = AuthorRepository()

    def __model_to_schema(self, author_db: AuthorModel) -> AuthorResponse:
        return AuthorResponse(
            id=author_db.id,
            fullname=author_db.fullname,
            platzi_id=author_db.platzi_id,
            photo_url=author_db.photo_url,
            courses=[course.id for course in author_db.courses],
        )
    
    def get_all(self, limit:int, offset:int) -> List[AuthorResponse]:
        authors = self.author_repo.get_all(limit, offset)

        return [self.__model_to_schema(author) for author in authors]