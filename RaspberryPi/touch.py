import time
from RPi import GPIO
if __name__=='__main__':
    GPIO.setmode(GPIO.BCM)
    PAD_Pin=17
    LED_Pin=27
    GPIO.setup(PAD_Pin,GPIO.IN)
    GPIO.setup(LED_Pin,GPIO.OUT)
    light=False
    try:
        while True:
            if GPIO.input(PAD_Pin):
                
                light=False if light else True
            if light:
                
                GPIO.output(LED_Pin,1)
            else:
                GPIO.output(LED_Pin,0)
    except KeyboardInterrupt:
        print('bye')
    finally:
        GPIO.cleanup()