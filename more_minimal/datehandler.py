from sqlalchemy import and_

#import dbtables


# class with some status information as properties and functions to change those properties
# the dbConnection as well as the databases tables are needed here!                                       xxxxxx


class ApplicationStatus():
    def __init__(self, dbConnection):
        self.databaseRange = determineDatabaseRange(dbConnection)
        self.currentDate = self.databaseRange[0]
        self.currentDateEntries = getEntriesforDate(self.currentDate, dbConnection)

    def setCurrentDate(self, date, dbConnection):
        print('setCurrentDate')




# in the following functions I need acces to database tables


def determineDatabaseRange(dbConnection):
    session = dbConnection.Session()
    query = session.query(dbConnection.locations.columns.time)
    dbRange = [query.first()[0], query.order_by(dbConnection.locations.columns.id.desc()).first()[0]]
    return dbRange


def getEntriesforDate(date, dbConnection):
    session = dbConnection.Session()
    query = session.query(dbConnection.stops).filter(and_(dbConnection.stops.columns.startTime >= 1496355082430,
                                                           dbConnection.stops.columns.startTime <= 1496416011016))
    entries = query.all()

    return entries

