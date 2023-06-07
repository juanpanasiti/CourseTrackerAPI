from fastapi.security import OAuth2PasswordRequestForm

from app.services.auth_service import AuthService
from app.schemas.auth_schemas import RegisterSchema, LoginSchema, TokenResponse


class AuthorController():
    def __init__(self) -> None:
        self.auth_service = AuthService()

    def register(self, user_data: RegisterSchema) -> str:
        return TokenResponse(access_token=self.auth_service.register(user_data))

    def login(self, credentials: OAuth2PasswordRequestForm):
        login_data = LoginSchema(username=credentials.username, password=credentials.password)
        return TokenResponse(access_token=self.auth_service.login(login_data))
