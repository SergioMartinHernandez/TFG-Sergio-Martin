from sqlalchemy.orm import Session
import requests
import json
import tweepy
import models, schemas, crud

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAPwbewEAAAAAFchVqp4fuXveeBPBiewYordtRuQ%3DVjQTaili6wXSzvvVYont62VrQyEhLxoEqKCIgljjNx6h9bbZKB";

def search_tweets(db: Session, query:str, search_id: int):
    #field_returned = "tweet.fields=text,author_id,created_at,public_metrics,lang,source"
    query= query + " is:verified"
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    tweets = client.search_recent_tweets(query=query, tweet_fields=['text','author_id','created_at','public_metrics','lang','source'],user_fields=['username'], expansions='author_id', max_results=10)

    users = {u["id"]: u for u in tweets.includes['users']}
    tweetssearch = {}
    for tweet in tweets.data:
        if users[tweet.author_id]:
            user = users[tweet.author_id]
            tweetssearch['url'] = 'https://twitter.com/{}/status/{}'.format(user.username, tweet['id'])
            tweetssearch["text"] = tweet.text
            tweetssearch["author"] = user.username
            tweetssearch["created_at"] = tweet.created_at
            tweetssearch["retweet_count"] = tweet.public_metrics["retweet_count"]
            tweetssearch["reply_count"] = tweet.public_metrics["reply_count"]
            tweetssearch["like_count"] = tweet.public_metrics["like_count"]
            tweetssearch["quote_count"] = tweet.public_metrics["quote_count"]
            tweetssearch["lang"] = tweet.lang
            tweetssearch["source"] = tweet.source
            crud.create_search_tweet_search(db, tweetssearch, search_id)
    #headers = {"Authorization": "Bearer {}".format(BEARER_TOKEN)}

    # url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
    #     query, field_returned
    # )
    # # Se hace la peticion a la API de twitter
    # response = requests.request("GET", url, headers=headers)
    # print(response.status_code)
    # if response.status_code != 200:
    #     raise Exception(response.status_code, response.text)
        
    # print(response.json())

    

    #HAY QUE PASAR A SERIALIZABLE EL RESPONSE Y METERLO EN LA BASE DE DATOS COMO NUEVOS tweetsearch


def search_user(db: Session, username:str, search_id: int):
    # Campos del usuario que queremos
    # field_returned = "user.fields=created_at,description,location,name,profile_image_url,public_metrics,username,verified"
    # headers = {"Authorization": "Bearer {}".format(BEARER_TOKEN)}

    # url = "https://api.twitter.com/2/users/by?{}&{}".format(
    #     query, field_returned
    # )
    # response = requests.request("GET", url, headers=headers)
    # print(response.status_code)
    # if response.status_code != 200:
    #     raise Exception(response.status_code, response.text)
    # response.json()

    # # CUANDO SE HACE LA BUSQUEDA DE UN USUARIO ADEMAS SE RECUPERAN LOS ULTIMOS TWEETS SUYOS
    # field_user = "tweet.fields=text,author_id,created_at,public_metrics,lang,source"

    # url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
    #     query, field_user
    # )
    # # Se hace la peticion a la API de twitter
    # response2 = requests.request("GET", url, headers=headers)
    # print(response2.status_code)
    # if response2.status_code != 200:
    #     raise Exception(response2.status_code, response2.text)
        
    # print(response2.json())
    username=username.replace(" ", "")
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    user = client.get_user(username=username,user_fields=['created_at','description','location','name','profile_image_url','public_metrics','username','verified'])
    userssearch = {}
    
    userssearch["created_at"] = user.data.created_at
    userssearch["description"] = user.data.description
    userssearch["location"] = user.data.location
    userssearch["name"] = user.data.name
    userssearch["profile_image_url"] = user.data.profile_image_url
    userssearch["followers_count"] = user.data.public_metrics["followers_count"]
    userssearch["following_count"] = user.data.public_metrics["following_count"]
    userssearch["listed_count"] = user.data.public_metrics["listed_count"]
    userssearch["tweet_count"] = user.data.public_metrics["tweet_count"]
    userssearch["username"] = user.data.username
    userssearch["verified"] = user.data.verified
    crud.create_search_user_search(db, userssearch, search_id)

    query = "from:" + username
    tweets = client.search_recent_tweets(query=query, tweet_fields=['text','author_id','created_at','public_metrics','lang','source'],user_fields=['username'], expansions='author_id', max_results=10)

    users = {u["id"]: u for u in tweets.includes['users']}
    tweetssearch = {}
    for tweet in tweets.data:
        if users[tweet.author_id]:
            user = users[tweet.author_id]
            tweetssearch['url'] = 'https://twitter.com/{}/status/{}'.format(user.username, tweet['id'])
            tweetssearch["text"] = tweet.text
            tweetssearch["author"] = user.username
            tweetssearch["created_at"] = tweet.created_at
            tweetssearch["retweet_count"] = tweet.public_metrics["retweet_count"]
            tweetssearch["reply_count"] = tweet.public_metrics["reply_count"]
            tweetssearch["like_count"] = tweet.public_metrics["like_count"]
            tweetssearch["quote_count"] = tweet.public_metrics["quote_count"]
            tweetssearch["lang"] = tweet.lang
            tweetssearch["source"] = tweet.source
            crud.create_search_tweet_search(db, tweetssearch, search_id)
    
