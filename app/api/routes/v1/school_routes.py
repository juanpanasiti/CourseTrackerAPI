from typing import List

from fastapi import APIRouter, Query

from app.controllers.school_controller import SchoolController
from app.schemas.school_schemas import SchoolResponse

router = APIRouter(prefix='/schools')
controller = SchoolController()


@router.get('/')
async def get_all_paginated(limit: int = Query(gt=0, default=10), offset: int = Query(ge=0, default=0)) -> List[SchoolResponse]:
    return controller.get_all(limit,offset)