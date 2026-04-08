
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel): 
    name:str
    email:str

class UserCreate(UserBase):
    password:str

class UserOut(UserBase):
    id:int
    created_at:datetime
    model_config = ConfigDict(from_attributes=True)

class UserUpdate(BaseModel):
    name:str | None = None
    email:str | None = None
    password:str | None = None