import logging
import os
import sys
import traceback

import datehandler
import dbconnection

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig()


class MainWindow():
    ''' just some class '''
    def __init__(self, appStatus, dbConnection):
        print('a MainWindow object is being created')
        # here I can access and change appStatus and dbConnection
        # I will also need to access those database tables


if __name__ == '__main__':
    try:
        # initialize a dbConnection and an object that holds the applications' status information
        # those objects are supposed to be passed around the whole app, so every component has access to these infos and can change them
        DB_PATH = os.path.join(os.path.dirname(__file__), './data.db')
        dbConnection = dbconnection.DatabaseConnection(DB_PATH)
        appStatus = datehandler.ApplicationStatus(dbConnection)

        # do some other stuff that needs both dbConnection and appStatus
        mainWindow = MainWindow(appStatus, dbConnection)

    except Exception as e:
        print('Exception occurred')
        traceback.print_exc(file=sys.stdout)
