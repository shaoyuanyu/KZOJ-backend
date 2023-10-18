from dataclasses import dataclass

@dataclass
class Account():
    id: str
    userName: str
    avatarUrl: str
    email: str
    auth: int