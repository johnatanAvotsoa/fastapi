from fastapi import FastAPI,Depends,HTTPException
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
app = FastAPI()

@app.get("/checkdb")
async def check_db(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1"))
        return {"status": "Database connection successful", "result": result.scalar()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")
