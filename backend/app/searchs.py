from sqlalchemy.orm import Session
import requests
import json

import models, schemas, crud

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAPwbewEAAAAAFchVqp4fuXveeBPBiewYordtRuQ%3DVjQTaili6wXSzvvVYont62VrQyEhLxoEqKCIgljjNx6h9bbZKB";

def search_tweets(db: Session, query:str, search_id: int):
    field_returned = "tweet.fields=text,author_id,created_at,public_metrics,lang,source"
    headers = {"Authorization": "Bearer {}".format(BEARER_TOKEN)}

    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, field_returned
    )
    # Se hace la peticion a la API de twitter
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
        
    print(response.json())

    #HAY QUE PASAR A SERIALIZABLE EL RESPONSE Y METERLO EN LA BASE DE DATOS COMO NUEVOS tweetsearch


def search_user(db: Session, query:str, search_id: int):
    # Campos del usuario que queremos
    field_returned = "user.fields=created_at,description,location,name,profile_image_url,public_metrics,username,verified"
    headers = {"Authorization": "Bearer {}".format(BEARER_TOKEN)}

    url = "https://api.twitter.com/2/users/by?{}&{}".format(
        query, field_returned
    )
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    response.json()

    # CUANDO SE HACE LA BUSQUEDA DE UN USUARIO ADEMAS SE RECUPERAN LOS ULTIMOS TWEETS SUYOS
    field_user = "tweet.fields=text,author_id,created_at,public_metrics,lang,source"

    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, field_user
    )
    # Se hace la peticion a la API de twitter
    response2 = requests.request("GET", url, headers=headers)
    print(response2.status_code)
    if response2.status_code != 200:
        raise Exception(response2.status_code, response2.text)
        
    print(response2.json())

    
