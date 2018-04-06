from flask import Flask, Blueprint
from measure.cpu import api_v1_cpu
from measure.storage import api_v1_storage
from measure.cpuinfo import api_v1_cpuinfo
from measure.network import api_v1_network
from measure.disk import api_v1_disk
from measure.process import api_v1_process
from measure.memory import api_v1_memory

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api_v1_cpuinfo)
    app.register_blueprint(api_v1_storage)
    app.register_blueprint(api_v1_network)
    app.register_blueprint(api_v1_disk)
    app.register_blueprint(api_v1_process)
    app.register_blueprint(api_v1_memory)
    app.run(debug=True)
