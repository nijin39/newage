from flask import Flask, Blueprint, jsonify
from flask_restplus import Api, Resource, fields
from measure import disk_service

api_v1_disk = Blueprint('api_v1_disk', __name__, url_prefix='/api/1/disk')

api = Api(api_v1_disk, version='1.0', title='Disk Information', description='Show Disk Information')

ns = api.namespace('disk', description='Disk Information')

parser = api.parser()
parser.add_argument('task', type=str, required=True, help='The task details', location='form')



@ns.route('/partitions')
class diskPartitions(Resource):

    def get(self):
        return jsonify(disk_service.part())


@ns.route('/usage')
class diskUsage(Resource):

    def get(self):
        return jsonify(disk_service.usage())

@ns.route('/ioCounters')
class diskIoCounters(Resource):

    def get(self):
        return jsonify(disk_service.count())

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api_v1_disk)
    app.run(debug=True)
