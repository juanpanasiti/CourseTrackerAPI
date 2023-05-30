from typing import List

from app.services.author_service import AuthorService
from app.schemas.author_schemas import AuthorResponse


class AuthorController():
    def __init__(self) -> None:
        self.author_service = AuthorService()
    
    def get_all(self, limit:int, offset:int) -> List[AuthorResponse]:
        return self.author_service.get_all(limit,offset)