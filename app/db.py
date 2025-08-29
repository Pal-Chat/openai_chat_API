from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import DATABASE_URL

# Create async engine with the database URL
engine = create_async_engine(DATABASE_URL, echo=False)

# Create async sessionmaker factory
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

# Base class for ORM models
Base = declarative_base()
