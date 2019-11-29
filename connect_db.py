import setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models.tweet as tweet


logbdb = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(setting.LOGIN, setting.MDP, setting.HOST, setting.NAME_BDD)
engine = create_engine(logbdb)

session = sessionmaker()
session.configure(bind=engine)
s = session()
   

tweet1 = tweet.Tweet(content='test add message bdd', user="user test")
s.add(tweet1)
s.commit()