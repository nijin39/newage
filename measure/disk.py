from flask import Flask, Blueprint, jsonify
from flask_restplus import Api, Resource, fields
import psutil

api_v1_disk = Blueprint('api_v1_disk', __name__, url_prefix='/api/1/disk')

api = Api(api_v1_disk, version='1.0', title='Disk Information', description='Show Disk Information')

ns = api.namespace('disk', description='Disk Information')


def part():
    """
    psutil.disk_partitions()
    [sdiskpart(device='/dev/sda1', mountpoint='/', fstype='ext4', opts='rw,relatime,errors=remount-ro,data=ordered')]
    """

    temp_part = psutil.disk_partitions()[0]

    part = {"device": temp_part.device, "mountpoint": temp_part.mountpoint, "fstype": temp_part.fstype,
            "opts": temp_part.opts}
    return part

@ns.route('/partitions')
class diskPartitions(Resource):
    def get(self):
        return jsonify(part())

def usage():
    """
    psutil.disk_usage('/')
    sdiskusage(total=44255346688, used=7377563648, free=34606149632, percent=17.6)
    """

    temp_usage = psutil.disk_usage('/')

    use = {"total" : temp_usage.total, "used" : temp_usage.used, "free" : temp_usage.free, "percent" : temp_usage.percent}
    return use

@ns.route('/usage')
class diskUsage(Resource):
    def get(self):
        return jsonify(usage())

def count():
    '''
    psutil.disk_io_counters(perdisk=False)
    sdiskio(read_count=50509, write_count=20688, read_bytes=1273859072, write_bytes=933240832, read_time=53948, write_time=61260, read_merged_count=5180, write_merged_count=29411, busy_time=41644)
    '''

    temp_count = psutil.disk_io_counters(perdisk=False)

    count = {"read_count" : temp_count.read_count, "write_count" : temp_count.write_count}
    return count

@ns.route('/ioCounters')
class diskIoCounters(Resource):
    def get(self):
        return jsonify(count())

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api_v1_disk)
    app.run(debug=True)
