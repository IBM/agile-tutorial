import os
from flask import Flask, jsonify
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app,
          version='1.0',
          doc='/apidocs/',
          title='My first Python API',
          description='A number-crunching API')


@api.route('/double/<int:number>')
@api.doc(params={'number': 'Number to be doubled.'},
         description='This method doubles the input.')
class DoubleNumber(Resource):
    def get(self, number):
        return jsonify(result=2 * number)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
