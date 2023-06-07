from pydantic import BaseModel, EmailStr


class LoginSchema(BaseModel):
    username: str
    password: str

class RegisterSchema(LoginSchema):
    email: EmailStr


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'
