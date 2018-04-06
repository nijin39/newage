from flask import Flask, Blueprint, jsonify
from flask_restplus import Api, Resource, fields
import psutil
import json

api_v1_memory = Blueprint('api_v1_memory', __name__, url_prefix='/api/1/memory')
api = Api(api_v1_memory, version='1.0', title='Memory API',
          description='Getting Memory Infomation API',
          )
ns = api.namespace('memory', description='Memory operations')

parser = api.parser()
parser.add_argument('task', type=str, required=True, help='The task details', location='form')

@ns.route('/virtualMemory')
class VirtualMemory(Resource):
    def get(self):
        '''Get Virtual Memory
        Success : json of Virtual memory infomation
        Fail : Err Virtual memory
        '''
        try:
            return jsonify(results=psutil.virtual_memory()._asdict())
        except:
            return jsonify(results='Err Virtual Memory')

@ns.route('/swapMemory')
class SwapMemory(Resource):
    def get(self):
        '''Get Swap Memory
        Success : json of Swap memory infomation
        Fail : Err Swap memory
        '''
        try:
            return jsonify(results=psutil.swap_memory()._asdict())
        except:
            return jsonify(results='Err Swap Memory')

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api_v1_memory)
    app.run(debug=True)

