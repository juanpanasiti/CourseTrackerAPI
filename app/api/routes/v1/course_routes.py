from typing import List

from fastapi import APIRouter, Query, Path

from app.controllers.course_controller import CourseController
from app.schemas.course_schemas import CourseResponse, CourseRequestUpdate


router = APIRouter(prefix='/courses')
controller = CourseController()


@router.get('/')
async def get_all_paginated(limit: int = Query(gt=0, default=10), offset: int = Query(ge=0, default=0)) -> List[CourseResponse]:
    return controller.get_all(limit,offset)

@router.patch('/{course_id}')
async def update_course(new_data: CourseRequestUpdate, course_id: int = Path(ge=1)) -> CourseResponse:
    return controller.update(course_id, new_data)