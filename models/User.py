from pydantic import BaseModel

class LoginInfo(BaseModel):
    phone: str
    code: str
