from sqlalchemy import and_

import dbtables


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
    query = session.query(dbtables.LocationsTable.time)
    dbRange = [query.first()[0], query.order_by(dbtables.LocationsTable.id.desc()).first()[0]]
    return dbRange


def getEntriesforDate(date, dbConnection):
    session = dbConnection.Session()
    query = session.query(dbtables.StopsTable).filter(and_(dbtables.StopsTable.startTime >= 1496355082430,
                                                           dbtables.StopsTable.startTime <= 1496416011016))
    entries = query.all()

    return entries

