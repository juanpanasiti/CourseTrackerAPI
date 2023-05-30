from .base_repository import BaseRepository
from app.database.models.school_model import SchoolModel

class SchoolRepository(BaseRepository[SchoolModel]):
    def __init__(self) -> None:
        super().__init__()
        self.model = SchoolModel