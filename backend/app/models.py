from array import array
from datetime import date
import datetime
from email.policy import default
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base


class Search(Base):
    __tablename__ = "search"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    type = Column(String)
    created_at = Column(String, default=str(datetime.datetime.now().ctime()))
    start_date = Column(String)
    end_date = Column(String)
    num_tweets = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

    ownersearch = relationship("User", back_populates="searchs")
    tweetsearchs = relationship("TweetSearch", back_populates="ownertweetsearch")
    usersearchs = relationship("UserSearch", back_populates="ownerusersearch")

    def __getsearch__(self, i):
        return f"Value {i}"

class TweetSearch(Base):
    __tablename__ = "tweetsearch"

    id = Column(Integer, primary_key=True, index=True)
    url= Column(String)
    text = Column(String)
    author = Column(String)
    created_at = Column(String)
    retweet_count = Column(Integer)
    reply_count = Column(Integer)
    like_count = Column(Integer)
    quote_count = Column(Integer)
    lang = Column(String)
    source = Column(String)
    owner_id = Column(Integer, ForeignKey("search.id"))

    ownertweetsearch = relationship("Search", back_populates="tweetsearchs")

    def __gettweetsearch__(self, i):
        return f"Value {i}"

class UserSearch(Base):
    __tablename__ = "usersearch"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(Date)
    description = Column(String)
    location = Column(String, nullable=True)
    name = Column(String)
    profile_image_url = Column(String)
    followers_count = Column(Integer)
    following_count = Column(Integer)
    listed_count = Column(Integer)
    tweet_count = Column(Integer)
    username = Column(String)
    verified = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("search.id"))

    ownerusersearch = relationship("Search", back_populates="usersearchs")

    def __getusersearch__(self, i):
        return f"Value {i}"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(String, default=str(date.today())) 
    image = Column(String, default="https://toppng.com/uploads/preview/instagram-default-profile-picture-11562973083brycehrmyv.png")

    searchs = relationship("Search", back_populates="ownersearch")
    tweetsaved = relationship("TweetSaved", back_populates="ownertweetsaved")

    def __getuser__(self, i):
        return f"Value {i}"


class TweetSaved(Base):
    __tablename__ = "tweetsaved"

    id = Column(Integer, primary_key=True, index=True)
    url= Column(String)
    text = Column(String)
    author = Column(String)
    created_at = Column(String)
    retweet_count = Column(Integer)
    reply_count = Column(Integer)
    like_count = Column(Integer)
    quote_count = Column(Integer)
    lang = Column(String)
    source = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    ownertweetsaved = relationship("User", back_populates="tweetsaved")

    def __gettweetsaved__(self, i):
        return f"Value {i}"