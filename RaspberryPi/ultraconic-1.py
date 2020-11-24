import time
from RPi import GPIO

#GPIO.setwarnings(False)
Trig_Pin=20
Echo_Pin=21
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setup(Trig_Pin,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Echo_Pin,GPIO.IN)
time.sleep(2)

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
    return (t2-t1)*340*100/2

if __name__=="__main__":
    print('aa')
    try:
        while True:
            print('Distance:%0.2f cm' % get_distance())
            time.sleep(1)
    except KeyboardInterrupt:
        print('bye')
    finally:
        GPIO.cleanup()