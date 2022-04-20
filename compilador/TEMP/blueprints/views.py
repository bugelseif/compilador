from urllib import request
from flask import render_template

def init_app(app):
    @app.route("/")
    def index():
        lista = ['qualquer', 'coisa', 'aaaa']
        return render_template("index.html", lista=lista)

    @app.route("/test", methods=['POST'])
    def test():
        return "testado"
