import os

from flask import Flask, jsonify
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', doc='/apidocs/', title='Agile Tutorial', description='Python API')
my_list = list()


@api.route('/list/print')
@api.doc(description='Print current list.')
class PrintList(Resource):
    def get(self):
        return jsonify(list=my_list)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
