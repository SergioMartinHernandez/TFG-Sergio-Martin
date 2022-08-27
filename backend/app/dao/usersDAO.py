from daoImpl import usersDAOImpl
from sqlalchemy.orm import Session
import schemas

def get_user_by_username(username: str, db: Session):
    return usersDAOImpl.get_user_by_username(db=db, username=username)

def create_user(user: schemas.UserCreate, db: Session):
    return usersDAOImpl.create_user(db=db, user=user)

def get_user_dict(username: str, db: Session):
    return usersDAOImpl.get_user_dict(db=db, username=username)

def get_user(user_id: int, db: Session):
    return usersDAOImpl.get_user(db=db, user_id=user_id)

def delete_user(db: Session, user: schemas.User):
    return usersDAOImpl.delete_user(db=db,user=user)

def read_user(user_id: int, db: Session):
    return usersDAOImpl.get_user(db=db, user_id=user_id)

def update_user(user_id: int, updated_fields: schemas.UserUpdate, db: Session):
    return usersDAOImpl.update_user(db=db, user_id = user_id, updated_fields=updated_fields)

def get_users(db: Session):
    return usersDAOImpl.get_users(db=db)

