import os

DEBUG = True

# configuration page num
PER_PAGE = 10

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RTCD'

DB_CONFIG = {
    "db_username": 'root',
    "db_password": '123456',
    'default_database_host': 'localhost',
    'default_database_port': '3306',
    'database_name_prefix': '',
    'database_name_default': 'tdb_db'
}
STATIC_FOLDER = os.path.abspath('..') + '/static'

