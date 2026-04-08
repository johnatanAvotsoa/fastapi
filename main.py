from fastapi import FastAPI
from typing import List
from models import User
from uuid import UUID

app = FastAPI()

db : List[User] = [
    User(first_name="John", middle_name="Doe", last_name="Smith", gender="male", Role=["admin"]),
    User(first_name="Jane", middle_name=None, last_name="Doe", gender="female", Role=["user"]),
    User(first_name="Alice", middle_name="Bob", last_name="Smith", gender="female", Role=["admin", "user"])
]

@app.get("/api/v1/user")
def fetch_users() -> List[User] :
    return db

@app.post("/api/v1/adduser")
def add_user(user : User) -> User :
    db.append(user)
    return user

@app.delete("/api/v1/deleteuser/{user_id}")

async def delete_user(user_id : UUID): 
    for user in db : 
        if user.id == user_id : 
            db.remove(user)
            return {"message" : "User deleted successfully"}
    return {"message" : "User not found"}