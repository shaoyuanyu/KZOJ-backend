#from .UserSys import router as user_router
#from .ProblemLibSys import router as problem_router
#from .SubmissionSys import router as submission_router

from . import UserSys, ProblemLibSys, SubmissionSys

user_router = UserSys.router
problem_router = ProblemLibSys.router
submission_router = SubmissionSys.router
