from apps import app
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from random import choice, randint
import time
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import exc, Column, Integer, String, Index, func

db_config = app.config['DB_CONFIG']

class MySqlConnection:
    def __init__(self):
        self.connection = []
        self.connect()
        # self.initDB()

    def connect(self):
        SQLALCHEMY_DATABASE_URI_UNSHARDDB = "mysql+mysqlconnector://%s:%s@%s:%s/%s" % (
            db_config['db_username'], db_config['db_password'], db_config['default_database_host'],
            db_config['default_database_port'],
            db_config['database_name_prefix'] + db_config['database_name_default'])
        engine = create_engine(SQLALCHEMY_DATABASE_URI_UNSHARDDB, pool_size=100, max_overflow=0,
                               pool_recycle=3600, pool_pre_ping=True)
        db_session = scoped_session(sessionmaker(autocommit=False,
                                                 autoflush=True,
                                                 bind=engine))
        self.connection.append(db_session)

    def get_connection_by_id(self, id=0):
        return self.connection[id]