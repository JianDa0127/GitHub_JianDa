import time
import sys
import os
from RPi import GPIO
import smbus2
from RPLCD.i2c import CharLCD
sys.modules['smbus'] = smbus2

#GPIO.setwarnings(False)
Trig_Pin=20
Echo_Pin=21
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setup(Trig_Pin,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Echo_Pin,GPIO.IN)
time.sleep(2)

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

def get_distance():
    GPIO.output(Trig_Pin,GPIO.HIGH)
    time.sleep(0.000100)
    GPIO.output(Trig_Pin,GPIO.LOW)
    while not GPIO.input(Echo_Pin):
        pass
    t1=time.time()
    while GPIO.input(Echo_Pin):
        pass
    t2=time.time()
    temp=get_temp()
    v=331.6+0.6*temp
    return (t2-t1)*v*100/2

if __name__=="__main__":
    lcd = CharLCD('PCF8574', address=0x27, port=1, backlight_enabled=True)
    lcd.clear()
    try:
        while True:
            lcd.write_string('D:%0.2fcm' % get_distance())
            time.sleep(1)
            lcd.clear()
    except KeyboardInterrupt:
        print('bye')
    finally:
        GPIO.cleanup()