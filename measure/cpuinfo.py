'''
==========================================
= This is an output of cpu's measurement =
==========================================
'''
from flask import Flask, Blueprint, jsonify
from flask_restplus import Api, Resource, fields
import psutil
from measure.cpu_service import getCpuStats, getCpuTimes, getCpuUsage

api_v1_cpuinfo = Blueprint('api_v1_cpuinfo', __name__, url_prefix='/api/1/cpuinfo')
api = Api(api_v1_cpuinfo, version='1.0', title='CPU Measurement', description='This is details of CPU Measurement',)
ns = api.namespace('cpu', description = 'cpu measurements')

@ns.route('/stats')
class CpuStats(Resource):
    def get(self):
        '''Shows CPU_stats'''
        return jsonify(getCpuStats())

@ns.route('/times')
class CpuTimes(Resource):
    def get(self):
        '''Shows CPU_times'''
        return jsonify(getCpuTimes())

@ns.route('/usage')
class CpuUsage(Resource):
    def get(self):
        '''Shows CPU_usage'''
        return jsonify(getCpuUsage())

if __name__== "__main__":
    app.Flask(__name__)
    app.register_blueprint(api_v1_cpuinfo)
    app.run(debug=True)
    #print("LOG")
