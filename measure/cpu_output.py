'''
==========================================
= This is an output of cpu's measurement =
==========================================
'''

from flask import Flask, Blueprint, jsonify
from flask_restplus import Api, Resource, fields
import psutil

api_5_cpu = Blueprint('api_5_cpu', __name__, url_prefix='/api/cpu')
api = Api(api_5_cpu, version='1.0', title='CPU Measurement', description='This is details of CPU Measurement',)
ns = api.namespace('cpu', description = 'cpu measurements')

#@ns.route('/freq')
#class CpuFreq(Resource):
#    def get(self):
#        '''Shows CPU_freq'''
#        cpufreq = {"current":psutil.cpu_freq()[0], "min":psutil.cpu_freq()[1], "max":psutil.cpu_freq()[2]}
#        return jsonify(CPU_freq=cpufreq)
#

@ns.route('/stats')
class CpuStats(Resource):
    def get(self):
        '''Shows CPU_stats'''
        cpustats = {"ctx_switches":psutil.cpu_stats()[0], "interrupts":psutil.cpu_stats()[1], "soft_interrupts":psutil.cpu_stats()[2], "syscalls":psutil.cpu_stats()[3], }
        return jsonify(CPU_stats=cpustats)

@ns.route('/times')
class CpuTimes(Resource):
    def get(self):
        '''Shows CPU_times'''
        cputimes = {"user":psutil.cpu_times()[0],"nice":psutil.cpu_times()[1],"system":psutil.cpu_times()[2],"idle":psutil.cpu_times()[3],"iowait":psutil.cpu_times()[4],"irq":psutil.cpu_times()[5],"softirq":psutil.cpu_times()[6],"steal":psutil.cpu_times()[7],"guest":psutil.cpu_times()[8],"guest_nice":psutil.cpu_times()[9]}
        return jsonify(CPU_times=cputimes)

@ns.route('/usage')
class CpuUsage(Resource):
    def get(self):
        '''Shows CPU_usage'''
        cpuusage = {"usage":psutil.cpu_percent(interval=1)}
        return jsonify(CPU_usage=cpuusage)

if __name__== "__main__":
	app.Flask(__name__)
	app.register_blueprint(api_5)
	app.run(debug=True)
