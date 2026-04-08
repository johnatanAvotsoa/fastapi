from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional
from typing import List
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"

class User(BaseModel) : 
    id : Optional[UUID] = uuid4()
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    gender : Gender
    Role : List[Role]