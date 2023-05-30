from typing import List

from app.services.school_service import SchoolService
from app.schemas.school_schemas import SchoolResponse


class SchoolController():
    def __init__(self) -> None:
        self.school_service = SchoolService()

    def get_all(self, limit:int, offset:int) -> List[SchoolResponse]:
        return self.school_service.get_all(limit,offset)
