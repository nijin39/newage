'''
==========================================
= This is get cpu measurement functions  =
=        for cpuinfo.py         =
==========================================
'''

import psutil

def getCpuStats():
    return {"cpu_stats":psutil.cpu_stats()._asdict()}


def getCpuTimes():
    return {"cpu_times":psutil.cpu_times()._asdict()}


def getCpuUsage():
    return {"cpu_usage" : psutil.cpu_percent(interval=1)}
