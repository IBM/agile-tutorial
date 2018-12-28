import os

from flask import Flask
from flask_restplus import Api, Resource
from werkzeug.contrib.fixers import ProxyFix

from src import default_functions as df

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
        return df.TheAnswerToLifeTheUniverseAndEverything()


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
