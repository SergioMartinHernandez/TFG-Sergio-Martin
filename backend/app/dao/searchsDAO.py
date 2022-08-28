from sqlalchemy.orm import Session
import schemas


class SearchsDAO:
    def search_tweets(query:str, search_id: int, db: Session):
        pass

    def search_user(username:str, search_id: int, db: Session):
        pass

    def create_user_search(search: schemas.SearchCreate, user_id: int, db: Session):
        pass

    def get_searchs(db: Session):
        pass

    def get_tweets_of_search(db: Session,search_id: int):
        pass

    def create_search_user_search(user_search: schemas.UserSearchCreate, search_id: int, db: Session):
        pass

    def create_search_tweet_search(tweet_search: schemas.TweetSearchCreate, search_id: int, db: Session):
        pass

    def get_tweet_searchs(db: Session):
        pass

    def get_tweet_by_id(tweetsearch_id: int, db: Session):
        pass

    def create_user_search(db: Session, search: schemas.SearchCreate, user_id: int):
        pass

    def get_user_searchs(db: Session):
        pass

    def get_user_of_search(db: Session, search_id: int):
        pass