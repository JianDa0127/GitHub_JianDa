path='/sys/bus/w1/devices/28-3c01b556d427/'

if __name__=='__main__':
    with open(path+'w1_slave','r',encoding='utf-8') as f:
        temp = f.read()
    print(temp)