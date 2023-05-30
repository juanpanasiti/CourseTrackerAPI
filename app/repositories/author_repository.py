from .base_repository import BaseRepository
from app.database.models.author_model import AuthorModel

class AuthorRepository(BaseRepository[AuthorModel]):
    def __init__(self) -> None:
        super().__init__()
        self.model = AuthorModel