import sqlite3
from models.account import Account

# 账号数据库类
# db就是database
class AccountDB():
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

		# 查询account表单
		self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ACCOUNT'")

		# 若ACCOUNT表单不存在则创建一个
		if not self.cursor.fetchone():
			# 创建ACCOUNT表单
			self.cursor.execute(
				"""CREATE TABLE ACCOUNT (
					id TEXT,
					userName TEXT,
					avatarUrl TEXT,
					email TEXT,
					auth INTEGER
				)"""
			)
			self.conn.commit()
		
		self.closeDB()
	
	# 根据id查询账号
	def queryAccountById(self, id):
		self.openDB()

		self.cursor.execute("SELECT * FROM ACCOUNT WHERE id='{}'".format(id))
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

	# 添加账号信息
	def addAccount(self, account: Account):
		# 先查询id所指的账号是否存在
		# 不存在则添加，已存在则返回False报错
		if not self.queryAccountById(account.id):
			self.openDB()

			self.cursor.execute("INSERT INTO ACCOUNT VALUES ('{}', '{}', '{}', '{}', {})".format(account.id, account.userName, account.avatarUrl, account.email, account.auth))
			self.conn.commit()

			self.closeDB()
		
			return True
		
		else:
			return False

	# 根据id删除账号
	def removeAccountById(self, id):
		# 先查询id所指的账号是否存在
		# 存在则删除，不存在则返回False报错
		if self.queryAccountById(id):
			self.openDB()

			self.cursor.execute("DELETE FROM ACCOUNT WHERE id='{}'".format(id))
			self.conn.commit()

			self.closeDB()

			return True
		
		else:
			return False

	def updateAccountById(self, id, newAccoutInfo: Account):
		# 先查询id所指的账号是否存在
		# 存在则更新账号信息，不存在则返回False报错
		if self.queryAccountById(id):
			self.openDB()

			self.cursor.execute("UPDATE ACCOUNT SET userName='{}',avatarUrl='{}',email='{}',auth={} WHERE id = '{}'".format(newAccoutInfo.userName, newAccoutInfo.avatarUrl, newAccoutInfo.email, newAccoutInfo.auth, newAccoutInfo.id))
			self.conn.commit()

			self.closeDB()

			return True
		
		else:
			return False


def main():
	accountDB = AccountDB("./accoutDatabase.db")
	account = Account(id="stu001", userName="testAccount", avatarUrl="", email="xxx@kzoj.cn", auth=1)
	# print(accountDB.addAccount(account))
	# print(accountDB.queryAccountById("stu000"))
	# print(accountDB.queryAccountById("stu001"))
	# print(accountDB.removeAccountById("stu000"))

if __name__ == '__main__':
	main()