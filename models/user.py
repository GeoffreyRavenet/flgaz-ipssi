from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Base = declarative_base()


class User(UserMixin, db.Model):
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