from flask import jsonify


def error400(message):
    print '@@@@@@@!@!@!@!@'
    description = 'Bad Request'
    if (message is not None):
        description = message
    response = jsonify({
        'code': 0,
        'msg': description
    })
    response.status_code = 400
    return response


def error401(message):
    description = 'Unauthorized'
    if (message is not None):
        description = message
    response = jsonify({
        'code': 0,
        'msg': description
    })
    response.status_code = 401
    return response


def error403(message):
    description = 'Forbidden'
    if (message is not None):
        description = message
    response = jsonify({
        'code': 0,
        'msg': description
    })
    response.status_code = 403
    return response


def error404(message):
    description = 'Request not found'
    if (message is not None):
        description = message
    response = jsonify({
        'code': 0,
        'msg': description
    })
    response.status_code = 404
    return response


def error500(message):
    description = 'Internal server error'
    if (message is not None):
        description = message
    response = jsonify({
        'code': 0,
        'msg': description
    })
    response.status_code = 500
    return response


def errorHTTP(code, message):
    response = jsonify({
        'code': 0,
        'msg': message
    })
    response.status_code = code
    return response
