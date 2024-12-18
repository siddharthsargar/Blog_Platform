from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from app.models import Post


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    posts: List["Post"] = []
    
    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    category_id: int


class Post(PostBase):
    id: int
    created_at: datetime
    author: User

    class Config:
        orm_mode = True


class Category(BaseModel):
    id: int
    name: str


    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    post_id: int


class Comment(CommentBase):
    id: int
    post: Post
    author: User

    class Config:
        orm_mode = True