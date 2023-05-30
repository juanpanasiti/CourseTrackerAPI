from pydantic import BaseModel


class AuthorBase(BaseModel):
    fullname: str = ''
    platzi_id: str =''
    bio: str =''
    about: str =''
    photo_url: str =''
    profile_url: str =''

class AuthorResponse(BaseModel):
    id: int
    # platzi_id: str
    fullname: str
    photo_url: str
    courses: list[int]