from flask import Flask, Blueprint, jsonify
from flask_restplus import Api, Resource, fields
import nw_service as service

api_v1_network = Blueprint('api_v1_network', __name__, url_prefix='/api/1/network')

api = Api(api_v1_network, version='1.0', title='Network REST API',
    description='Network info',
)

ns = api.namespace('nw', description='Network REST API')


@ns.route('/ioCounters')
class NetworkIoCounters(Resource):

    def get(self):
        return jsonify(service.getNIC())

@ns.route('/ifStats')
class NetworkIfStats(Resource):

    def get(self):

        return jsonify(service.getIS())

@ns.route('/ifAddrs')
class NetworkIfAddrs(Resource):

    def get(self):
        return jsonify(service.getNIA())

@ns.route('/netInfo')
class NetInfo(Resource):

    def get(self):
        ans = []
        ans.append(service.getNIC())
        ans.append(service.getNIA())
        ans.append(service.getIS())
        return jsonify(net_info=ans)


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api_v1_network)
    app.run(debug=True)

