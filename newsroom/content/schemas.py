from ninja import Schema
from datetime import datetime
from typing import List, Optional



class AuthorSchema(Schema):
    id : int
    username: str
    email: str

    class Config:
        orm_mode = True

class CategorySchema(Schema):
    id: int
    name: str
    logo: Optional[str]
    parent_category: Optional[int]

    class Config:
        orm_mode = True

class CategoryNotFoundSchema(Schema):
    message: str

class TagsSchema(Schema):
    name: str

    class Config:
        orm_mode = True

class TagNotFoundSchema(Schema):
    message: str

class ArticleSchema(Schema):
    id: int
    title: str
    author: AuthorSchema
    category: Optional[CategorySchema]
    description: Optional[str]
    publish_date: Optional[datetime]
    tags: Optional[List[TagsSchema]]
    main_image: Optional[str]
    is_published: bool

    class Config:
        orm_mode = True

class ArticleNotFoundSchema(Schema):
    message: str
