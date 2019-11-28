import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'tweet'
    id_casper = Column(Integer, primary_key=True)    
    content = Column('content', String(280))    
    #delay = Column('delay', String(50))    
    date_creation = Column('date_creation', DateTime, default=datetime.datetime.utcnow)    
    #is_temporary = Column('is_temporary', Boolean)
    categorie = Column(String(150), ForeignKey('user.id_user'))
    id_creator = Column(Integer, ForeignKey('category.id_categorie'))

    def __str__(self):
        return self.content