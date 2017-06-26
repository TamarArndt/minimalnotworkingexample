from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# so far so good:
# this class is not problematic, I just have to make sure I only create one instance of it
# right in the beginning

class DatabaseConnection():
    def __init__(self, db_path):
        self.engine = create_engine("sqlite:///%s" % db_path, echo=False)
        self.engine.connect()
        self.Base = declarative_base(self.engine)
        self.Session = sessionmaker(bind=self.engine)

        meta = MetaData()

        self.stops = Table('stops', meta, autoload=True, autoload_with=self.engine)
        print(self.stops.columns)
        self.locations = Table('locations', meta, autoload=True, autoload_with=self.engine)
        print(self.locations.columns)


