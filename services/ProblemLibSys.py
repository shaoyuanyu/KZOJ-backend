from fastapi import APIRouter

router = APIRouter()

@router.post('/add', summary="新建题目")
def addProblem():
	pass

@router.delete('/delete', summary="根据id删除题目")
def deleteProblemById():
	pass

@router.put('/edit', summary="编辑题目")
def deleteProblemById():
	pass
