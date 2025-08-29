from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.db import Base

class User(Base):
    """
    ORM model representing a user in the system.

    Attributes:
        id (int): Primary key, unique user identifier.
        username (str): Unique username for login or identification.
        messages (List[Message]): One-to-many relationship; 
                    user's chat messages stored in the database.
    """
    __tablename__ = "users"

    # Primary key column - unique user ID
    id = Column(Integer, primary_key=True)

    # Username column - must be unique and indexed for fast lookup
    username = Column(String, unique=True, index=True)

    # Relationship to Message model; cascade deletes messages when user is deleted
    messages = relationship("Message", back_populates="user", cascade="all, delete-orphan")

class Message(Base):
    """
    ORM model representing a user message or query.

    Attributes:
        id (int): Primary key, unique message identifier.
        user_id (int): Foreign key referencing the User who sent the message.
        content (str): The text content of the user's message.
        user (User): The user relationship for easy access to the message sender.
    """
    __tablename__ = "messages"


    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    # Relationship back to User model for easy access from message to user
    user = relationship("User", back_populates="messages")
