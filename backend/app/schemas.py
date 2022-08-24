from datetime import date, datetime
from pydantic import BaseModel, EmailStr
from typing import List, Optional

from pydantic import BaseModel

from fastapi import Depends, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm, OAuth2
from fastapi.security.base import SecurityBase
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.utils import get_openapi

from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, Response, JSONResponse
from starlette.requests import Request


# Modelo Pydantic de Tweet buscado 
class TweetSearchBase(BaseModel):
    url: str
    text: str
    author: str
    created_at: date
    retweet_count: int
    reply_count: int
    like_count: int
    quote_count: int
    lang: str
    source: str

# Modelo Pydantic de creacion Tweet buscado
class TweetSearchCreate(TweetSearchBase):
    pass

# Recuperacion del objeto del API ya añadiendo los campos que no se sabian en la creacion
class TweetSearch(TweetSearchBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True



# Modelo Pydantic de usuario buscado 
class UserSearchBase(BaseModel):
    created_at: date
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

# Modelo Pydantic de creacion usuario buscado
class UserSearchCreate(UserSearchBase):
    pass

# Recuperacion del objeto del API ya añadiendo los campos que no se sabian en la creacion
class UserSearch(UserSearchBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# Modelo Pydantic de Tweet guardado 
class TweetSavedBase(BaseModel):
    url: str
    text: str
    author: str
    created_at: date
    retweet_count: int
    reply_count: int
    like_count: int
    quote_count: int
    lang: str
    source: str

# Modelo Pydantic de creacion Tweet guardado
class TweetSavedCreate(TweetSavedBase):
    pass

# Recuperacion del objeto del API ya añadiendo los campos que no se sabian en la creacion
class TweetSaved(TweetSavedBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# Modelo Pydantic de busqueda 
class SearchBase(BaseModel):
    title: str
    type: str

# Modelo Pydantic de creacion de busqueda
class SearchCreate(SearchBase):
    pass

# Recuperacion del objeto del API ya añadiendo los campos que no se sabian en la creacion
class Search(SearchBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# Modelo Pydantic de usuario
class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr

# Modelo Pydantic de creacion de usuario
class UserCreate(UserBase):
    password: str

# Recuperacion del objeto del API ya añadiendo los campos que no se sabian en la creacion
class User(UserBase):
    id: int
    created_at: str
    image: str
    searchs: list[Search] = []
    tweetsaved: list[TweetSearch] = []

    class Config:
        orm_mode = True

# Modelo Pydantic de usuario con contraseña hash
class UserInDB(UserBase):
    hashed_password: str

# Modelo Pydantic de actualizacion de usuario
class UserUpdate(BaseModel):
    oldpassword: Optional[str]
    password: Optional[str]
    image: Optional[str]

    class Config:
        orm_mode = True


# Modelo Pydantic para la autentificacion de los usuarios 
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
