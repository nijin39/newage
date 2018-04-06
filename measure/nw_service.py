import psutil, subprocess

def getNIC():
    return {"net_io_counters" : psutil.net_io_counters()._asdict()}

def getNIA():
    ans = {}
    data = psutil.net_if_addrs()
    for key in data.keys():
        arr = []
        for i in range(0, len(data[key])):

            arr.append(data[key][i]._asdict())
        ans[key] = arr
    return {"net_if_addrs" : ans}

def getIS():
    ans = {}
    data = psutil.net_if_stats()
    for key in data:
        ans[key] = data[key]._asdict()
    return {"net_if_stats" : ans}

def executeCommand(cmd):
    with psutil.Popen(cmd, stdout=subprocess.PIPE) as proc:
        data = proc.stdout.read().decode('utf-8')

    return data
