from pydantic import BaseModel
from .AuthLevel import AuthLevel

class LoginInfo(BaseModel):
    phone: str
    code: str

class User(BaseModel):
    id: str
    userName: str
    avatarUrl: str
    email: str
    auth: AuthLevel
