from psutil import pids, Process

def get_process_info():
    procs = dict()
    for pid in pids():
        proc = Process(pid=pid)
        proc.cpu_percent(interval=0.0)
        procs[proc.name()] = float(proc.cpu_percent(interval=0.0))
    return procs