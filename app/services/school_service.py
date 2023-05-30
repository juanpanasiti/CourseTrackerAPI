from typing import List

from app.repositories.school_repository import SchoolRepository
from app.schemas.school_schemas import SchoolResponse
from app.database.models.school_model import SchoolModel



class SchoolService():
    def __init__(self) -> None:
        self.school_repo = SchoolRepository()

    def __model_to_schema(self, school_db: SchoolModel) -> SchoolResponse:
        return SchoolResponse(
            id=school_db.id,
            category=school_db.category,
            description=school_db.description,
            platzi_id=school_db.platzi_id,
            route_url=school_db.route_url,
            badge_url=school_db.badge_url,
            name=school_db.name,
        )

    def get_all(self, limit:int, offset:int)-> List[SchoolResponse]:
        schools_db = self.school_repo.get_all(limit, offset)
        return [self.__model_to_schema(school) for school in schools_db]