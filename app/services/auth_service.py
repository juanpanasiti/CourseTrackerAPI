from app.schemas.auth_schemas import RegisterSchema, LoginSchema
from app.exceptions import client_exceptions as ce, server_exceptions as se, base_http_exception as be
from app.repositories.user_repository import UserRepository
from app.core.jwt import jwt_manager


class AuthService():
    def __init__(self) -> None:
        self.repo = UserRepository()

    def register(self, register_data: RegisterSchema) -> str:
        try:
            user = self.repo.create(register_data.dict())
            payload = {
                'id': str(user.id),
                'role': user.role,
            }
            token = jwt_manager.encode(payload)
            return token
        except Exception as ex:
            # !DELETE PRINT
            print('\033[91m', type(ex), '\033[0m')
            print('\033[93m', ex.args, '\033[0m')
            raise se.InternalServerError('error on AuthService.create()')

    def login(self, credentials: LoginSchema) -> str:
        try:
            user = self.repo.get_one_by_filter({'username': credentials.username})
            if not user.check_password(credentials.password):
                raise ce.Unauthorized('Error on username/password')
            payload = {
                'id': str(user.id),
                'role': user.role,
            }
            token = jwt_manager.encode(payload)
            return token
        # except NotFoundError:
        #     raise ce.Unauthorized('Error on username/password')
        except Exception as ex:
            raise se.InternalServerError()
