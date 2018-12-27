import os

from flask import Flask
from flask_restplus import Api, Resource
from werkzeug.contrib.fixers import ProxyFix

from src import basic_functions as bf

# Setting up Python API
my_list = list()
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='Agile Tutorial', description='A simple Python API')
api.namespaces.clear()

# Creating API namespaces
basic_ns = api.namespace('basic', description='List manipulation')
math_ns = api.namespace('math', description='Math operations')


@basic_ns.route('/print')
@basic_ns.doc(description='Print current list.')
class PrintList(Resource):
    def get(self):
        return bf.to_json(my_list)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
