import setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models


logbdb = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(setting.LOGIN, setting.MDP, setting.HOST, setting.NAME_BDD)
engine = create_engine(logbdb)

session = sessionmaker()
session.configure(bind=engine)
s = session()


user = models.User(username='user', role='utilisateur', mail="mail@mail.com", password="pass", is_active=True, is_connected=True, profile_picture="image")
s.add(user)
s.commit()