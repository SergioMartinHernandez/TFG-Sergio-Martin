from sqlalchemy.orm import Session
import schemas
from fastapi import Depends, APIRouter, HTTPException

from dependencies import get_db, get_current_user
import daoImpl.searchsDAOImpl as se


router = APIRouter()

# BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAPwbewEAAAAAFchVqp4fuXveeBPBiewYordtRuQ%3DVjQTaili6wXSzvvVYont62VrQyEhLxoEqKCIgljjNx6h9bbZKB";

# def search_tweets(db: Session, query:str, search_id: int):
#     query = query + " is:verified"
#     client = tweepy.Client(bearer_token=BEARER_TOKEN)
#     tweets = client.search_recent_tweets(query=query, tweet_fields=['text','author_id','created_at','public_metrics','lang','source'],user_fields=['username'], expansions='author_id', max_results=10)

#     users = {u["id"]: u for u in tweets.includes['users']}
#     tweetssearch = {}
#     for tweet in tweets.data:
#         if users[tweet.author_id]:
#             user = users[tweet.author_id]
#             tweetssearch['url'] = 'https://twitter.com/{}/status/{}'.format(user.username, tweet['id'])
#             tweetssearch["text"] = tweet.text
#             tweetssearch["author"] = user.username
#             tweetssearch["created_at"] = tweet.created_at
#             tweetssearch["retweet_count"] = tweet.public_metrics["retweet_count"]
#             tweetssearch["reply_count"] = tweet.public_metrics["reply_count"]
#             tweetssearch["like_count"] = tweet.public_metrics["like_count"]
#             tweetssearch["quote_count"] = tweet.public_metrics["quote_count"]
#             tweetssearch["lang"] = tweet.lang
#             tweetssearch["source"] = tweet.source
#             crud.create_search_tweet_search(db, tweetssearch, search_id)
    


# def search_user(db: Session, username:str, search_id: int):
#     username=username.replace(" ", "")
#     client = tweepy.Client(bearer_token=BEARER_TOKEN)
#     user = client.get_user(username=username,user_fields=['created_at','description','location','name','profile_image_url','public_metrics','username','verified'])
#     userssearch = {}
    
#     userssearch["created_at"] = user.data.created_at
#     userssearch["description"] = user.data.description
#     userssearch["location"] = user.data.location
#     userssearch["name"] = user.data.name
#     userssearch["profile_image_url"] = user.data.profile_image_url
#     userssearch["followers_count"] = user.data.public_metrics["followers_count"]
#     userssearch["following_count"] = user.data.public_metrics["following_count"]
#     userssearch["listed_count"] = user.data.public_metrics["listed_count"]
#     userssearch["tweet_count"] = user.data.public_metrics["tweet_count"]
#     userssearch["username"] = user.data.username
#     userssearch["verified"] = user.data.verified
#     crud.create_search_user_search(db, users_search, search_id)

#     query = "from:" + username
#     tweets = client.search_recent_tweets(query=query, tweet_fields=['text','author_id','created_at','public_metrics','lang','source'],user_fields=['username'], expansions='author_id', max_results=10)

#     users = {u["id"]: u for u in tweets.includes['users']}
#     tweetssearch = {}
#     for tweet in tweets.data:
#         if users[tweet.author_id]:
#             user = users[tweet.author_id]
#             tweetssearch['url'] = 'https://twitter.com/{}/status/{}'.format(user.username, tweet['id'])
#             tweetssearch["text"] = tweet.text
#             tweetssearch["author"] = user.username
#             tweetssearch["created_at"] = tweet.created_at
#             tweetssearch["retweet_count"] = tweet.public_metrics["retweet_count"]
#             tweetssearch["reply_count"] = tweet.public_metrics["reply_count"]
#             tweetssearch["like_count"] = tweet.public_metrics["like_count"]
#             tweetssearch["quote_count"] = tweet.public_metrics["quote_count"]
#             tweetssearch["lang"] = tweet.lang
#             tweetssearch["source"] = tweet.source
#             crud.create_search_tweet_search(db, tweetssearch, search_id)
    

# Crea una busqueda para un usuario
# @router.post("/user/search", response_model=schemas.Search)
# def create_search_for_user(
#     search: schemas.SearchCreate, 
#     db: Session = Depends(get_db),
#     current_user: schemas.User = Depends(get_current_user)
# ):
#     searchquery = crud.create_user_search(db=db, search=search, user_id=current_user.id)
#     if search.type == "tweet":
#         # hacer busqueda de TweetSearch
#         search_tweets(db=db, query=searchquery.title, search_id=searchquery.id)
#     else:
#         # hacer busqueda de usertweet
#         search_user(db=db, username=searchquery.title, search_id=searchquery.id)
#     return searchquery

