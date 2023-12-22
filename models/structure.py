from typing import Annotated, Union
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(default="lastname", min_length=1, max_length=20)
    age: Annotated[Union[int, None], Field(default=100, ge=5, lt=150)] = None
    id: Annotated[Union[int, None], Field(default=100, ge=1, lt=150)] = None

class Main_User(User):
    password: Annotated[Union[str, None], Field(max_length=200, min_length=8)] = None

#информация о программе
class New_Respons(BaseModel):
    message: str