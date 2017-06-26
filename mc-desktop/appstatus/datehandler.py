import datetime
from sqlalchemy import and_
from helper import timehelper
from database import dbtables


# class with some status information as properties and functions to change those properties
# the dbConnection as well as the databases tables are needed here!                                       xxxxxx


class ApplicationStatus():
    def __init__(self, dbConnection):
        self.databaseRange = determineDatabaseRange(dbConnection)
        self.currentDate = self.databaseRange[0]
        self.currentDateEntries = getEntriesforDate(self.currentDate)

    def setCurrentDate(self, date, dbConnection):
        print('setCurrentDate')




# in the following functions I need acces to the database tables


def determineDatabaseRange(dbConnection):
    session = dbConnection.Session()
    query = session.query(dbtables.LocationsTable.time)
    db_range_timestamp = [query.first()[0], query.order_by(dbtables.LocationsTable.id.desc()).first()[0]]
    db_range_utc = [timehelper.timestamp_to_utc(db_range_timestamp[0]), timehelper.timestamp_to_utc(db_range_timestamp[1])]
    #db_range_cet = [utc_to_cet(db_range_utc[0]), utc_to_cet(db_range_utc[1])]

    return db_range_timestamp, db_range_utc



def getEntriesforDate(date, dbConnection):
    if type(date) == QtCore.QDate:
        date = QtCore.QDate.toPyDate(date)
    date = datetime.datetime.combine(date, datetime.datetime.min.time())
    next_date = date + datetime.timedelta(days=1)

    # TODO figure out timezone for date xx

    dayrange_timestamp = [timehelper.cetdatetime_to_timestamp(date), timehelper.cetdatetime_to_timestamp(next_date)]
    session = dbConnection.Session()

    # STOPS
    stop_query = session.query(dbtables.StopsTable).filter(and_(dbtables.StopsTable.startTime >= dayrange_timestamp[0],
                                                       dbtables.StopsTable.startTime < dayrange_timestamp[1]))
    stops_list = stop_query.all()
    # convert DatabaseTable objects to easier to use Stop objects
    #stops_list = [stop.Stop(stop) for stop in stops_list] # equivalent to list(map(Stop, stops_list))

    # MOVEMENTS
    movement_query = session.query(dbtables.MovementTable).filter(and_(dbtables.MovementTable.startTime >= dayrange_timestamp[0],
                                                              dbtables.MovementTable.startTime < dayrange_timestamp[1]))
    movements_list = movement_query.all()
    #movements_list = [movement.Movement(movement) for movement in movements_list]

    sorted_entries = sorted(stops_list + movements_list, key=lambda entry: entry.startTime)

    print(sorted_entries)
    return sorted_entries

