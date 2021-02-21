import math
import sys


percentages = {}
statuses = {}

def percentagesInit():
    for i in f.list:
        percentages[i]=200



def write(selected):
    current = statuses[selected]['current']
    al = statuses[selected]['all']
    percent = statuses[selected]['percent']
    sys.stdout.write('\r')
    sys.stdout.write(str(current))
    sys.stdout.write('/')
    sys.stdout.write(str(al))
    sys.stdout.write('  ')
    sys.stdout.write(str(percent))
    sys.stdout.write('%')
    sys.stdout.flush()
    return True

def update(selected, current, al):
    if not selected in statuses:
        statuses[selected] = {}
    statuses[selected] = {
        'current' : current,
        'all'     : math.floor(al),
        'percent' : math.floor((current/al)*100)
    }


def status(selected, current, al):
    now = -1
    if selected in statuses:
        now = statuses[selected]['percent']
    update(selected, current, al)
    if now == statuses[selected]['percent'] :
        return False
    write(selected)
    return True

def end(selected):
    statuses[selected]['current'] = statuses[selected]['all']
    statuses[selected]['percent'] = 100

def endWrite(selected):
    end(selected)
    write(selected)
    print(' ... ok')
