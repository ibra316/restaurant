import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base #
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base() # make the classes we make spical so it can creat tables inside the database
#---------Code---------


class Restaurant(Base):
    """Restaurant Table inside the DB."""
    __tablename__ = 'restaurant'

    name = Column(String(80), nullable = False) # Column called name inside restaurant table, nullable = false means it have to have entry

    id = Column(
    Integer, primary_key = True
    )



class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable = False)

    id = Column(
    Integer, primary_key = True
    )

    course = Column(String(250))

    description = Column(String(250))

    price = Column(String(8))

    restaurant_id = Column(Integer, ForeignKey('restaurant.id'
    ))

    restaurant = relationship(Restaurant)



#---------Code---------
engine = create_engine('sqlite:///restaurantmenu.db') #link or creat a DB
Base.metadata.create_all(engine) # goes to the database and add the Classes we made as a table
