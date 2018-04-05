from flask import Flask, Blueprint
from flask_restplus import Api, Resource, fields
import json
import psutil

api_v1_memory = Blueprint('api_v1_memory', __name__, url_prefix='/api/1/memory')
api = Api(api_v1_memory, version='1.0', title='Memory API',
          description='Getting Memory Infomation API',
          )

parser = api.parser()
parser.add_argument('task', type=str, required=True, help='The task details', location='form')

@api.route('/virtualMemory')
class VirtualMemory(Resource):
    def get(self):
        '''Get Virtual Memory
        Success : json of Virtual memory infomation
        Fail : Err Virtual memory
        '''
        str = ''
        try:
            str = json.dumps(psutil.virtual_memory()._asdict())
        except:
            str = 'Err Virtual Memory'
        finally:
            return str

@api.route('/swapMemory')
class SwapMemory(Resource):
    def get(self):
        '''Get Swap Memory
        Success : json of Swap memory infomation
        Fail : Err Swap memory
        '''
        str = ''
        try:
            str = json.dumps(psutil.swap_memory()._asdict())
        except:
            str = 'Err Swap Memory'
        finally:
            return str

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api_v1_memory)
    app.run(debug=True)
