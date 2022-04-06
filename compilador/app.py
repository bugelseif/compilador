from flask import Flask
from flask_bootstrap import Bootstrap

from compilador.blueprints import views
from compilador.blueprints import restapi

app = Flask(__name__)

app.config['TITLE'] = 'Compilador'

Bootstrap(app)

restapi.init_app(app)
views.init_app(app)