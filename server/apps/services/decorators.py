from flask import request, redirect, url_for, session, flash, Response, abort, make_response, current_app
from functools import wraps
from threading import Thread
from functools import update_wrapper
import apps.services.httpError

httpError = apps.services.httpError
from datetime import timedelta
from flask.ext.login import current_user

def require_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated:
            return httpError.error401('Unauthorized')

        return f(*args, **kwargs)

    return decorated