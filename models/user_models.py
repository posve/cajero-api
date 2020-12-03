from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str

class UserOut():
    username: str
    balance: int