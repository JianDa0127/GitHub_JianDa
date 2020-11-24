import os
import time

def get_path():
    p= '/sys/bus/w1/devices/'
    l=os.listdir(p)
    for i in l:
        if '28' in i:
            return p+i+'/'
    raise FileNotFoundError('1-wire device not found')

def get_temp():
    with open(get_path()+'w1_slave','r',encoding='utf-8') as f:
        t = f.read()
    t=int(t.split(' ')[-1].strip()[2:])/1000
    return t
if __name__=='__main__':
    try:
        while True:
            print(get_temp())
            time.sleep(0.5)
    except KeyboardInterrupt:
        print('bye')