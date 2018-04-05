from flask import Flask, Blueprint, jsonify
from flask_restplus import Api, Resource, fields
import psutil

api_v1_network = Blueprint('api_v1_network', __name__, url_prefix='/api/1/network')

api = Api(api_v1_network, version='1.0', title='Network REST API',
    description='Network info',
)

ns = api.namespace('nw', description='Network REST API')

def getNIC():
    return {"net_io_counters" : psutil.net_io_counters()._asdict()}

@ns.route('/ioCounters')
class getNetworkIoCounters(Resource):

    def get(self):
        return jsonify(getNIC())

def getIS():
    ans = {}
    data = psutil.net_if_stats()
    for st in data:
        ans[st] = data[st]._asdict()
    return {"net_if_stats" : ans}
@ns.route('/ifStats')
class getNetworkIfStats(Resource):

    def get(self):

        return jsonify(getIS())

def getNIA():
    ans = {}
    data = psutil.net_if_addrs()
    for key in data.keys():
        arr = []
        for i in range(0, len(data[key])):

            arr.append(data[key][i]._asdict())
        ans[key] = arr
    return {"net_if_addrs" : ans}

@ns.route('/ifAddrs')
class getNetworkIfAddrs(Resource):

    def get(self):
        return jsonify(getNIA())

@ns.route('/netInfo')
class getNetworkIfAddrs(Resource):

    def get(self):
        ans = []
        ans.append(getNIC())
        ans.append(getNIA())
        ans.append(getIS())
        return jsonify(net_info=ans)


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api_v1_network)
    app.run(debug=True)

