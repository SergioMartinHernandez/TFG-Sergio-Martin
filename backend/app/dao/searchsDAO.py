from daoImpl import searchsDAOImpl
from sqlalchemy.orm import Session
import schemas

def search_tweets(query:str, search_id: int, db: Session):
    return searchsDAOImpl.search_tweets(query=query, search_id=search_id, db=db)

def search_user(username:str, search_id: int, db: Session):
    return searchsDAOImpl.search_user(username=username, search_id=search_id, db=db)

def create_user_search(search: schemas.SearchCreate, user_id: int, db: Session):
    return searchsDAOImpl.create_user_search(search=search, db=db)

def get_searchs(db: Session):
    return searchsDAOImpl.get_searchs(db=db)

def get_tweets_of_search(db: Session,search_id: int):
    return searchsDAOImpl.get_tweets_of_search(db=db, search_id=search_id)

def create_search_user_search(user_search: schemas.UserSearchCreate, search_id: int, db: Session):
    return searchsDAOImpl.create_search_user_search(db=db, users_search=user_search, search_id=search_id)

def create_search_tweet_search(tweet_search: schemas.TweetSearchCreate, search_id: int, db: Session):
    return searchsDAOImpl.create_search_tweet_search(tweet_search=tweet_search, search_id=search_id, db=db)

def get_tweet_searchs(db: Session):
    return searchsDAOImpl.get_tweet_searchs(db=db)

def get_tweet_by_id(tweetsearch_id: int, db: Session):
    return searchsDAOImpl.get_tweet_by_id(tweetsearch_id=tweetsearch_id, db=db)

def create_user_search(db: Session, search: schemas.SearchCreate, user_id: int):
    return searchsDAOImpl.create_user_search(user_id=user_id, search=search, db=db)

def get_user_searchs(db: Session):
    return searchsDAOImpl.get_user_searchs(db=db)

def get_user_of_search(db: Session, search_id: int):
    return searchsDAOImpl.get_user_of_search(db=db, search_id=search_id)