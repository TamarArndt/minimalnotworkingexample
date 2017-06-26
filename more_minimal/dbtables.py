from sqlalchemy import Table



# WHAT DO I DO ???                                                              xxxxxxxxx
# define tables from database:
# the class definitions need to be the way they are,
# I can't make an __init__ function to pass Base and engine!
# I have no clue what to do.

# I guess I need an object of DatabaseConnection, but not just one, but THE object.
# but I cant put class definition into a function, can I?

# the only way I can think of is to somehow to deliver the DatabaseConnectionObject to this file when importing
# - but that doesn't sound good either

stops = Table('stops', Base.metadata, autoload=True, autoload_with=engine)
locations = Table('locations', Base.metadata, autoload=True, autoload_with=engine)


class StopsTable(Base):
    __table__ = Table('stops', Base.metadata, autoload=True, autoload_with=engine)


class LocationsTable(Base):
    __table__ = Table('locations', Base.metadata, autoload=True)




