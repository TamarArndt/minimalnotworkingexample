from sqlalchemy import create_engine
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

