from flask import Flask, render_template, jsonify, session

from sqlalchemy.ext.declarative import declarative_base

import apps.services.httpError as httpError

from flask.ext.login import LoginManager

app = Flask(__name__,
            static_url_path='/static',
            static_folder='../../static',
            template_folder='../../client')

app_name = __name__.split('.')[0]
app.url_map.strict_slashes = False
app.config.from_object('config')

########################MySQL#####################################
Base = declarative_base()
# ****************************SHARDING**********************************
from apps.services.mysqlconnection import MySqlConnection
mysqlConnection = MySqlConnection()
##################################################################

from apps.hello.views import hello_blueprint
app.register_blueprint(hello_blueprint, url_prefix='/api/hello')
