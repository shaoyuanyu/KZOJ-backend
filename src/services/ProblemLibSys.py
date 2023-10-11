from fastapi import APIRouter
from ..models.Problem import Problem, JudgeConfig, ExampleCase, JudgeCase
from ..models.User import User
from ..models.AuthLevel import AuthLevel

router = APIRouter()

@router.post('/add', summary="新建题目")
def addProblem():
	pass

@router.get('/{given_id}', summary="获取题目")
def queryProblem(given_id: str):
	problem = Problem(
		problemId = given_id,
		creater = User(id="000001", userName="TESTER", avatarUrl="", email="xxx@kzoj.cn", auth=AuthLevel.ADMIN),
		title = "TEST PROBLEM TITLE",
		content = """ TEST PROBLEM CONTENT :) """,
		remark = "FOR TEST",
		tags = ["TEST", "EASY"],
		submitCount = 100,
		acceptedCount = 1,
		exampleCase = [
			ExampleCase(caseIn="0", caseOut="0001")
		],
		judgeConfig = [
			JudgeConfig(language="C/C++", timeLimit=300.0, memoryLimit=20.0),
			JudgeConfig(language="Python", timeLimit=300.0, memoryLimit=20.0),
			JudgeConfig(language="Others", timeLimit=300.0, memoryLimit=20.0)
		],
		judgeCase = [
			JudgeCase(caseIn="0", caseOut="0001"),
			JudgeCase(caseIn="1", caseOut="0002"),
			JudgeCase(caseIn="100", caseOut="0101")
		],
		refAnswer = """ print("...") """,
		createTime = "2023/10/11"
	)
	return problem

@router.delete('/delete', summary="根据id删除题目")
def deleteProblemById():
	pass

@router.put('/edit', summary="编辑题目")
def deleteProblemById():
	pass
