from sqlalchemy.orm import Session
import bcrypt
from sqlalchemy import update
from security import pwd_context
import requests
import json

import models, schemas

#FALTAN HACER UPDATE USER, DELETE USER, DELETE TWEETS SEARCH, DELETE USER SEARCHS

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# AÑADIDO
def get_user_dict(db: Session, username: str):
    #if db.query(models.User).filter(models.User.username == username).first() not null:
        #user_dict = db[username]
        #return schemas.UserInDB(**user_dict)
    user = db.query(models.User).filter(models.User.username == username).first()
    return user


# def get_user_me_dict(db: Session, username: str):
#     if username in db:
#         user_dict = db[username]
#         return schemas.User(**user_dict)


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, first_name=user.first_name, last_name=user.last_name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, updated_fields: schemas.UserUpdate):
    db_user = get_user(db, user_id)
    db_user.hashed_password = pwd_context.hash(updated_fields.password)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user: schemas.User):
    db.delete(user)
    db.commit()



def get_searchs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Search).offset(skip).limit(limit).all()


def create_user_search(db: Session, search: schemas.SearchCreate, user_id: int):
    db_search = models.Search(**search.dict(), owner_id=user_id)
    db.add(db_search)
    db.commit()
    db.refresh(db_search)
    return db_search



def get_tweet_searchs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TweetSearch).offset(skip).limit(limit).all()


def create_search_tweet_search(db: Session, tweet_search: schemas.TweetSearchCreate, search_id: int):
    #db_tweet_search = models.TweetSearch(**tweet_search.dict(), owner_id=search_id)
    db_tweet_search = models.TweetSearch(**tweet_search, owner_id=search_id)
    db.add(db_tweet_search)
    db.commit()
    db.refresh(db_tweet_search)
    return db_tweet_search


def get_user_searchs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UserSearch).offset(skip).limit(limit).all()


def create_search_user_search(db: Session, user_search: schemas.UserSearchCreate, search_id: int):
    db_user_search = models.UserSearch(**user_search.dict(), owner_id=search_id)
    db.add(db_user_search)
    db.commit()
    db.refresh(db_user_search)
    return db_user_search

