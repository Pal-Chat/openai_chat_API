from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import DATABASE_URL

# Create an asynchronous SQLAlchemy engine connected to the specified database URL.
# This engine supports async operations to interact with the database efficiently
engine = create_async_engine(DATABASE_URL, echo=False)

# Create an async session factory.
# Sessions provide the interface for all ORM database operations, supporting async methods.
async_session = sessionmaker(
    engine,
    expire_on_commit=False,  # Prevents objects from being expired after commit, so they remain accessible.
    class_=AsyncSession, # Uses AsyncSession class for async DB interactions.
)

# Base class for all ORM models to inherit from.
# Contains metadata and ORM configuration shared across your models.
Base = declarative_base()
