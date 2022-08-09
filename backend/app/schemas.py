from datetime import date, datetime
from pydantic import BaseModel, EmailStr
from typing import List, Optional

#FALTAN HACER UPDATE USER, DELETE USER, DELETE TWEETS SEARCH, DELETE USER SEARCHS

# Creacion del objeto
class TweetSearchBase(BaseModel):
    text: str
    author_id: int
    created_at: str
    retweet_count: int
    reply_count: int
    like_count: int
    quote_count: int
    lang: str
    source: str


class TweetSearchCreate(TweetSearchBase):
    pass

# Recuperacion del objeto del API ya añadiendo los campos que no se sabian en la creacion
class TweetSearch(TweetSearchBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True



class UserSearchBase(BaseModel):
    created_at: str
    description: str
    location: str
    name: str
    profile_image_url: str
    followers_count: int
    following_count: int
    listed_count: int
    tweet_count: int
    username: str
    verified: bool


class UserSearchCreate(UserSearchBase):
    pass


class UserSearch(UserSearchBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class SearchBase(BaseModel):
    title: str
    type: str


class SearchCreate(SearchBase):
    pass


class Search(SearchBase):
    id: int
    owner_id: int

    tweetSearch: list[TweetSearch] = []
    userSearch: list[UserSearch] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    created_at: str
    searchs: list[Search] = []
    #tweetsaves: list[TweetSearch] = []

    class Config:
        orm_mode = True

class UserInDB(UserBase):
    hashed_password: str


class UserUpdate(BaseModel):
    password: Optional[str]

    class Config:
        orm_mode = True

# PARA LA AUTENTIFICACION 
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
