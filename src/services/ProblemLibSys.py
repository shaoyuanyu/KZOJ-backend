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
		id = given_id,
		creater = User(id="000001", userName="TESTER", avatarUrl="", email="xxx@kzoj.cn", auth=AuthLevel.ADMIN),
		title = "Hello,World!",
		content = [
			"""编写一个能够输出“Hello,World!”的程序，这个程序常常作为一个初学者接触一门新的编程语言所写的第一个程序，也经常用来测试开发、编译环境是否能够正常工作。""",
			"""提示：“Hello,World!”中间没空格。"""
		],
		remark = "FOR TEST",
		tags = ["TEST", "EASY"],
		submitCount = 100,
		acceptedCount = 1,
		judgeConfig = [
			JudgeConfig(language="C/C++", timeLimit=300.0, memoryLimit=20.0),
			JudgeConfig(language="Python", timeLimit=301.0, memoryLimit=21.0),
			JudgeConfig(language="Others", timeLimit=30.0, memoryLimit=2.0)
		],
		judgeCases = [
			JudgeCase(caseIn="", caseOut="Hello,World!"),
		],
		exampleCases = [
			ExampleCase(caseIn="", caseOut="Hello,World!")
		],
		refAnswer = """print("Hello,World!")""",
		createTime = "2023/10/11",

		difficultLevel = "easy",
		source = "一本通",
		inputDiscription = "无输入",
		outputDiscription = "输出字符串Hello,World!"
	)
	return problem

@router.delete('/delete', summary="根据id删除题目")
def deleteProblemById():
	pass

@router.put('/edit', summary="编辑题目")
def deleteProblemById():
	pass
