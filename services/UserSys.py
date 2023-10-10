from fastapi import APIRouter

from pydantic import BaseModel

router = APIRouter()

class LoginInfo(BaseModel):
    phone: str
    code: str

@router.post('/login')
def loginByCode(login_info: LoginInfo):
	print(login_info.phone, login_info.code)
	return { 'ok' }