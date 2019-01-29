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

@basic_ns.route('/print')
@basic_ns.doc(description='Print list.')
class PrintList(Resource):
    def get(self):
        return my_list

@basic_ns.route('/sort')
@basic_ns.doc(description='Sort list.')
class SortList(Resource):
    def put(self):
        my_list.sort()
        return my_list


@math_ns.route('/product')
@math_ns.doc(description='Product of the list.')
class ProductList(Resource):
    def get(self):
        return ms.product(my_list)


@math_ns.route('/max')
@math_ns.doc(description='Max value of the list.')
class MaxList(Resource):
    def get(self):
        return max(my_list)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))


@math_ns.route('/square')
@math_ns.doc(description='Takes the square of the list.')
class SquareList(Resource):
    def put(self):
        return ms.square_list(my_list)


@basic_ns.route('/insert/<int:integer>/<int:position>')
@basic_ns.doc(params={'integer': 'Integer value.', 'position': 'List position.'},
              description='Inserts a single integer value at a given position in the list.')
class InsertList(Resource):
    def put(self, integer, position):
        my_list.insert(position, integer)
        return my_list
