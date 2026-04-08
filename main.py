from fastapi import FastAPI
from typing import List
from models import User, UserUpdate
from uuid import UUID
from fastapi import HTTPException
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
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/api/v1/updateuser/{user_id}")
async def update_user(user_id : UUID, user_update : UserUpdate) :
    for user in db : 
        if user.id == user_id : 
            if user_update.first_name is not None : 
                user.first_name = user_update.first_name
            if user_update.middle_name is not None : 
                user.middle_name = user_update.middle_name
            if user_update.last_name is not None : 
                user.last_name = user_update.last_name
            return {"message" : "User updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")