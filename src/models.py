import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    password = Column(String(50), nullable=True, unique=True)
    email = Column(String(50), nullable=True)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    img = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)
    post = relationship(Post)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String(200), nullable=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e