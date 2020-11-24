import matplotlib.pyplot as plt
from RPi import GPIO
import time

#GPIO.setwarnings(False)
Trig_Pin=20
Echo_Pin=21
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setup(Trig_Pin,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Echo_Pin,GPIO.IN)
time.sleep(2)
if __name__=="__main__":
    x=['14','15','16','10','20','21','22','23','26','27']
    y=[2950,2985,2970,3020,3100,3120,3150,3195,3205,3160]
    
    plt.plot(x,y)
    plt.show()
    GPIO.cleanup()