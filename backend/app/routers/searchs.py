from sqlalchemy.orm import Session
import schemas
from fastapi import Depends, APIRouter, HTTPException,Response, status

from dependencies import get_db, get_current_user
import daoImpl.searchsDAOImpl as se


router = APIRouter()
    

# Crea una busqueda para un usuario
@router.post("/user/search", response_model=schemas.Search)
def create_search_for_user(search: schemas.SearchCreate, current_user: schemas.User = Depends(get_current_user),db: Session = Depends(get_db),):
    searchquery = se.searchsDAOImpl.create_user_search(search=search, user_id=current_user.id, db=db)
    if search.type == "Tweet":
        # hacer busqueda de TweetSearch
        se.searchsDAOImpl.search_tweets(query=searchquery.title, search_id=searchquery.id, start_date=searchquery.start_date, end_date=searchquery.end_date, num_tweets=searchquery.num_tweets, db=db)
    else:
        # hacer busqueda de usertweet
        se.searchsDAOImpl.search_user(username=searchquery.title, search_id=searchquery.id, start_date=searchquery.start_date, end_date=searchquery.end_date, num_tweets=searchquery.num_tweets, db=db)
    return searchquery


# Recupera todas las busquedas realizadas
@router.get("/searchs", response_model=list[schemas.Search])
def read_searchs(db: Session = Depends(get_db)):
    searchs = se.searchsDAOImpl.get_searchs(db=db)
    return searchs

# Borra una busqueda de un usuario
@router.delete("/user/search/{search_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_search_user(search_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    search = se.searchsDAOImpl.get_search_by_id(db=db, search_id=search_id, user_id=current_user.id)
    se.searchsDAOImpl.delete_search(db=db, search=search)
    return None

# Recupera los tweets buscados en una busqueda concreta
@router.get("/search/tweets", response_model=list[schemas.TweetSearch])
def get_tweets_of_search(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    search_id = current_user.searchs[-1].id
    tweets = se.searchsDAOImpl.get_tweets_of_search(db=db,search_id=search_id)
    return tweets


# Crea una nueva busqueda de tweets
@router.post("/users/{search_id}/tweetsearch", response_model=schemas.TweetSearch)
def create_tweet_search_for_search(search_id: int, tweet_search: schemas.TweetSearchCreate, db: Session = Depends(get_db)):
    return se.searchsDAOImpl.create_search_tweet_search(tweet_search=tweet_search, search_id=search_id, db=db)


# Recupera todos los tweets buscados
@router.get("/tweetssearchs", response_model=list[schemas.TweetSearch])
def read_tweet_searchs(db: Session = Depends(get_db)):
    tweetsearchs = se.searchsDAOImpl.get_tweet_searchs(db=db)
    return tweetsearchs


# Recupera un tweet buscado
@router.get("/tweetsearch/{tweetsearch_id}", response_model=schemas.TweetSearch)
def get_tweet_by_id(tweetsearch_id: int, db: Session = Depends(get_db)):
    db_tweet = se.searchsDAOImpl.get_tweet_by_id(tweetsearch_id=tweetsearch_id, db=db)
    if db_tweet is None:
        raise HTTPException(status_code=404, detail="Tweet not found")
    return db_tweet

# Crea una nueva busqueda de usuario
@router.post("/users/{search_id}/usersearch", response_model=schemas.UserSearch)
def create_user_search_for_search(search_id: int, user_search: schemas.UserSearchCreate, db: Session = Depends(get_db),):
    return se.searchsDAOImpl.create_user_search(user_search=user_search, search_id=search_id, db=db)


# Recupera todos los usuarios buscados
@router.get("/usersearchs", response_model=list[schemas.UserSearch])
def read_user_searchs(db: Session = Depends(get_db)):
    usersearchs = se.searchsDAOImpl.get_user_searchs(db=db)
    return usersearchs


# Recupera el usuario buscado en una busqueda concreta
@router.get("/search/user", response_model=schemas.UserSearch)
def get_user_of_search(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    search_id = current_user.searchs[-1].id
    user = se.searchsDAOImpl.get_user_of_search(db=db, search_id=search_id)
    return user