# DAO
@router.post("/user/search", response_model=schemas.Search)
def create_search_for_user(
    search: schemas.SearchCreate, 
    current_user: schemas.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    searchquery = se.searchsDAOImpl.create_user_search(search=search, user_id=current_user.id, db=db)
    if search.type == "Tweet":
        # hacer busqueda de TweetSearch
        se.searchsDAOImpl.search_tweets(query=searchquery.title, search_id=searchquery.id, db=db)
    else:
        # hacer busqueda de usertweet
        se.searchsDAOImpl.search_user(username=searchquery.title, search_id=searchquery.id, db=db)
    return searchquery


# Recupera todas las busquedas realizadas
# @router.get("/searchs", response_model=list[schemas.Search])
# def read_searchs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     searchs = crud.get_searchs(db, skip=skip, limit=limit)
#     return searchs

# DAO
@router.get("/searchs", response_model=list[schemas.Search])
def read_searchs(db: Session = Depends(get_db)):
    searchs = se.searchsDAOImpl.get_searchs(db=db)
    return searchs

# Recupera los tweets buscados en una busqueda concreta
# @router.get("/search/tweets", response_model=list[schemas.TweetSearch])
# def get_tweets_of_search(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
#     search_id = current_user.searchs[-1].id
#     tweets = crud.get_tweets_of_search(db, skip=skip, limit=limit, search_id=search_id)
#     return tweets

#DAO
@router.get("/search/tweets", response_model=list[schemas.TweetSearch])
def get_tweets_of_search(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    search_id = current_user.searchs[-1].id
    tweets = se.searchsDAOImpl.get_tweets_of_search(db=db,search_id=search_id)
    return tweets

# Crea una nueva busqueda de tweets
# @router.post("/users/{search_id}/tweetsearch", response_model=schemas.TweetSearch)
# def create_tweet_search_for_search(
#     search_id: int, tweet_search: schemas.TweetSearchCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_search_tweet_search(db=db, tweet_search=tweet_search, search_id=search_id)

#DAO
@router.post("/users/{search_id}/tweetsearch", response_model=schemas.TweetSearch)
def create_tweet_search_for_search(
    search_id: int, tweet_search: schemas.TweetSearchCreate, db: Session = Depends(get_db)
):
    return se.searchsDAOImpl.create_search_tweet_search(tweet_search=tweet_search, search_id=search_id, db=db)

# Recupera todos los tweets buscados
# @router.get("/tweetssearchs", response_model=list[schemas.TweetSearch])
# def read_tweet_searchs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     tweetsearchs = crud.get_tweet_searchs(db, skip=skip, limit=limit)
#     return tweetsearchs

#DAO
@router.get("/tweetssearchs", response_model=list[schemas.TweetSearch])
def read_tweet_searchs(db: Session = Depends(get_db)):
    tweetsearchs = se.searchsDAOImpl.get_tweet_searchs(db=db)
    return tweetsearchs


# Recupera un tweet buscado
# @router.get("/tweetsearch/{tweetsearch_id}", response_model=schemas.TweetSearch)
# def get_tweet_by_id(tweetsearch_id: int,db: Session = Depends(get_db)):
#     db_tweet = crud.get_tweet_by_id(db, tweetsearch_id=tweetsearch_id)
#     if db_tweet is None:
#         raise HTTPException(status_code=404, detail="Tweet not found")
#     return db_tweet

#DAO
@router.get("/tweetsearch/{tweetsearch_id}", response_model=schemas.TweetSearch)
def get_tweet_by_id(tweetsearch_id: int, db: Session = Depends(get_db),):
    db_tweet = se.searchsDAOImpl.get_tweet_by_id(tweetsearch_id=tweetsearch_id, db=db)
    if db_tweet is None:
        raise HTTPException(status_code=404, detail="Tweet not found")
    return db_tweet

# Crea una nueva busqueda de usuario
# @router.post("/users/{search_id}/usersearch", response_model=schemas.UserSearch)
# def create_user_search_for_search(
#     search_id: int, user_search: schemas.UserSearchCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_search(db=db, user_search=user_search, search_id=search_id)

#DAO
@router.post("/users/{search_id}/usersearch", response_model=schemas.UserSearch)
def create_user_search_for_search(
    search_id: int, user_search: schemas.UserSearchCreate, db: Session = Depends(get_db),
):
    return se.searchsDAOImpl.create_user_search(user_search=user_search, search_id=search_id, db=db)


# Recupera todos los usuarios buscados
# @router.get("/usersearchs", response_model=list[schemas.UserSearch])
# def read_user_searchs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     usersearchs = crud.get_user_searchs(db, skip=skip, limit=limit)
#     return usersearchs

# DAO
@router.get("/usersearchs", response_model=list[schemas.UserSearch])
def read_user_searchs(db: Session = Depends(get_db)):
    usersearchs = se.searchsDAOImpl.get_user_searchs(db=db)
    return usersearchs

# Recupera el usuario buscado en una busqueda concreta
# @router.get("/search/user", response_model=schemas.UserSearch)
# def get_user_of_search(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
#     search_id = current_user.searchs[-1].id
#     user = crud.get_user_of_search(db, search_id=search_id)
#     return user

#DAO
@router.get("/search/user", response_model=schemas.UserSearch)
def get_user_of_search(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    search_id = current_user.searchs[-1].id
    user = se.searchsDAOImpl.get_user_of_search(db=db, search_id=search_id)
    return user