from datetime import date, timedelta
import datetime
from dependencies import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
import tweepy
import schemas, models
from dao.searchsDAO import SearchsDAO

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAPwbewEAAAAAFchVqp4fuXveeBPBiewYordtRuQ%3DVjQTaili6wXSzvvVYont62VrQyEhLxoEqKCIgljjNx6h9bbZKB";

class searchsDAOImpl(SearchsDAO):
    # Guarda un tweet de una busqueda en la base de datos
    def create_search_tweet_search(tweet_search: schemas.TweetSearchCreate, search_id: int, db: Session):
        db_tweet_search = models.TweetSearch(**tweet_search, owner_id=search_id)
        db.add(db_tweet_search)
        db.commit()
        db.refresh(db_tweet_search)
        return db_tweet_search

    # Realiza una consulta de tweets a la API de Twitter
    def search_tweets(query: str, search_id: int, start_date: str, end_date: str, num_tweets: int, db: Session):
        dateToday = date.today()

        if end_date == str(dateToday):
            end_date = datetime.datetime.now(datetime.timezone.utc) - timedelta(seconds=30)
            start_date=start_date+"T00:01:00+02:00"
        elif end_date == start_date:
            end_date = end_date[:-13]
            end_date = end_date + "23:59:00+02:00"
                      
        query = query + " is:verified"
        client = tweepy.Client(bearer_token=BEARER_TOKEN)
        tweets = client.search_recent_tweets(query=query, end_time=end_date, start_time=start_date, tweet_fields=['text','author_id','created_at','public_metrics','lang','source'],user_fields=['username'], expansions='author_id', max_results=num_tweets)

        if tweets[0] == None:
            return None
            
        users = {u["id"]: u for u in tweets.includes['users']}
        tweet_search = {}
        for tweet in tweets.data:
            if users[tweet.author_id]:
                user = users[tweet.author_id]
                tweet_search['url'] = 'https://twitter.com/{}/status/{}'.format(user.username, tweet['id'])
                tweet_search["text"] = tweet.text
                tweet_search["author"] = user.username
                tweet_search["created_at"] = tweet.created_at
                tweet_search["retweet_count"] = tweet.public_metrics["retweet_count"]
                tweet_search["reply_count"] = tweet.public_metrics["reply_count"]
                tweet_search["like_count"] = tweet.public_metrics["like_count"]
                tweet_search["quote_count"] = tweet.public_metrics["quote_count"]
                tweet_search["lang"] = tweet.lang
                tweet_search["source"] = tweet.source
                searchsDAOImpl.create_search_tweet_search(db=db, tweet_search=tweet_search, search_id=search_id)

    # Realiza una consulta de usuarios a la API de Twitter
    def search_user(username:str, search_id: int, start_date: str, end_date:str, num_tweets:int, db: Session):
        username=username.replace(" ", "")
        username=username.replace("@", "")
        dateToday = date.today()
        timelimit = datetime.datetime.now(datetime.timezone.utc) - timedelta(days=7)

        if end_date == str(dateToday):
            end_date = datetime.datetime.now(datetime.timezone.utc) - timedelta(seconds=30)
            start_date=start_date+"T00:01:00+02:00"
        elif end_date == start_date:
            end_date = end_date[:-13]
            end_date = end_date + "23:59:00+02:00"


        client = tweepy.Client(bearer_token=BEARER_TOKEN)
        user = client.get_user(username=username,user_fields=['created_at','description','location','name','profile_image_url','public_metrics','username','verified'])
        user_search = {}
        
        user_search["created_at"] = user.data.created_at
        user_search["description"] = user.data.description
        user_search["location"] = user.data.location
        user_search["name"] = user.data.name
        user_search["profile_image_url"] = user.data.profile_image_url
        user_search["followers_count"] = user.data.public_metrics["followers_count"]
        user_search["following_count"] = user.data.public_metrics["following_count"]
        user_search["listed_count"] = user.data.public_metrics["listed_count"]
        user_search["tweet_count"] = user.data.public_metrics["tweet_count"]
        user_search["username"] = user.data.username
        user_search["verified"] = user.data.verified
        searchsDAOImpl.create_search_user_search(db=db, user_search=user_search, search_id=search_id)

        query = "from:" + username
        tweets = client.search_recent_tweets(query=query, end_time=end_date, start_time=start_date, tweet_fields=['text','author_id','created_at','public_metrics','lang','source'],user_fields=['username'], expansions='author_id', max_results=num_tweets)

        if tweets[0] == None:
            return None

        users = {u["id"]: u for u in tweets.includes['users']}
        tweet_search = {}
        for tweet in tweets.data:
            if users[tweet.author_id]:
                user = users[tweet.author_id]
                tweet_search['url'] = 'https://twitter.com/{}/status/{}'.format(user.username, tweet['id'])
                tweet_search["text"] = tweet.text
                tweet_search["author"] = user.username
                tweet_search["created_at"] = tweet.created_at
                tweet_search["retweet_count"] = tweet.public_metrics["retweet_count"]
                tweet_search["reply_count"] = tweet.public_metrics["reply_count"]
                tweet_search["like_count"] = tweet.public_metrics["like_count"]
                tweet_search["quote_count"] = tweet.public_metrics["quote_count"]
                tweet_search["lang"] = tweet.lang
                tweet_search["source"] = tweet.source
                searchsDAOImpl.create_search_tweet_search(db=db, tweet_search=tweet_search, search_id=search_id)

    # Guarda un usuario buscado en la base de datos
    def create_search_user_search(db: Session, user_search: schemas.UserSearchCreate, search_id: int):
        db_user_search = models.UserSearch(**user_search, owner_id=search_id)
        db.add(db_user_search)
        db.commit()
        db.refresh(db_user_search)
        return db_user_search

    # Crea una busqueda para un usuario
    def create_user_search(search: schemas.SearchCreate, user_id: int, db: Session):
        db_search = models.Search(**search.dict(), owner_id=user_id)
        db.add(db_search)
        db.commit()
        db.refresh(db_search)
        return db_search

    # Obtiene todas las busquedas 
    def get_searchs(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Search).offset(skip).limit(limit).all()

    # Obtiene una búsqueda dado su Id 
    def get_search_by_id(db: Session, search_id: int, user_id: int):
        return db.query(models.Search).filter(models.Search.id == search_id).filter(models.Search.owner_id == user_id).first()

    # Elimina una busqueda de un usuario
    def delete_search(db: Session, search: schemas.Search):
        db.delete(search)
        db.commit()

    # Obtiene los tweets de una busqueda
    def get_tweets_of_search(search_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return db.query(models.TweetSearch).filter(models.TweetSearch.owner_id == search_id).offset(skip).limit(limit).all()

    # Obtiene los tweets buscados
    def get_tweet_searchs(db: Session,skip: int = 0, limit: int = 100):
        return db.query(models.TweetSearch).offset(skip).limit(limit).all()

    # Obtiene un tweet dado su id
    def get_tweet_by_id(tweetsearch_id: int, db: Session):
        return db.query(models.TweetSearch).filter(models.TweetSearch.id == tweetsearch_id).first()

    # Obtiene las busquedas de usuarios
    def get_user_searchs(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.UserSearch).offset(skip).limit(limit).all()

    # Obtiene el usuario buscado de una busqueda
    def get_user_of_search(db: Session, search_id: int):
        return db.query(models.UserSearch).filter(models.UserSearch.owner_id == search_id).first()
