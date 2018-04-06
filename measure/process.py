from flask import Flask, Blueprint, jsonify
from flask_restplus import Api, Resource, fields
from measure.processinfo import get_process_info

api_v1_process = Blueprint('api_v1_process', __name__, url_prefix='/api/1/process')

api = Api(api_v1_process, version='1.0', title='Process Info API',
    description='get process information',
)

ns = api.namespace('pcs', description='Process Info API')
ERRMSG = "Error: can't get process information"

@ns.route("/process")
class GetProcessInfo(Resource):
    def get(self):
        try:
            return jsonify(procinfo = get_process_info())
        except:
            return ERRMSG

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api_v1_process)
    app.run(debug=True)
