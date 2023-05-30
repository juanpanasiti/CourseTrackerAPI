from fastapi import APIRouter

from app.controllers.scrapping_controller import ScrappingController

router = APIRouter(prefix='/scrapping')
controller = ScrappingController()

@router.post('/schools')
async def scrap_schools():
    return controller.scrap_schools()
