import json
import psutil


def get():
    '''Get Virtual Memory'''
    # print(str)
    # for key, value in vm.items():
    #    print(key, value)
    return json.dumps(psutil.virtual_memory()._asdict())

def get2(): #def get():
    '''Get Swap Memory'''
    # print(str)
    return json.dumps(psutil.swap_memory()._asdict())

get()
print(get2())