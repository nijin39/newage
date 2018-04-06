import psutil
from operator import itemgetter

NAME = 'name'
CPUPERCENT = 'cpu_percent'

def get_process_info():
    procs = list()
    try:
        for proc in psutil.process_iter():
            procs.append(proc.as_dict([NAME, CPUPERCENT]))
        procs.sort(key=lambda p: p[NAME].lower())
        return sorted(procs, key=itemgetter(CPUPERCENT), reverse=True)
    except:
        return None