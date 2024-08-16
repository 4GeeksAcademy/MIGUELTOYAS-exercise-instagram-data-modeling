import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50))
    email = Column(String(250), unique=True, nullable=False)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email
        }

class Follower(Base):
    __tablename__ = 'Follower'

    user_from_id = Column(Integer, ForeignKey(User.id), primary_key=True, nullable=False)
    user_to_id = Column(Integer, ForeignKey(User.id), primary_key=True, nullable=False)

    def to_dict(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id
        }

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

    def to_dict(self):
        return {
            "post_id": self.post_id,
            "user_id": self.user_id
        }

class Media(Base):
    __tablename__ = 'Media'

    id = Column(Integer, primary_key=True)
    type = Column(Enum('photo', 'video', 'reel'), nullable=False)
    URL = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey(Post.id), nullable=False)

    def to_dict(self):
        return {
            "media_id": self.media_id,
            "type": self.type,
            "URL": self.URL,
            "post_id": self.post_id
        }

class Comment(Base):
    __tablename__ = 'Comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(400), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    post_id = Column(Integer, ForeignKey(Post.id), nullable=False)

    def to_dict(self):
        return {
            "comment_id": self.comment_id,
            "comment_text": self.comment_text,
            "author_id": self.user_id,
            "post_id": self.post_id
        }

# Dibujar el diagrama a partir de la base de datos SQLAlchemy
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
