from pydantic import BaseModel
from typing import List,Optional

class BlogBase(BaseModel):
    title:str
    body:str
    

class Blog(BlogBase):
    class Config():
        orm_mode=True


class User(BaseModel):
    name:str
    email:str
    password:str



class showUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog]=[]
    class Config():
        orm_mode=True


class showBlog(BaseModel):
    title:str
    body:str
    creator:Optional[showUser]=None

    class Config():
        orm_mode=True


class Login(BaseModel):
    username:str
    password:str
    class Config():
        orm_mode=True

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    email: Optional[str]=None