from typing import List

from fastapi import APIRouter, Query

from app.controllers.author_controller import AuthorController
from app.schemas.author_schemas import AuthorResponse

router = APIRouter(prefix='/authors')
controller = AuthorController()


@router.get('/')
async def get_all_paginated(limit: int = Query(gt=0, default=10), offset: int = Query(ge=0, default=0)) -> List[AuthorResponse]:
    return controller.get_all(limit, offset)