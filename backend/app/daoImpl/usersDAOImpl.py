from fastapi import Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import schemas, models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Crea un usuario y lo añade a la base de datos
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, first_name=user.first_name, last_name=user.last_name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Obtiene un diccionario de usuarios
def get_user_dict(db, username: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is not None:
        user_dict = user.__dict__
        return schemas.UserInDB(**user_dict)


# Obtiene un usuario en base a su nombre de usuario
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Obtiene un usuario dado su id
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Borra un usuario de la base de datos
def delete_user(db: Session, user: schemas.User):
    db.delete(user)
    db.commit()


# Actualiza los campos de un usuario en la base de datos
def update_user(db: Session, user_id: int, updated_fields: schemas.UserUpdate):
    db_user = get_user(db, user_id)
    if updated_fields.password is not None:
        if pwd_context.verify(updated_fields.oldpassword, db_user.hashed_password):
            db_user.hashed_password = pwd_context.hash(updated_fields.password)
    if updated_fields.image is not None:
        db_user.image = updated_fields.image
    db.commit()
    db.refresh(db_user)
    return db_user

# Obtiene todos los usuarios
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()