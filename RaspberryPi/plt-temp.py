import matplotlib.pyplot as plt
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

if __name__=="__main__":
    x=['1','2','3','4','5','6','7','8','9','10','11','12']
    y=[]
    try:
        for i in range(12):
            y.append(get_temp())
            time.sleep(2)
    except KeyboardInterrupt:
        print('bye')
    
    plt.plot(x,y)
    plt.show()