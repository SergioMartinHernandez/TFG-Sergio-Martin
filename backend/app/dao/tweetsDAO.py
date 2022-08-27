from daoImpl import tweetsDAOImpl
from sqlalchemy.orm import Session
import schemas

def save_tweet_user(tweet: schemas.TweetSavedCreate, user_id: int, db: Session):
    return tweetsDAOImpl.save_tweet_user(db, user_id=user_id, tweet=tweet)

def get_tweet_saved_by_id(tweetsaved_id: int, user_id:int, db: Session):
    return tweetsDAOImpl.get_tweet_saved_by_id(db, tweetsaved_id=tweetsaved_id, user_id=user_id)

def delete_tweet_user(tweet: schemas.TweetSearch, db: Session):
    return tweetsDAOImpl.delete_tweet_user(db=db, tweet=tweet)

def get_tweets_saved(db: Session, user_id: int):
    return tweetsDAOImpl.get_tweets_saved(db=db, user_id=user_id)