from fastapi import Depends, APIRouter, HTTPException,Response, status
from fastapi.security import OAuth2PasswordRequestForm
import crud, schemas
from datetime import timedelta
from database import SessionLocal, engine
from starlette.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from dependencies import get_db, get_current_user, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token


router = APIRouter()

# Crea un nuevo usuario
@router.post("/signup", response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

# Inicia sesion en un usuario registrado
@router.post("/login", response_model=schemas.Token)
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
@router.get("/users/me", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(get_current_user)):
    return current_user

# Borra un usuario de la base de datos
@router.delete("/deleteUser/{user_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    crud.delete_user(db=db,user=user)
    return None

# Actualiza los campos cambiados de un usuarios que se encuentra en la base de datos
@router.patch("/updateUser", response_model=schemas.UserUpdate)
def update_user(
    updated_fields: schemas.UserUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user)
):
    user_id = current_user.id
    return crud.update_user(db, user_id, updated_fields)

# Recupera todos los usuarios de la base de datos
@router.get("/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# Recupera un usuario concreto de la base de datos
@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Recupera todos los usuarios buscados
@router.get("/usersearchs", response_model=list[schemas.UserSearch])
def read_user_searchs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usersearchs = crud.get_user_searchs(db, skip=skip, limit=limit)
    return usersearchs

# Recupera el usuario buscado en una busqueda concreta
@router.get("/search/user", response_model=schemas.UserSearch)
def get_user_of_search(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    search_id = current_user.searchs[-1].id
    user = crud.get_user_of_search(db, search_id=search_id)
    return user