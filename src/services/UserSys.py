from fastapi import APIRouter
from ..models.User import LoginInfo

router = APIRouter()

@router.post('/code', summary="发送验证码")
def sendCode():
	pass

@router.post('/login/byCode', summary="验证码登录")
def loginByCode(login_info: LoginInfo):
	print(login_info.phone, login_info.code)
	return { 'ok' }

@router.post('/login/byPasswd', summary="密码登录")
def loginByCode():
	pass

@router.get('/queryAccount', summary="获取账号信息")
def queryAccount():
	pass

@router.post('/updateAccount', summary="更新账号信息")
def updateAccountInfo():
	pass

@router.put('/updateAvatar', summary="更新头像")
def updateAccountInfo():
	pass

@router.get('/account/{account_id}', summary="通过id查询账号")
def queryAccountById(accound_id: str):
	pass
