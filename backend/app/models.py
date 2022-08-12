from array import array
from datetime import date
from email.policy import default
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base


class Search(Base):
    __tablename__ = "search"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    type = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    ownersearch = relationship("User", back_populates="searchs")
    tweetsearchs = relationship("TweetSearch", back_populates="ownertweetsearch")
    usersearchs = relationship("UserSearch", back_populates="ownerusersearch")

    def __getsearch__(self, i):
        return f"Value {i}"

class TweetSearch(Base):
    __tablename__ = "tweetsearch"

    id = Column(Integer, primary_key=True, index=True)
    url= Column(String, index=True)
    text = Column(String, index=True)
    author = Column(String, index=True)
    created_at = Column(Date, index=True)
    retweet_count = Column(Integer, index=True)
    reply_count = Column(Integer, index=True)
    like_count = Column(Integer, index=True)
    quote_count = Column(Integer, index=True)
    lang = Column(String, index=True)
    source = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("search.id"))

    ownertweetsearch = relationship("Search", back_populates="tweetsearchs")
    #tweetowner = relationship("User", back_populates="tweetsaves")

    def __gettweetsearch__(self, i):
        return f"Value {i}"

class UserSearch(Base):
    __tablename__ = "usersearch"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(Date, index=True)
    description = Column(String, index=True)
    location = Column(String, index=True)
    name = Column(String, index=True)
    profile_image_url = Column(String, index=True)
    followers_count = Column(Integer, index=True)
    following_count = Column(Integer, index=True)
    listed_count = Column(Integer, index=True)
    tweet_count = Column(Integer, index=True)
    username = Column(String, index=True)
    verified = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("search.id"))

    ownerusersearch = relationship("Search", back_populates="usersearchs")

    def __getusersearch__(self, i):
        return f"Value {i}"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(String, default=str(date.today())) 
    image = Column(String, default="https://www.dreamstime.com/default-avatar-profile-icon-vector-user-image-image179582665")
    tweets_saved = list()

    searchs = relationship("Search", back_populates="ownersearch")
    #tweetsaves = relationship("TweetSearch", back_populates="tweetowner")

    def __getuser__(self, i):
        return f"Value {i}"
