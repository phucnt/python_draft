from flask import Blueprint, jsonify, request, session, copy_current_request_context
from apps import app
from flask_cors import CORS

hello_blueprint = Blueprint('hello', __name__)
per_page = app.config['PER_PAGE']
CORS(hello_blueprint, supports_credentials=True)

import apps.hello.controllers

helloControllers = apps.hello.controllers

import gevent
import apps.services.httpError

httpError = apps.services.httpError
#### ACL ####
from flask_simpleAcl import ACL

acl = ACL(app)

@hello_blueprint.route('/', methods=['GET'])
def get_hello():
    @copy_current_request_context
    def g_hello(request):
        return helloControllers.hello(request)

    thread = gevent.spawn(g_hello, request)
    thread.join()
    if (thread.successful() == True):
        return thread.value
    else:
        return httpError.error500({
            "code": 0,
            "msg": "Failed",
            "err": 10,
            "data": "Server internal error"
        })