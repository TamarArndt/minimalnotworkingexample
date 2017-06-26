from sqlalchemy import Table, Column, INT


# WHAT DO I DO ???                                                              xxxxxxxxx
# define tables from database:
# the class definitions need to be the way they are,
# I can't make an __init__ function to pass Base and engine!
# I have no clue what to do.

# I guess I need an object of DatabaseConnection, but not just one, but THE object.
# but I cant put class definition into a function, can I?

# the only way I can think of is to somehow to deliver the DatabaseConnectionObject to this file when importing
# - but that doesn't sound good either


class StopsTable(Base):
    __table__ = Table('stops', Base.metadata, autoload=True, autoload_with=engine)


class MovementTable(Base):
    # rename originTime to startTime and destinationTime to endTime to make it equivalent to Stops' startTime/endTime
    __tablename__ = 'movement'
    __table_args__ = {'autoload': True}
    startTime = Column('originTime', INT)
    endTime = Column('destinationTime', INT)


class MovementLocationTable(Base):
    __table__ = Table('movementLocation', Base.metadata, autoload=True)


class PlaceTypeTable(Base):
    __table__ = Table('place_type', Base.metadata, autoload=True)


class TravelModeTable(Base):
    __table__ = Table('travelMode', Base.metadata, autoload=True)


class ClusterTable(Base):
    __table__ = Table('cluster', Base.metadata, autoload=True)


class ClusterTypeLookupTable(Base):
    __table__ = Table('cluster_type_lookup_table', Base.metadata, autoload=True)


class LocationsTable(Base):
    __table__ = Table('locations', Base.metadata, autoload=True)




