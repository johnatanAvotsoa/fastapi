from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,text 

DATABASE_URL = "mysql+pymysql://root:@localhost/testdb"

engine = create_engine(DATABASE_URL, echo=True, future=True, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()