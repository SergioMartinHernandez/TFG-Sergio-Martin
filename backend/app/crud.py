from sqlalchemy.orm import Session
import bcrypt
from sqlalchemy import update
from security import pwd_context
import requests
import json

import models, schemas

# Obtiene un usuario dado su id
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Obtiene un usuario en base a su nombre de usuario
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Obtiene todos los usuarios
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# Obtiene un diccionario de usuarios
# def get_user_dict(db: Session, username: str):
#     #if db.query(models.User).filter(models.User.username == username).first() not null:
#         #user_dict = db[username]
#         #return schemas.UserInDB(**user_dict)
#     user = db.query(models.User).filter(models.User.username == username).first()
#     return user
def get_user_dict(db, username: str):
    if db.query(models.User).filter(models.User.username == username).first() is not None:
        user_dict = db[username]
        return schemas.UserInDB(**user_dict)


# def get_user_me_dict(db: Session, username: str):
#     if username in db:
#         user_dict = db[username]
#         return schemas.User(**user_dict)

# Crea un usuario y lo añade a la base de datos
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, first_name=user.first_name, last_name=user.last_name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Actualiza los campos de un usuario en la base de datos
def update_user(db: Session, user_id: int, updated_fields: schemas.UserUpdate):
    db_user = get_user(db, user_id)
    if updated_fields.password is not None:
        db_user.hashed_password = pwd_context.hash(updated_fields.password)
    if updated_fields.image is not None:
        db_user.image = updated_fields.image
    db.commit()
    db.refresh(db_user)
    return db_user

# Borra un usuario de la base de datos
def delete_user(db: Session, user: schemas.User):
    db.delete(user)
    db.commit()

# Obtiene todas las busquedas 
def get_searchs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Search).offset(skip).limit(limit).all()

# Obtiene los tweets de una busqueda
def get_tweets_of_search(db: Session, search_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.TweetSearch).filter(models.TweetSearch.owner_id == search_id).offset(skip).limit(limit).all()

# Crea una busqueda para un usuario
def create_user_search(db: Session, search: schemas.SearchCreate, user_id: int):
    db_search = models.Search(**search.dict(), owner_id=user_id)
    db.add(db_search)
    db.commit()
    db.refresh(db_search)
    return db_search

# Obtiene los tweets buscados
def get_tweet_searchs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TweetSearch).offset(skip).limit(limit).all()

# Obtiene un tweet dado su id
def get_tweet_by_id(db: Session, tweetsearch_id: int):
    return db.query(models.TweetSearch).filter(models.TweetSearch.id == tweetsearch_id).first()

# Guarda un tweet en el perfil del usuario
def save_tweet_user(db: Session, tweet: schemas.TweetSearch, user: schemas.User):
    user.tweets_saved.append(tweet)
    #user.tweets_saved.append("hola")
    print(user.tweets_saved[0].text)
    db.commit()
    db.refresh(user)
    return user.tweets_saved

# Elimina un tweet en el perfil del usuario
def delete_tweet_user(db: Session, tweet: schemas.TweetSearch, user: schemas.User):
    for tweets in user.tweets_saved:
        if tweets.id == tweet.id:
            user.tweets_saved.remove(tweets)
    db.commit()
    db.refresh(user)
    return user.tweets_saved

# Guarda un tweet de una busqueda en la base de datos
def create_search_tweet_search(db: Session, tweet_search: schemas.TweetSearchCreate, search_id: int):
    #db_tweet_search = models.TweetSearch(**tweet_search.dict(), owner_id=search_id)
    db_tweet_search = models.TweetSearch(**tweet_search, owner_id=search_id)
    db.add(db_tweet_search)
    db.commit()
    db.refresh(db_tweet_search)
    return db_tweet_search

# Obtiene las busquedas de usuarios
def get_user_searchs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UserSearch).offset(skip).limit(limit).all()

# Obtiene el usuario buscado de una busqueda
def get_user_of_search(db: Session, search_id: int):
    return db.query(models.UserSearch).filter(models.UserSearch.owner_id == search_id).first()

# Guarda un usuario buscado en la base de datos
def create_search_user_search(db: Session, user_search: schemas.UserSearchCreate, search_id: int):
    db_user_search = models.UserSearch(**user_search, owner_id=search_id)
    db.add(db_user_search)
    db.commit()
    db.refresh(db_user_search)
    return db_user_search

