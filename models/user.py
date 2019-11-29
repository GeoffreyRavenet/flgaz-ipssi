from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

#Base = declarative_base()


class User(db.Model):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True)    
    username = Column('username', String(32))    
    role = Column('role', String(50))    
    mail = Column('mail', String(250))    
    password = Column('password', String(250))
    is_active = Column('is_active', Boolean)
    is_connected = Column('is_connected', Boolean)
    profile_picture = Column('profile_picture', String)
    tweet = relationship("Tweet")

    def __str__(self):
        return self.username    