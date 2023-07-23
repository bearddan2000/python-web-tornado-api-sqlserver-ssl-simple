from sqlalchemy import Column, Integer, String
from tornado_sqlalchemy import SQLAlchemy

import settings

database_url = '{engine}://{username}:{password}@{host}/{db_name}'.format(
        **settings.POSTGRESQL
    )

db = SQLAlchemy(url=database_url)

class DogModel(db.Model):
    __tablename__ = 'dog'
    id = Column(Integer, primary_key=True, autoincrement=True,)
    breed = Column(String(20))
    color = Column(String(10))

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def __repr__(self):
        return "<Dog('%s', '%s')>" % (self.breed, self.color)
