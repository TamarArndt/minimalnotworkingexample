import os

# I have made this file in order to have one exact place to manage those variables
# also I don't know whether this is good practice


ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), './../')
DB_PATH = os.path.join(ROOT_DIR, './assets/data.db')