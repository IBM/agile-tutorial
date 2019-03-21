import os

from flask import Flask
from flask_restplus import Api, Resource
from werkzeug.contrib.fixers import ProxyFix

from src import math_services as ms
from src import basic_services as bs
from src import default_services as ds

# Setting up Python API
my_list = list()
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='Agile Tutorial', description='A simple Python API')

# Creating custom API namespaces
basic_ns = api.namespace('basic', description='List manipulation')
math_ns = api.namespace('math', description='Math operations')


@math_ns.route('/double')
@math_ns.doc(description='Multiply list by 2.')
class DoubleList(Resource):
    def put(self):
        return ms.double_list(my_list)


@api.route('/answer')
@api.doc(description='The Answer to the Ultimate Question of Life, the Universe, and Everything.')
class TheAnswer(Resource):
    def get(self):
        return ds.TheAnswerToLifeTheUniverseAndEverything()

@basic_ns.route('/input/<string:csv>')
@basic_ns.doc(params={'csv': 'Comma-separated integer values.'}, description='Inputs list.')
class InputList(Resource):
    def post(self, csv):
        my_list.clear()
        my_list.extend(bs.csv_to_list(csv))
        return my_list

@basic_ns.route('/reverse')
@basic_ns.doc(description='Reverse list.')
class ReverseList(Resource):
    def put(self):
        my_list.reverse()
        
@basic_ns.route('/reset')
@basic_ns.doc(description='Reset list.')
class ResetList(Resource):
    def delete(self):
        my_list.clear()
        return my_list

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
