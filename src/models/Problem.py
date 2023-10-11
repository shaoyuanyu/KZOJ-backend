from pydantic import BaseModel
from typing import List
from .User import User

# 判题配置
class JudgeConfig(BaseModel):
	# 语言
	language: str
	# 时间限制(ms)
	timeLimit: float
	# 内存限制(MB)
	memoryLimit: float

# 测试用例
class ExampleCase(BaseModel):
	caseIn: str
	caseOut: str

# 判题用例
class JudgeCase(BaseModel):
	caseIn: str
	caseOut: str

# 题目
class Problem(BaseModel):
	problemId: str
	creater: User
	title: str
	content: str
	remark: str
	tags: List[str]
	submitCount: int
	acceptedCount: int
	exampleCase: List[ExampleCase]
	judgeConfig: List[JudgeConfig]
	judgeCase: List[JudgeCase]
	refAnswer: str
	createTime: str
