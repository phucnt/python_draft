from apps import app, Base, mysqlConnection

from sqlalchemy import exc, Column, Integer, String, Index, func
import apps.services.utilities

utilities = apps.services.utilities

def hello():
    returnObj = {}
    unsharded_session = None
    try:
        unsharded_session = mysqlConnection.get_connection_by_id()

        returnObj["code"] = 200
        returnObj["result"] = "Hello World"
        return returnObj
    except exc.IntegrityError as error:
        if unsharded_session is not None:
            unsharded_session.rollback()
        returnObj["code"] = 500
        returnObj["result"] = error.orig.args[1]
        return returnObj
    finally:
        if unsharded_session is not None:
            unsharded_session.remove()