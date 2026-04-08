from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from core.database import get_db
from . import crud, schemas

router = APIRouter()

@router.post("/users/", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await crud.get_user_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = await crud.create_user(db, user_in)
    return new_user

@router.get("/", response_model=List[schemas.UserOut])
async def read_users(
    skip: int = 0, 
    limit: int = 100, 
    db: AsyncSession = Depends(get_db)
):

    users = await crud.get_users(db, skip=skip, limit=limit)
    return users