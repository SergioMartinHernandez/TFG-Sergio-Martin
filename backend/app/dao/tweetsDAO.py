#from daoImpl import tweetsDAOImpl
from sqlalchemy.orm import Session
import schemas

class TweetsDAO:
    def save_tweet_user(tweet: schemas.TweetSavedCreate, user_id: int, db: Session):
        pass

    def get_tweet_saved_by_id(tweetsaved_id: int, user_id:int, db: Session):
        pass

    def delete_tweet_user(tweet: schemas.TweetSearch, db: Session):
        pass

    def get_tweets_saved(db: Session, user_id: int):
        pass