from enum import Enum

class AuthLevel(Enum):
	GUEST = -1
	USER = 0
	ADMIN = 1
