from flask import Flask, Blueprint
from measure.cpu import api_v1_cpu
from measure.storage import api_v1_storage
from measure.network import api_v1_network

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api_v1_cpu)
    app.register_blueprint(api_v1_storage)
    app.register_blueprint(api_v1_network)
    app.run(debug=True)
