from fastapi import FastAPI,Depends,HTTPException
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
import models,schemas
from database import Base, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/checkdb")
async def check_db(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1"))
        return {"status": "Database connection successful", "result": result.scalar()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

@app.post("/customers/")
async def create_customer(customer:schemas.CustomerCreate, db:Session = Depends(get_db)):
    db_customer = models.Customer(name=customer.name, email=customer.email)
    try : 
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return db_customer
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating customer: {str(e)}")

