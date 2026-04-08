from sqlalchemy.orm import declarative_base

from .config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)

SessionLocal = async_sessionmaker(
    bind=engine,    
    class_=AsyncSession,
    expire_on_commit=False)

Base = declarative_base()

async def get_db():
    async with SessionLocal() as session:
        yield session