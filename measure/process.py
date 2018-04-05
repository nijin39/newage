'''
GET /process/
[{process_name:cpu_usage},...]

psutil.pids()
psutil.Process(pid=?) => 'name' & .cpu_percent()

'''

from flask import Flask, Blueprint, jsonify
from flask_restplus import Api, Resource, fields
from processinfo import get_process_info

api_v1_process = Blueprint('api_v1_process', __name__, url_prefix='/api/1/process')

api = Api(api_v1_process, version='1.0', title='Process Info API',
    description='get process information',
)

ns = api.namespace('pcs', description='Process Info API')

@ns.route("/process")
class GetProcessInfo(Resource):
    def get(self):
        return jsonify(procinfo = get_process_info())

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api_v1_process)
    app.run(debug=True)