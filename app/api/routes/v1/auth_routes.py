from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.auth_schemas import TokenResponse, RegisterSchema
from app.controllers.auth_controller import AuthorController


router = APIRouter(prefix='/auth')
controller = AuthorController()


@router.post('/register')
async def register(credentials: RegisterSchema) -> TokenResponse:
    return controller.register(credentials)


@router.post('/login')
async def login(credentials: OAuth2PasswordRequestForm = Depends()) -> TokenResponse:
    return controller.login(credentials)
