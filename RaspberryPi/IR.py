import time
from RPi import GPIO

if __name__=='__main__':
    PIR_PIN=18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN,GPIO.IN)
    try:
        while True:
            print(GPIO.input(PIR_PIN))
            time.sleep(1)
    except eyboardInterrupt:
        print('bye')
    finally:
        GPIO.cleanup()