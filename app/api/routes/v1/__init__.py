from fastapi import APIRouter

from .scrapping_routes import router as scrapping_router
from .school_routes import router as school_router
from .course_routes import router as course_router
from .author_routes import router as author_router
from .auth_routes import router as auth_router

router_v1 = APIRouter(prefix='/v1')

router_v1.include_router(scrapping_router, tags=['Scarpping'])
router_v1.include_router(school_router, tags=['School'])
router_v1.include_router(course_router, tags=['Course'])
router_v1.include_router(author_router, tags=['Author'])
router_v1.include_router(auth_router, tags=['Auth'])
