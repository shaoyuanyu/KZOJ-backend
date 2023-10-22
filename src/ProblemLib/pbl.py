import sqlite3
from ProblemLib.problemlib import ProblemLib

# 题目数据库类
# db就是database
class ProblemLibDB():
	def __init__(self, db_path):
		# 数据成员声明
		self.db_path = db_path
		self.conn: sqlite3.Connection
		self.cursor: sqlite3.Cursor

		# 执行初始化操作
		self.initCheck()

	# 打开数据库
	def openDB(self):
		# 连接数据库
		self.conn = sqlite3.connect(self.db_path)
		# 创建游标
		self.cursor = self.conn.cursor()
	
	# 关闭数据库
	def closeDB(self):
		self.cursor.close()
		self.conn.close()

	# 初始化检查，检查表单是否存在
	def initCheck(self):
		self.openDB()

		# 查询PROBLEMLIB表单
		self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='PROBLEMLIB'")

		# 若PROBLEMLIB表单不存在则创建一个
		if not self.cursor.fetchone():
			# 创建PROBLEMLIB表单
			self.cursor.execute(
				"""CREATE TABLE PROBLEMLIB (
					id TEXT,
					creater TEXT,
					content TEXT,
					remark TEXT,
					tags TEXT,
					submitCount INTEGER,
					acceptedeCount INTEGER,
					refAnswer TEXT,
					createTime TEXT,
					difficultLevel TEXT,
					source TEXT,
					inputDiscription TEXT,
					outputDiscription TEXT
				)"""
			)
			self.conn.commit()
		
		self.closeDB()
	
	# 根据id查询题目
	def queryProblemLibById(self, id):
		self.openDB()

		self.cursor.execute("SELECT * FROM PROBLEMLIB WHERE id='{}'".format(id))
		results = self.cursor.fetchall()

		self.closeDB()

		if len(results) > 1:
			# 查询到多个结果
			# 正常一个id只因查询到一个结果，此时一定是出现问题了，需要写入日志提醒管理员检查
			pass
		elif len(results) == 0:
			# 没有查询到结果
			return None
		else:
			# 查询到结果
			return results[0]

	# 添加题目信息
	def addProblemLib(self, problemlib: ProblemLib):
		# 先查询id所指的题目是否存在
		# 不存在则添加，已存在则返回False报错
		if not self.queryExerciseById(ProblemLib.id):
			self.openDB()

			self.cursor.execute("INSERT INTO PROBLEMLIB VALUES ('{}', '{}', '{}', '{}', '{}',{},{},'{}','{}','{}','{}','{}','{}')".format(problemlib.id,problemlib.creater,problemlib.content,problemlib.remark, problemlib.tags,problemlib.submitCount,problemlib.acceptedeCount,problemlib.refAnswer,problemlib.createTime,problemlib.difficultLevel,problemlib.source,problemlib.outputDiscription,problemlib.inputDiscription))
			self.conn.commit()

			self.closeDB()
		
			return True
		
		else:
			return False

	# 根据id删除题目
	def removeProblemLibById(self, id):
		# 先查询id所指的题目是否存在
		# 存在则删除，不存在则返回False报错
		if self.queryProblemLibById(id):
			self.openDB()

			self.cursor.execute("DELETE FROM PROBLEMLIB WHERE id='{}'".format(id))
			self.conn.commit()

			self.closeDB()

			return True
		
		else:
			return False

	def updateProblemLibById(self, id, newProblemLibInfo: ProblemLib):
		# 先查询id所指的题目是否存在
		# 存在则更新题目信息，不存在则返回False报错
		if self.queryProblemLibById(id):
			self.openDB()

			self.cursor.execute("UPDATE PROBLEMLIB SET creater='{}',content='{}',reamrk='{}',tags='{}',submitCount={},acceptedeCount={},refAnswer='{}',createTime='{}',difficultLevel='{}',source='{}',outputDiscription='{}',nputDiscription='{}' WHERE id = '{}'".format(newProblemLibInfo.creater,newProblemLibInfo.content,newProblemLibInfo.remark,newProblemLibInfo.tags,newProblemLibInfo.submitCount,newProblemLibInfo.acceptedeCount,newProblemLibInfo.refAnswer,newProblemLibInfo.createTime,newProblemLibInfo.difficultLevel,newProblemLibInfo.source,newProblemLibInfo.outputDiscription,newProblemLibInfo.inputDiscription,newProblemLibInfo.id))
			self.conn.commit()

			self.closeDB()

			return True
		
		else:
			return False


def main():
	problemlibDB = ProblemLibDB("./problemlibDatabase.db")
	problemlib = ProblemLib(id="exp001", creater="testAccount", content="00", remark="暂无", tags='未知',submitCount=1,acceptedeCount=1,refAnswer='暂无',createTime='xx的deadline',difficultLevel='┭┮﹏┭┮',source='无',outputDiscription='无',inputDiscription='无')

if __name__ == '__main__':
	main()