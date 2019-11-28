from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


Base = declarative_base()

class Categorie(Base):
    __tablename__ = 'category'
    id_casper = Column(Integer, primary_key=True)    
    categorie = Column('categorie', String(150))
    tweet =  relationship('Tweet')  

    def __str__(self):
        return self.content    