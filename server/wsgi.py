# from myapp import app
from gevent.pywsgi import WSGIServer
from apps import app as application

if __name__ == "__main__":
    # application.run()

    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop

    http_server = HTTPServer(WSGIContainer(application))
    http_server.listen(5001)
    IOLoop.instance().start()

#http = WSGIServer(('', 5000), application.wsgi_app)
# TODO gracefully handle shutdown
#http.serve_forever()