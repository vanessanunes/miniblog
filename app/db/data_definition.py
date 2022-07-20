# todas as coneectionssss
from datetime import datetime
from sqlalchemy import (Column, DateTime, ForeignKey, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, relationship
from app.settings import settings

engine = create_engine(settings.postgre_url, echo=True)


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, index=True, unique=True) #marcar como unique
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    post = relationship("Post", back_populates="post")


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime, default=datetime.utcnow())


class Follow(Base):
    __tablename__ = 'follow'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    follow_id = Column(Integer, ForeignKey("user.id"))


    
