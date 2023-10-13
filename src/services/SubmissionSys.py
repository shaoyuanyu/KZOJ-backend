from fastapi import APIRouter

router = APIRouter()

@router.post('/submit', summary="提交")
def submit():
	pass

@router.get('/status/{id}', summary="根据id查询提交状态")
def queryStatusById(id: str):
	pass
