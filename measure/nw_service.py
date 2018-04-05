import psutil

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