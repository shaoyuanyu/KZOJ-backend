from fastapi import APIRouter
from ..models.Problem import Problem, JudgeConfig, ExampleCase, JudgeCase
from ..models.ProblemPreview import ProblemPreviewsQuery
from ..models.User import User
from ..models.AuthLevel import AuthLevel

# 假数据
from ..dataManager.problemManager import getExampleProblem, getExampleProblemPreviews

router = APIRouter()

@router.post('/add', summary="新建题目")
def addProblem():
	pass

@router.get('/getProblem/{given_id}', summary="获取题目")
def queryProblem(given_id: str):
	return getExampleProblem()

@router.post('/getPreviews', summary="获取题目预览队列")
def queryProblemPreviews(problemPreviewsQuery: ProblemPreviewsQuery):
	print(problemPreviewsQuery)
	return getExampleProblemPreviews()

@router.delete('/delete', summary="根据id删除题目")
def deleteProblemById():
	pass

@router.put('/edit', summary="编辑题目")
def deleteProblemById():
	pass
