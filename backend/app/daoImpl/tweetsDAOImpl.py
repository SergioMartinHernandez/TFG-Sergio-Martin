from dependencies import get_db, get_current_user
from fastapi import Depends
from sqlalchemy.orm import Session
import tweepy
import schemas, models

# Guarda un tweet en el perfil del usuario
def save_tweet_user(db: Session, tweet: schemas.TweetSavedCreate, user_id: int):
    db_tweet_saved = models.TweetSaved(url=tweet.url, text=tweet.text, author=tweet.author,
    created_at=tweet.created_at, retweet_count=tweet.retweet_count, reply_count=tweet.reply_count, like_count=tweet.like_count, quote_count=tweet.quote_count,
    lang=tweet.lang, source=tweet.source, owner_id=user_id)
    db.add(db_tweet_saved)
    db.commit()
    db.refresh(db_tweet_saved)
    return db_tweet_saved

# Obtiene un tweet guardado dado su id
def get_tweet_saved_by_id(db: Session, tweetsaved_id: int, user_id:int):
    return db.query(models.TweetSaved).filter(models.TweetSaved.id == tweetsaved_id).filter(models.TweetSaved.owner_id == user_id).first()

# Elimina un tweet en el perfil del usuario
def delete_tweet_user(db: Session, tweet: schemas.TweetSearch):
    db.delete(tweet)
    db.commit()

# Obtiene los tweets guardados del usuario
def get_tweets_saved(db: Session, user_id: int):
    return db.query(models.TweetSaved).filter(models.TweetSaved.owner_id == user_id).all()
