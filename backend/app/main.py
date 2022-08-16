from os import access
from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel
from passlib.context import CryptContext


from typing import Optional
import base64
from passlib.context import CryptContext
from datetime import datetime, timedelta


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




import crud, models, schemas, searchs
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

#AUTENTIFICACION

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "0442fceb275663041ca1a2d8be1c0ac5b07c650f7c433bc73176125e09f15b5e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class OAuth2PasswordBearerCookie(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: str = None,
        scopes: dict = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        header_authorization: str = request.headers.get("Authorization")
        cookie_authorization: str = request.cookies.get("Authorization")

        header_scheme, header_param = get_authorization_scheme_param(
            header_authorization
        )
        cookie_scheme, cookie_param = get_authorization_scheme_param(
            cookie_authorization
        )

        print("header_scheme")
        print(header_scheme)

        print("cookie_scheme")
        print(cookie_scheme)

        if header_scheme.lower() == "bearer":
            authorization = True
            scheme = header_scheme
            param = header_param

        elif cookie_scheme.lower() == "bearer":
            authorization = True
            scheme = cookie_scheme
            param = cookie_param

        else:
            authorization = False

        print(authorization)
        
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"
                )
            else:
                return None
        return param

oauth2_scheme = OAuth2PasswordBearerCookie(tokenUrl="login", scheme_name="JWT")

# Se declara la aplicacion y se configura
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependencia de base de datos
def get_db(request: Request):
    return request.state.db

# Borra un usuario de la base de datos
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    return crud.delete_user(db=db,user=user)

# Actualiza los campos cambiados de un usuarios que se encuentra en la base de datos
@app.patch("/users/{user_id}", response_model=schemas.UserUpdate)
def update_user(
    user_id: int,
    updated_fields: schemas.UserUpdate,
    db: Session = Depends(get_db),
):
    return crud.update_user(db, user_id, updated_fields)

# Recupera todos los usuarios de la base de datos
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# Recupera un usuario concreto de la base de datos
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Crea una busqueda para un usuario
@app.post("/users/{user_id}/search/", response_model=schemas.Search)
def create_search_for_user(
    user_id: int, search: schemas.SearchCreate, db: Session = Depends(get_db)
):
    searchquery = crud.create_user_search(db=db, search=search, user_id=user_id)
    if search.type == "tweet":
        # hacer busqueda de TweetSearch
        searchs.search_tweets(db=db, query=searchquery.title, search_id=searchquery.id)
    else:
        # hacer busqueda de usertweet
        searchs.search_user(db=db, username=searchquery.title, search_id=searchquery.id)
    return searchquery

# Recupera todas las busquedas realizadas
@app.get("/searchs/", response_model=list[schemas.Search])
def read_searchs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    searchs = crud.get_searchs(db, skip=skip, limit=limit)
    return searchs

# Recupera los tweets buscados en una busqueda concreta
@app.get("/{search_id}/tweets", response_model=list[schemas.TweetSearch])
def get_tweets_of_search(search_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tweets = crud.get_tweets_of_search(db, skip=skip, limit=limit, search_id=search_id)
    return tweets

# Guarda el tweet en el perfil del usuario
@app.post("/{user_id}/savetweet/{tweet_id}", response_model=list[schemas.TweetSearch])
def save_tweet_user(user_id: int, tweet_id: int, db: Session = Depends(get_db)):
    tweet = crud.get_tweet_by_id(db, tweetsearch_id=tweet_id)
    user = crud.get_user(db, user_id)
    tweets_saved = crud.save_tweet_user(db, user=user, tweet=tweet)
    return tweets_saved

# Elimina el tweet del perfil del usuario
@app.delete("/{user_id}/deletetweet/{tweet_id}", response_model=list[schemas.TweetSearch])
def delete_tweet_user(user_id: int, tweet_id: int, db: Session = Depends(get_db)):
    tweet = crud.get_tweet_by_id(db, tweetsearch_id=tweet_id)
    user = crud.get_user(db, user_id)
    tweets_saved = crud.delete_tweet_user(db, user=user, tweet=tweet)
    return tweets_saved
    
# CREO QUE NO SE UTILIZA PARA NADA
@app.post("/users/{search_id}/tweetsearch/", response_model=schemas.TweetSearch)
def create_tweet_search_for_search(
    search_id: int, tweet_search: schemas.TweetSearchCreate, db: Session = Depends(get_db)
):
    return crud.create_search_tweet_search(db=db, tweet_search=tweet_search, search_id=search_id)

# Recupera todos los tweets buscados
@app.get("/tweetssearchs/", response_model=list[schemas.TweetSearch])
def read_tweet_searchs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tweetsearchs = crud.get_tweet_searchs(db, skip=skip, limit=limit)
    return tweetsearchs

# Recupera un tweet buscado
@app.get("/tweetsearch/{tweetsearch_id}", response_model=schemas.TweetSearch)
def get_tweet_by_id(tweetsearch_id: int,db: Session = Depends(get_db)):
    db_tweet = crud.get_tweet_by_id(db, tweetsearch_id=tweetsearch_id)
    if db_tweet is None:
        raise HTTPException(status_code=404, detail="Tweet not found")
    return db_tweet

# CREO QUE NO SE UTILIZA PARA NADA
@app.post("/users/{search_id}/usersearch/", response_model=schemas.UserSearch)
def create_user_search_for_search(
    search_id: int, user_search: schemas.UserSearchCreate, db: Session = Depends(get_db)
):
    return crud.create_user_search(db=db, user_search=user_search, search_id=search_id)

# Recupera todos los usuarios buscados
@app.get("/usersearchs/", response_model=list[schemas.UserSearch])
def read_user_searchs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usersearchs = crud.get_user_searchs(db, skip=skip, limit=limit)
    return usersearchs

# Recupera el usuario buscado en una busqueda concreta
@app.get("/{search_id}/user", response_model=schemas.UserSearch)
def get_user_of_search(search_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_of_search(db, search_id=search_id)
    return user

# Crea un nuevo usuario
@app.post("/signup", response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)






pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Funciones para la autentificacion del usuario
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(db, username: str, password: str):
    user = crud.get_user_dict(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    print(password,user.hashed_password)
    print("entrado en constrasena verificada")
    return user


# Función de utilidad para generar un nuevo token de acceso
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    print(expire)
    to_encode.update({"exp": expire})
    print(to_encode)
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Funcion para obtener el usuario actual
async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# Inicia sesion en un usuario registrado
# @app.post("/login", response_model=schemas.Token)
# async def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     print("usuario en el post /login")
#     print(user.username)
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username, "type": "access_token"}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}


@app.post("/login", response_model=schemas.Token)
async def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)
    content = {"message": "You've successfully logged in. Welcome back!"}
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False,
    ) 
    return response

# Obtiene el usuario que esta utilizando la aplicacion
@app.get("/users/me/", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(get_current_user)):
    return current_user

