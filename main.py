from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import time

from src.services import user_router, problem_router, submission_router

def main():
	app = FastAPI()

	# 允许跨域请求
	app.add_middleware(
		CORSMiddleware,
		allow_origins=["*"],
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)

	app.include_router(router=user_router, prefix='/user')
	app.include_router(router=problem_router, prefix='/problem')
	app.include_router(router=submission_router, prefix='/submission')

	uvicorn.run(app, host='127.0.0.1', port=8081)

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(e)
		with open('error_log.txt', 'a', encoding='utf-8') as f:
			f.write("{}: \n{}\n\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), e))
			f.close()