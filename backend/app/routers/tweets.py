from fastapi import Depends, APIRouter, Response, status
from sqlalchemy.orm import Session
import schemas
from dependencies import get_db, get_current_user
#from daoImpl import searchsDAOImpl, tweetsDAOImpl
import daoImpl.tweetsDAOImpl as tw
import daoImpl.searchsDAOImpl as se


router = APIRouter()

# Guarda el tweet en el perfil del usuario
# @router.post("/user/savetweet/{tweet_id}", response_model=schemas.TweetSaved)
# def save_tweet_user(tweet_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
#     tweet = crud.get_tweet_by_id(db, tweetsearch_id=tweet_id)
#     tweets_saved = crud.save_tweet_user(db, user_id=current_user.id, tweet=tweet)
#     return tweets_saved

# DAO
@router.post("/user/savetweet/{tweet_id}", response_model=schemas.TweetSaved)
def save_tweet_user(tweet_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    tweet = se.searchsDAOImpl.get_tweet_by_id(db=db, tweetsearch_id=tweet_id)
    tweets_saved = tw.tweetsDAOImpl.save_tweet_user(db=db, user_id=current_user.id, tweet=tweet)
    return tweets_saved

# Elimina el tweet del perfil del usuario
# @router.delete("/user/deletetweet/{tweet_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
# def delete_tweet_user(tweet_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
#     tweet = tweetsDAO.get_tweet_saved_by_id(db=db, tweetsaved_id=tweet_id, user_id=current_user.id)
#     tweets_saved = tweetsDAO.delete_tweet_user(db=db, tweet=tweet)
#     return tweets_saved

#DAO
@router.delete("/user/deletetweet/{tweet_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_tweet_user(tweet_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    tweet = tw.tweetsDAOImpl.get_tweet_saved_by_id(db=db, tweetsaved_id=tweet_id, user_id=current_user.id)
    tw.tweetsDAOImpl.delete_tweet_user(db=db, tweet=tweet)
    return None

# Recupera los tweets guardados del usuario
# @router.get("/user/tweetssaved", response_model=list[schemas.TweetSaved])
# def get_tweets_saved(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
#     tweetsaved = tweetsDAO.get_tweets_saved(db=db, user_id=current_user.id)
#     return tweetsaved

#DAO
@router.get("/user/tweetssaved", response_model=list[schemas.TweetSaved])
def get_tweets_saved(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    tweetsaved = tw.tweetsDAOImpl.get_tweets_saved(db=db, user_id=current_user.id)
    return tweetsaved