from pydantic import BaseModel
from typing import List

# 题目预览
# 查看题库或其他表单时使用的预览
class ProblemPreview(BaseModel):
	id: str
	title: str
	createTime: str
	tags: List[str]
	submitCount: int
	acceptedCount: int

# 题目预览队列查询
class ProblemPreviewsQuery(BaseModel):
    # 排序依据
    sortedBy: str
    # 是否正序
    orderASC: bool

    # 序列始终
    rangeStart: int
    rangeEnd: int
