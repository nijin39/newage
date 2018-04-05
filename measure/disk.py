from flask import Flask
from flask import jsonify
import psutil

app = Flask(__name__)

@app.route("/disk/partitions")
def part():
    """
    psutil.disk_partitions()
    [sdiskpart(device='/dev/sda1', mountpoint='/', fstype='ext4', opts='rw,relatime,errors=remount-ro,data=ordered')]
    """

    temp_part = psutil.disk_partitions()[0]

    part = {"device": temp_part.device, "mountpoint" : temp_part.mountpoint, "fstype" : temp_part.fstype, "opts" : temp_part.opts}
    return jsonify(Partitions = part)

@app.route("/disk/usage")
def usage():
    """
    psutil.disk_usage('/')
    sdiskusage(total=44255346688, used=7377563648, free=34606149632, percent=17.6)
    """

    temp_usage = psutil.disk_usage('/')

    use = {"total" : temp_usage.total, "used" : temp_usage.used, "free" : temp_usage.free, "percent" : temp_usage.percent}
    return jsonify(Usage = use)


@app.route("/disk/io/counters")
def count():
    '''
    psutil.disk_io_counters(perdisk=False)
    sdiskio(read_count=50509, write_count=20688, read_bytes=1273859072, write_bytes=933240832, read_time=53948, write_time=61260, read_merged_count=5180, write_merged_count=29411, busy_time=41644)
    '''

    temp_count = psutil.disk_io_counters(perdisk=False)

    count = {"read_count" : temp_count.read_count, "write_count" : temp_count.write_count}
    return jsonify(Counter = count)

if __name__ == "__main__":
    app.run()

